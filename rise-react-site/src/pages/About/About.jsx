import { FaMapMarkerAlt, FaEnvelope, FaUniversity } from 'react-icons/fa';
import './About.css';

const About = () => {
  return (
    <div className="about-page">
      <div className="container">
        <h1 className="page-title">About RISE Lab</h1>

        <section className="about-intro">
          <p>
            The Research in Software Engineering (RISE) Lab at Stevens Institute of Technology
            is dedicated to advancing the field of software engineering through innovative research
            and education. Founded by Dr. Lu Xiao, our lab focuses on developing cutting-edge
            solutions to modern software development challenges.
          </p>
        </section>

        <section className="about-mission">
          <h2>Our Mission</h2>
          <div className="mission-cards">
            <div className="mission-card">
              <h3>Research Excellence</h3>
              <p>
                Conduct pioneering research in software engineering that addresses real-world
                challenges and advances the state of the art.
              </p>
            </div>
            <div className="mission-card">
              <h3>Education & Training</h3>
              <p>
                Train the next generation of software engineers and researchers through
                hands-on research experiences and mentorship.
              </p>
            </div>
            <div className="mission-card">
              <h3>Industry Collaboration</h3>
              <p>
                Partner with industry leaders to ensure our research has practical impact
                and addresses current industry needs.
              </p>
            </div>
          </div>
        </section>

        {/* <section className="about-facilities">
          <h2>Facilities & Resources</h2>
          <p>
            Our lab is equipped with state-of-the-art computing resources, including high-performance
            servers for large-scale software analysis, dedicated workstations for research, and
            collaborative spaces for team discussions and brainstorming sessions.
          </p>
        </section> */}

        <section className="about-join">
          <h2>Join Our Team</h2>
          <p>
            We are always looking for talented and motivated individuals to join our research team.
            If you are interested in pursuing a PhD in Software Engineering or collaborating on
            research projects, we encourage you to reach out.
          </p>
          <div className="join-requirements">
            <h3>What We Look For:</h3>
            <ul>
              <li>Strong background in Computer Science or Software Engineering</li>
              <li>Passion for research and problem-solving</li>
              <li>Excellent programming skills</li>
              <li>Good communication and teamwork abilities</li>
              <li>Self-motivation and dedication to excellence</li>
            </ul>
          </div>
        </section>

        <section className="about-contact">
          <h2>Contact Us</h2>
          <div className="contact-info">
            <div className="contact-item">
              <FaUniversity className="contact-icon" />
              <div>
                <h3>Institution</h3>
                <p>Stevens Institute of Technology</p>
                <p>School of Systems and Enterprises</p>
              </div>
            </div>
            <div className="contact-item">
              <FaMapMarkerAlt className="contact-icon" />
              <div>
                <h3>Address</h3>
                <p>1 Castle Point Terrace</p>
                <p>Hoboken, NJ 07030</p>
              </div>
            </div>
            <div className="contact-item">
              <FaEnvelope className="contact-icon" />
              <div>
                <h3>Email</h3>
                <p>lxiao@stevens.edu</p>
              </div>
            </div>
          </div>
        </section>
      </div>
    </div>
  );
};

export default About;