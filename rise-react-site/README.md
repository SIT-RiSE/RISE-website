# RISSE Lab Website

A modern, responsive React website for the RISSE Lab (Research in Software Engineering) at Stevens Institute of Technology. Built with Vite and optimized for GitHub Pages deployment.

## 🚀 Features

- **Modern React Architecture**: Built with React 19 and Vite for fast development and optimal performance
- **Responsive Design**: Mobile-first design that works seamlessly across all devices
- **Interactive Animations**: Dynamic pixel canvas animation and smooth hover effects
- **GitHub Pages Ready**: Configured with HashRouter for seamless static deployment
- **Performance Optimized**: Fast loading with code splitting and optimized assets

## 📋 Pages

- **Home**: Interactive landing page with lab introduction and recent news
- **Research**: Showcase of research areas and ongoing projects
- **Publications**: Dynamic publication list loaded from JSON data
- **People**: Team member profiles and contact information
- **About**: Comprehensive lab information and facilities

## 🛠️ Technologies

- **React 19** - Modern React with latest features
- **Vite 7** - Fast build tool and development server
- **React Router DOM** - Client-side routing with HashRouter for GitHub Pages
- **Framer Motion** - Smooth animations and transitions
- **CSS3** - Modern styling with animations and responsive design

## 📦 Installation & Setup

### Prerequisites
- Node.js (v18 or higher)
- npm or yarn package manager
- Git

### Development Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/your-username/RISSE-website.git
   cd RISSE-website/rise-react-site
   ```

2. **Install dependencies**
   ```bash
   npm install
   ```

3. **Start development server**
   ```bash
   npm run dev
   ```

   The site will be available at `http://localhost:5173`

4. **Build for production**
   ```bash
   npm run build
   ```

5. **Preview production build**
   ```bash
   npm run preview
   ```

## 🌐 GitHub Pages Deployment

### Automatic Deployment

1. **Push your code to GitHub**
   ```bash
   git add .
   git commit -m "Initial commit"
   git push origin main
   ```

2. **Deploy to GitHub Pages**
   ```bash
   npm run deploy
   ```

   This command will:
   - Build the project (`npm run build`)
   - Deploy the `dist` folder to `gh-pages` branch
   - Make the site available at `https://your-username.github.io/repository-name`

### Manual GitHub Pages Setup

1. Go to your repository settings on GitHub
2. Navigate to "Pages" section
3. Set source to "Deploy from a branch"
4. Select `gh-pages` branch and `/ (root)` folder
5. Save the configuration

### Custom Domain (Optional)

1. Add a `CNAME` file to the `public` folder with your domain
2. Configure DNS settings with your domain provider
3. Enable "Enforce HTTPS" in GitHub Pages settings

## 📁 Project Structure

```
rise-react-site/
├── public/                 # Static assets
│   ├── images/            # Images and logos
│   │   ├── logo/         # Lab and institution logos
│   │   └── people/       # Team member photos
│   └── data/             # JSON data files
│       └── publications.json
├── src/
│   ├── components/       # Reusable components
│   │   ├── Banner/       # Hero banner with pixel animation
│   │   ├── Layout/       # Main layout wrapper
│   │   └── Navbar/       # Navigation component
│   ├── pages/           # Page components
│   │   ├── Home/        # Landing page
│   │   ├── Research/    # Research areas
│   │   ├── Publications/ # Publications list
│   │   ├── People/      # Team members
│   │   └── About/       # Lab information
│   ├── styles/          # Global styles
│   │   └── global.css   # Global CSS variables and utilities
│   ├── App.jsx          # Main app with routing
│   └── main.jsx         # Application entry point
├── package.json         # Dependencies and scripts
├── vite.config.js       # Vite configuration
└── README.md           # This file
```

## 🔧 Configuration

### Vite Configuration

The project uses a custom Vite configuration optimized for GitHub Pages:

```javascript
// vite.config.js
export default defineConfig({
  plugins: [react()],
  base: './',  // Relative paths for GitHub Pages
})
```

### Router Configuration

Uses HashRouter for GitHub Pages compatibility:

```javascript
// Ensures routing works on GitHub Pages
import { HashRouter } from 'react-router-dom';
```

## 📝 Content Management

### Publications

Update publications by editing `/public/data/publications.json`:

```json
{
  "publications": [
    {
      "title": "Your Paper Title",
      "authors": "Author Names",
      "venue": "Conference/Journal Name",
      "year": "2024",
      "type": "conference"
    }
  ]
}
```

### Images

- **Logos**: Place in `/public/images/logo/`
- **People Photos**: Place in `/public/images/people/`
- **Other Images**: Place in appropriate subdirectories under `/public/images/`

### Styling

- **Global Styles**: `/src/styles/global.css`
- **Component Styles**: Each component has its own CSS file
- **Responsive Design**: Uses CSS media queries for mobile optimization

## 🚀 Deployment Workflow

1. **Make Changes**: Edit components, styles, or content
2. **Test Locally**: Run `npm run dev` to test changes
3. **Build**: Run `npm run build` to create production build
4. **Deploy**: Run `npm run deploy` to publish to GitHub Pages
5. **Verify**: Check your live site at the GitHub Pages URL

## 🐛 Troubleshooting

### Common Issues

**Routing doesn't work on GitHub Pages**
- Ensure you're using HashRouter, not BrowserRouter
- Check that `base: './'` is set in vite.config.js

**Images not loading**
- Verify images are in the `/public/images/` directory
- Use absolute paths starting with `/images/`

**Deployment fails**
- Check that `gh-pages` package is installed
- Ensure you have push permissions to the repository
- Verify the repository name matches your GitHub Pages URL

## 📄 License

© 2025 RISSE Lab @ Stevens Institute of Technology

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

---

**RISSE Lab** - Research in Software Engineering
Stevens Institute of Technology
Contact: lxiao6@stevens.edu