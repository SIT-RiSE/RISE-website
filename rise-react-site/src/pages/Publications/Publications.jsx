import { useState, useEffect } from 'react';
import { FaFilePdf, FaGithub } from 'react-icons/fa';
import './Publications.css';

const Publications = () => {
  const [publications, setPublications] = useState([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    // Load publications from JSON file
    fetch(`${import.meta.env.BASE_URL}data/publications.json`)
      .then(response => response.json())
      .then(data => {
        setPublications(data);
        setLoading(false);
      })
      .catch(error => {
        console.error('Error loading publications:', error);
        setLoading(false);
        // Fallback data
        setPublications([
          {
            title: "How Do Developers Structure Unit Test Cases? An Empirical Study from the \"AAA\" Perspective",
            authors: "Chenhao Wei, Lu Xiao, Tingting Yu, Sunny Wong, Abigail Clune",
            year: "2024",
            venue: "arXiv preprint",
            paper_url: "https://arxiv.org/abs/2407.08138",
            github_url: "https://github.com/Codegass/Unit-Test-Empricial-Study-from-AAA-Perspective",
          }
        ]);
      });
  }, []);

  const PublicationItem = ({ pub }) => (
    <div className="gradient-border">
      <div className="card-content">
        <p className="publication-authors">{pub.authors}</p>
        <h3 className="publication-title">{pub.title}</h3>
        <div className="publication-meta">
          {pub.venue && (
            <span className="publication-venue">{pub.venue}</span>
          )}
          <span className="publication-year">{pub.year}</span>
        </div>
        <div className="publication-links">
          {pub.paper_url && (
            <a
              href={pub.paper_url}
              target="_blank"
              rel="noopener noreferrer"
              className="publication-link paper-link"
            >
              <FaFilePdf /> Paper
            </a>
          )}
          {pub.github_url && (
            <a
              href={pub.github_url}
              target="_blank"
              rel="noopener noreferrer"
              className="publication-link github-link"
            >
              <FaGithub /> Code
            </a>
          )}
        </div>
      </div>
    </div>
  );

  if (loading) {
    return (
      <div className="publications-page">
        <div className="container">
          <h1 className="page-title">Publications</h1>
          <div className="loading">Loading publications...</div>
        </div>
      </div>
    );
  }

  return (
    <div className="publications-page">
      <div className="container">
        <h1 className="page-title">Publications</h1>

        <div className="publications-list">
          {publications.length > 0 ? (
            publications.map((pub, index) => (
              <PublicationItem key={index} pub={pub} />
            ))
          ) : (
            <p className="no-publications">No publications available at the moment.</p>
          )}
        </div>
      </div>
    </div>
  );
};

export default Publications;