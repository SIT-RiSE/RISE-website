import './People.css';

const People = () => {
  const professors = [
    {
      name: "Lu Xiao",
      title: "Associate Professor",
      image: `${import.meta.env.BASE_URL}images/people/lxiao6.webp`,
      note: "",
      tag: "PI",
      url: "https://scholar.google.com/citations?user=YOUR_ID"
    }
  ];

  const students = [
    {
      name: "Chenhao Wei",
      title: "PhD Student",
      image: `${import.meta.env.BASE_URL}images/people/cwei7.webp`,
      note: "Research focus: Unit Testing Architecture",
      url: "https://scholar.google.com/citations?user=q6kIw60AAAAJ"
    },
    {
      name: "Gengwu Zhao",
      title: "PhD Student",
      image: `${import.meta.env.BASE_URL}images/people/gzhao.jpeg`,
      note: "Research focus: Unit Test Mocking",
      url: "https://scholar.google.com/citations?user=QFl5ZekAAAAJ"
    },
    {
      name: "Hanbin Qin",
      title: "PhD Student",
      image: `${import.meta.env.BASE_URL}images/people/hqin.jpeg`,
      note: "Research focus: Unit Test Mocking",
      url: "#"
    }
  ];

  const alumni = [
    {
      name: "Yutong Zhao",
      title: "PhD Graduate",
      image: `${import.meta.env.BASE_URL}images/people/yzhao.jpeg`,
      note: "Current position: Assistant Professor",
      tag: "Alumni",
      url: "https://scholar.google.com/citations?user=aMcoNgEAAAAJ"
    },
    {
      name: "Xiao Wang",
      title: "PhD Graduate",
      image: `${import.meta.env.BASE_URL}images/people/xwang.jpeg`,
      note: "Current position: SDE II at Amazon",
      tag: "Alumni",
      url: "https://scholar.google.com/citations?user=4fcRQJoAAAAJ"
    }
  ];

  const PersonCard = ({ person }) => (
    <a
      href={person.url}
      target={person.url !== '#' ? '_blank' : '_self'}
      rel="noopener noreferrer"
      className="person-card-link"
    >
      <div className="person-card">
        {person.tag && (
          <span className="person-tag">{person.tag}</span>
        )}
        <div className="person-image-container">
          <img
            src={person.image}
            alt={person.name}
            className="person-image"
            onError={(e) => {
              e.target.src = 'https://via.placeholder.com/200x200?text=' + person.name.split(' ').map(n => n[0]).join('');
            }}
          />
        </div>
        <div className="person-info">
          <h3 className="person-name">{person.name}</h3>
          <p className="person-title">{person.title}</p>
          {person.note && (
            <p className="person-note">{person.note}</p>
          )}
        </div>
      </div>
    </a>
  );

  const Section = ({ title, people }) => (
    <section className="people-section">
      <h2 className="section-title">{title}</h2>
      <div className="people-grid">
        {people.map((person, index) => (
          <PersonCard key={index} person={person} />
        ))}
      </div>
    </section>
  );

  return (
    <div className="people-page">
      <div className="container">
        <h1 className="page-title">Our Team</h1>
        <p className="page-subtitle">
          Meet the talented researchers and students who make up the RISE Lab
        </p>

        <Section title="Faculty" people={professors} />
        <Section title="PhD Students" people={students} />
        <Section title="Alumni" people={alumni} />
      </div>
    </div>
  );
};

export default People;