import './Research.css';

const Research = () => {
  const researchAreas = [
    {
      title: "Software Engineering Processes",
      description: "We investigate agile methodologies, DevOps practices, and continuous integration/continuous deployment (CI/CD) pipelines to improve software development efficiency and quality."
    },
    {
      title: "Software Architecture and Design",
      description: "Our team explores microservices architecture, cloud-native application design, and software design patterns to create scalable and maintainable systems."
    },
    {
      title: "AI in Software Engineering",
      description: "We research the application of machine learning and artificial intelligence techniques in code generation, bug prediction, and automated testing to enhance developer productivity."
    }
  ];

  return (
    <div className="research-page">
      <div className="container">
        <h1 className="page-title">Our Research</h1>
        <p className="page-subtitle">
          At RISSE Lab, we conduct cutting-edge research in various areas of software engineering,
          focusing on both theoretical foundations and practical applications.
        </p>

        <div className="research-areas">
          {researchAreas.map((area, index) => (
            <div key={index} className="gradient-border">
              <div className="card-content">
                <h3 className="research-title">{area.title}</h3>
                <p className="research-description">{area.description}</p>
              </div>
            </div>
          ))}
        </div>
      </div>

      {/* Footer */}
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

export default Research;