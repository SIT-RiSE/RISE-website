# Publication Auto-Update System

This system automatically fetches the latest publications from Google Scholar and performs incremental updates to the website's publication data.

## Features

- ✅ **Incremental Updates**: Only adds new publications and updates citation counts
- ✅ **Fallback Support**: Works even without Python dependencies (uses existing data)
- ✅ **Smart Merging**: Preserves existing data while updating with new information
- ✅ **Build Integration**: Automatically runs during build/deploy process
- ✅ **Manual Control**: Can be run independently when needed
- ✅ **Cross-Platform**: Works on different development environments

## Setup

### 1. Install Python Dependencies

#### Option A: Using Virtual Environment (Recommended)

```bash
# Create virtual environment in project root
cd /path/to/RISE-website
python3 -m venv .venv

# Activate virtual environment
# On macOS/Linux:
source .venv/bin/activate
# On Windows:
# .venv\Scripts\activate

# Install required packages
pip install scholarly tqdm
```

#### Option B: Using System Python

```bash
# Install globally (not recommended for production)
pip3 install scholarly tqdm

# Or using the requirements file
pip3 install -r scripts/requirements.txt
```

### 2. Available Scripts

```bash
# Update publications manually
npm run update-publications

# Force update (ignore cache/recent updates)
npm run update-publications:force

# Build without updating publications  
npm run build:no-update

# Normal build (includes publication update)
npm run build

# Deploy (includes publication update)
npm run deploy
```

## How It Works

### Python Environment Detection:
The script automatically searches for Python in the following order:
1. `.venv/bin/python` in project root directory
2. `.venv/bin/python` in rise-react-site directory  
3. System `python3`
4. System `python`

### Automated Process (during build/deploy):
1. **Check Dependencies**: Verifies Python and required packages are available
2. **Load Existing Data**: Reads current publications.json file
3. **Fetch from Scholar**: Gets latest publications from Google Scholar (Lu Xiao's profile)
4. **Smart Merge**: 
   - Updates citation counts for existing publications
   - Adds genuinely new publications
   - Preserves all existing metadata
   - Filters out non-paper entries
5. **Save Results**: Updates publications.json with merged data
6. **Continue Build**: Proceeds with normal Vite build process

### Graceful Degradation:
- If Python dependencies are missing → Uses existing publications.json
- If Scholar API fails → Falls back to existing data
- If no existing data + no dependencies → Shows helpful error message

## Project Structure

```
RISE-website/
├── .venv/                          # Virtual environment (created by you)
│   └── bin/python                  # Python executable with dependencies
├── rise-react-site/
│   ├── scripts/
│   │   ├── README.md               # This file
│   │   ├── requirements.txt        # Python dependencies
│   │   ├── update-publications.js  # Node.js wrapper
│   │   └── fetch-publications.py   # Python script
│   └── public/data/
│       └── publications.json       # Generated publication data
```

## Manual Usage

```bash
# Update publications only
npm run update-publications

# Get help
node scripts/update-publications.js --help

# Force update
npm run update-publications:force
```

## Configuration

The Google Scholar author ID is configured in `fetch-publications.py`:
```python
author_id = "s2Z7NFYAAAAJ"  # Lu Xiao's Google Scholar ID
```

## Troubleshooting

### Python Dependencies Not Found
```bash
# Create and activate virtual environment
python3 -m venv .venv
source .venv/bin/activate  # On macOS/Linux
# or .venv\Scripts\activate  # On Windows

# Install dependencies
pip install scholarly tqdm
```

### Permission Issues
```bash
chmod +x scripts/*.py scripts/*.js
```

### Manual Fallback
If automated updates fail, you can manually copy publication data:
```bash
cp /path/to/manual/publications.json public/data/publications.json
```

## For New Contributors

When setting up this project on a new machine:

1. **Clone the repository**
2. **Create virtual environment**: `python3 -m venv .venv`
3. **Activate it**: `source .venv/bin/activate`
4. **Install Python deps**: `pip install scholarly tqdm`
5. **Install Node deps**: `npm install`
6. **Test**: `npm run update-publications`

The script will automatically find your virtual environment and use it.