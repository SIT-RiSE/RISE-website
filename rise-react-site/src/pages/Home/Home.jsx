import Banner from '../../components/Banner/Banner';
import './Home.css';

const Home = () => {
  const professor = {
    name: "Dr. Lu Xiao",
    title: "Associate Professor",
    image: `${import.meta.env.BASE_URL}images/people/lxiao6.webp`,
    bio: "Dr. Lu Xiao is an Associate Professor specializing in software engineering...",
  };

  const newsItems = [
    { date: "2023-05-01", content: "Our paper on AI-driven testing was accepted at ICSE 2023." },
    { date: "2023-04-15", content: "Dr. Lu Xiao received the NSF CAREER Award." },
  ];

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
          <h2 className="section-title">Recent News</h2>
          <div className="news-list">
            {newsItems.map((item, index) => (
              <div key={index} className="gradient-border">
                <div className="card-content">
                  <p className="news-date">{item.date}</p>
                  <p>{item.content}</p>
                </div>
              </div>
            ))}
          </div>
        </div>
      </section>

      {/* Open Positions Section */}
      <section className="section">
        <div className="container text-center">
          <h2 className="section-title">Open Positions</h2>
          <p className="section-subtitle">
            We are currently looking for students to join our research team.
          </p>
          <a href="/about" className="btn-primary">
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