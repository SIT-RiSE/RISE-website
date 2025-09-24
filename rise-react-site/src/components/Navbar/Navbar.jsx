import { Link, useLocation } from 'react-router-dom';
import './Navbar.css';

const Navbar = () => {
  const location = useLocation();

  return (
    <nav className="navbar">
      <div className="navbar-content">
        <Link to="/" className="navbar-brand">
          RISSE Lab
        </Link>
        <div className="navbar-spacer" />
        <div className="navbar-links">
          <Link to="/" className="navbar-link">
            Home
          </Link>
          <Link to="/research" className="navbar-link">
            Research
          </Link>
          <Link to="/publications" className="navbar-link">
            Publications
          </Link>
          <Link to="/people" className="navbar-link">
            People
          </Link>
          <Link to="/about" className="navbar-link">
            About
          </Link>
        </div>
      </div>
    </nav>
  );
};

export default Navbar;