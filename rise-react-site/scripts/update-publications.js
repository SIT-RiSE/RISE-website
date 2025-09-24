#!/usr/bin/env node

/**
 * Node.js wrapper for the Python publication fetcher script.
 * This script can be integrated into the npm build process.
 */

import { spawn } from 'child_process';
import path from 'path';
import { promises as fs } from 'fs';
import { fileURLToPath } from 'url';

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);

async function checkPythonDependencies() {
    return new Promise((resolve) => {
        // Try different Python executables
        const pythonCommands = [
            // Try virtual environment in project root
            path.join(__dirname, '..', '..', '.venv', 'bin', 'python'),
            // Try virtual environment in rise-react-site directory
            path.join(__dirname, '..', '.venv', 'bin', 'python'),
            // Try system Python installations
            'python3',
            'python'
        ];

        let tried = 0;
        
        function tryNextPython() {
            if (tried >= pythonCommands.length) {
                resolve({ success: false, python: null });
                return;
            }

            const pythonCmd = pythonCommands[tried];
            tried++;

            const checkCmd = spawn(pythonCmd, ['-c', 'import scholarly, tqdm; print("Dependencies OK")'], {
                stdio: 'pipe'
            });

            let output = '';
            checkCmd.stdout.on('data', (data) => {
                output += data.toString();
            });

            checkCmd.on('close', (code) => {
                if (code === 0 && output.includes('Dependencies OK')) {
                    resolve({ success: true, python: pythonCmd });
                } else {
                    tryNextPython();
                }
            });

            checkCmd.on('error', () => {
                tryNextPython();
            });
        }

        tryNextPython();
    });
}

async function runPythonScript(pythonExecutable) {
    return new Promise((resolve, reject) => {
        const scriptPath = path.join(__dirname, 'fetch-publications.py');
        const pythonProcess = spawn(pythonExecutable, [scriptPath], {
            stdio: 'inherit',
            cwd: __dirname
        });

        pythonProcess.on('close', (code) => {
            if (code === 0) {
                resolve();
            } else {
                reject(new Error(`Python script exited with code ${code}`));
            }
        });

        pythonProcess.on('error', (err) => {
            reject(new Error(`Failed to start Python script: ${err.message}`));
        });
    });
}

async function checkIfPublicationFileExists() {
    const publicationsPath = path.join(__dirname, '..', 'public', 'data', 'publications.json');
    try {
        await fs.access(publicationsPath);
        return true;
    } catch {
        return false;
    }
}

async function main() {
    console.log('🔄 Checking for publication updates...');

    // Check if publications file exists
    const hasPublications = await checkIfPublicationFileExists();
    
    // Check if Python dependencies are available
    const pythonCheck = await checkPythonDependencies();

    if (!pythonCheck.success) {
        console.log('⚠️  Python dependencies (scholarly, tqdm) not found.');
        
        if (!hasPublications) {
            console.log('❌ No existing publications.json found and cannot fetch new data.');
            console.log('💡 Please install Python dependencies: pip install scholarly tqdm');
            process.exit(1);
        } else {
            console.log('✅ Using existing publications.json file.');
            console.log('💡 To enable automatic updates, install: pip install scholarly tqdm');
            return;
        }
    }

    try {
        console.log('🔍 Fetching latest publications from Google Scholar...');
        console.log(`Using Python: ${pythonCheck.python}`);
        await runPythonScript(pythonCheck.python);
        console.log('✅ Publications updated successfully!');
    } catch (error) {
        console.error('❌ Failed to update publications:', error.message);
        
        if (!hasPublications) {
            console.error('❌ No fallback publications file available.');
            process.exit(1);
        } else {
            console.log('✅ Continuing with existing publications.json');
        }
    }
}

// Handle command line arguments
if (process.argv.includes('--force')) {
    console.log('🚀 Force updating publications...');
}

if (process.argv.includes('--help')) {
    console.log(`
📚 Publication Updater

Usage: node update-publications.js [options]

Options:
  --force    Force update even if recent update exists
  --help     Show this help message

Requirements:
  - Python 3
  - pip install scholarly tqdm

The script will:
1. Check if Python dependencies are available
2. Fetch latest publications from Google Scholar
3. Perform incremental updates (merge with existing data)
4. Update citation counts
5. Save to public/data/publications.json
`);
    process.exit(0);
}

main().catch((error) => {
    console.error('❌ Unexpected error:', error);
    process.exit(1);
});