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
    </div>
  );
};

export default Research;