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

## Branch Structure & Pull Request Guide

### Important: Branch Information
⚠️ **Always target the `static` branch for pull requests!**

- **`static` branch**: Current active React-based website (target for all PRs)
- **`main` branch**: Legacy Python/Reflex version (deprecated, do not use)
- **`gh-pages` branch**: Auto-generated deployment branch (do not modify directly)

### How to Contribute

1. **Fork and clone the repository**
   ```bash
   git clone https://github.com/YOUR-USERNAME/RISE-website.git
   cd RISE-website
   git checkout static  # Make sure you're on the static branch
   ```

2. **Create a feature branch from static**
   ```bash
   git checkout -b feature/your-feature-name
   ```

3. **Make your changes**
   - Edit files in `rise-react-site/` directory
   - Test locally with `npm run dev`
   - Update publications if needed with `npm run update-publications`

4. **Test your changes**
   ```bash
   cd rise-react-site
   npm run dev      # Test development server
   npm run build    # Test production build
   npm run preview  # Test production preview
   ```

5. **Commit and push**
   ```bash
   git add .
   git commit -m "Add: brief description of changes"
   git push origin feature/your-feature-name
   ```

6. **Create Pull Request**
   - Go to GitHub and create a PR
   - **Set base branch to `static`** (not main!)
   - Add clear description of changes
   - Reference any related issues

7. **After merge**
   - Changes will be automatically deployed to GitHub Pages
   - The `gh-pages` branch will be updated automatically

### Common Contribution Types

- **Content Updates**: Edit React components in `src/pages/`
- **Styling Changes**: Modify CSS files in component directories
- **New Team Members**: Update `src/pages/People/People.jsx`
- **Publications**: System auto-updates, but can manually update `public/data/publications.json`
- **Images**: Add to `public/images/` directory

## Contributing

1. Follow the PR guide above
2. Make your changes on a feature branch from `static`
3. Test locally before submitting
4. Create PR targeting `static` branch
5. Changes will be deployed automatically after merge