# RISSE Lab Website Setup Guide

This guide helps new contributors set up the RISSE Lab website on their local machine.

## Quick Start

1. **Clone the repository**
   ```bash
   git clone https://github.com/SIT-RiSE/RISE-website.git
   cd RISE-website
   ```

2. **Set up Python environment** (for publication auto-updates)
   ```bash
   # Create virtual environment in project root
   python3 -m venv .venv
   
   # Activate it
   source .venv/bin/activate  # macOS/Linux
   # or .venv\Scripts\activate  # Windows
   
   # Install Python dependencies
   pip install scholarly tqdm
   ```

3. **Set up Node.js environment**
   ```bash
   cd rise-react-site
   npm install
   ```

4. **Test the setup**
   ```bash
   # Test publication update system
   npm run update-publications
   
   # Start development server
   npm run dev
   ```

5. **Deploy to GitHub Pages**
   ```bash
   npm run deploy
   ```

## Project Structure

```
RISE-website/
├── .venv/                     # Python virtual environment (you create this)
├── assets/                    # Original assets and scripts
├── rise-react-site/          # React application
│   ├── scripts/              # Publication update scripts
│   ├── src/                  # React source code
│   ├── public/               # Static files
│   └── package.json          # Node.js dependencies
└── RISSE_website/            # Original Python/Reflex version
```

## Development Workflow

1. **Make changes** to React components in `rise-react-site/src/`
2. **Test locally** with `npm run dev`
3. **Deploy** with `npm run deploy` (automatically updates publications)

## Publication System

The website automatically fetches and updates publications from Google Scholar:
- **Automatic**: Runs during every build/deploy
- **Filtered**: Only shows research papers (excludes books, proceedings, etc.)
- **Smart**: Updates citation counts and adds new papers incrementally

## Troubleshooting

### Python Environment Issues
```bash
# Recreate virtual environment
rm -rf .venv
python3 -m venv .venv
source .venv/bin/activate
pip install scholarly tqdm
```

### Node.js Issues
```bash
cd rise-react-site
rm -rf node_modules package-lock.json
npm install
```

### Publication Update Fails
The system gracefully falls back to existing data if Scholar API is unavailable.

## Contributing

1. Make your changes
2. Test locally
3. Create a pull request
4. Changes will be automatically deployed after merge