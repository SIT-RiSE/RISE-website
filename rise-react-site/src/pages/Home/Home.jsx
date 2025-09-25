import { useState, useEffect } from 'react';
import Banner from '../../components/Banner/Banner';
import './Home.css';

const Home = () => {
  const [recentPapers, setRecentPapers] = useState([]);

  const professor = {
    name: "Dr. Lu Xiao",
    title: "Associate Professor",
    image: `${import.meta.env.BASE_URL}images/people/lxiao6.webp`,
    bio: "Dr. Lu Xiao is an Associate Professor in the School of Systems and Enterprises at Stevens Institute of Technology. Her research focuses on software engineering, particularly software architecture, software economics, and software ecosystems. She has published her work in top-tier conferences and journals including ICSE, ESEM, FSE, and JSS.",
  };

  // Fetch recent papers from publications.json
  useEffect(() => {
    const fetchRecentPapers = async () => {
      try {
        const response = await fetch(`${import.meta.env.BASE_URL}data/publications.json`);
        const publications = await response.json();
        
        const currentYear = new Date().getFullYear();
        const recentYear = currentYear - 1; // Last year and this year
        
        const recent = publications
          .filter(pub => pub.year >= recentYear)
          .sort((a, b) => b.year - a.year) // Sort by year descending
          .slice(0, 2); // Take only the first 2
        
        setRecentPapers(recent);
      } catch (error) {
        console.error('Failed to fetch publications:', error);
      }
    };

    fetchRecentPapers();
  }, []);

  return (
    <div className="home">
      <Banner />

      {/* Lab Introduction Section */}
      <section className="section lab-intro-section">
        <div className="container">
          <h2 className="section-title">Lab Introduction</h2>
          <div className="lab-intro-content">
            <img
              src={professor.image}
              alt={professor.name}
              className="professor-image"
            />
            <div className="professor-info">
              <h3>{professor.name}</h3>
              <p className="text-gray">{professor.title}</p>
              <p>{professor.bio}</p>
            </div>
          </div>
        </div>
      </section>

      {/* Recent News Section */}
      <section className="section recent-news-section">
        <div className="container">
          <h2 className="section-title">Recent Publications</h2>
          <div className="news-glass-container">
            {recentPapers.length > 0 ? (
              recentPapers.map((paper, index) => (
                <div 
                  key={index} 
                  className="news-glass-item"
                  onMouseMove={(e) => {
                    const rect = e.currentTarget.getBoundingClientRect();
                    const x = ((e.clientX - rect.left) / rect.width) * 100;
                    const y = ((e.clientY - rect.top) / rect.height) * 100;
                    e.currentTarget.style.setProperty('--mouse-x', `${x}%`);
                    e.currentTarget.style.setProperty('--mouse-y', `${y}%`);
                  }}
                >
                  <div className="news-content">
                    <div className="news-year">{paper.year}</div>
                    <div className="news-title">{paper.title}</div>
                    <div className="news-authors">{paper.authors}</div>
                    {paper.venue && <div className="news-venue">{paper.venue}</div>}
                  </div>
                  <div className="news-glass-overlay"></div>
                </div>
              ))
            ) : (
              <div className="news-glass-item">
                <div className="news-content">
                  <div className="news-title">Loading recent publications...</div>
                </div>
                <div className="news-glass-overlay"></div>
              </div>
            )}
          </div>
        </div>
      </section>

      {/* Open Positions Section */}
      <section className="section">
        <div className="container text-center">
          <h2 className="section-title">Open Positions</h2>
          <p className="section-subtitle">
            We are always looking for students to join our research team.
          </p>
          <a href="#/about" className="btn-primary">
            Learn More
          </a>
        </div>
      </section>

      {/* Simplified Footer */}
      <footer className="home-footer">
        <div className="container">
          <div className="footer-content">
            {/* Left: Basic Lab Info */}
            <div className="footer-left">
              <h3 className="footer-title">RISSE Lab</h3>
              <p className="footer-subtitle">Research in Software Engineering</p>
              <p className="footer-address">Stevens Institute of Technology</p>
              <p className="footer-email">Email: lxiao6@stevens.edu</p>
            </div>

            <div className="footer-right">
              <div className="footer-logos">
                <img
                  src={`${import.meta.env.BASE_URL}images/logo/sit.png`}
                  alt="Stevens Institute of Technology"
                  className="footer-logo stevens-logo"
                />
                <img
                  src={`${import.meta.env.BASE_URL}images/logo/new_logo.png`}
                  alt="RISSE Lab Logo"
                  className="footer-logo"
                />
              </div>
            </div>
          </div>

          {/* Copyright */}
          <div className="footer-bottom">
            <p>© 2025 RISSE Lab @ Stevens Institute of Technology</p>
          </div>
        </div>
      </footer>
    </div>
  );
};

export default Home;