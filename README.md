# RISE Lab Website
This repository contains the source code for the Research in Software Engineering (RISE) Lab website at Stevens Institute of Technology.


## Overview

The RISE Lab website is built using Reflex, a Python framework for building web applications. It showcases the lab's research, publications, team members, and other relevant information.


## Features

- **Home Page**: Provides an overview of the lab and its mission.
- **Research Page**: Highlights the lab's research interests and ongoing projects.
- **People Page**: Introduces the lab members, including current students, alumni, and faculty.
- **Publications Page**: Displays the lab's publications with details such as authors, publication venue, year, and links to papers and code.
- **About Page**: Provides information about the lab's history, facilities, and collaborations.

## Getting Started

To run the website locally, follow these steps:

1. Clone the repository:

2. Install dependencies:
```
pip install -r requirements.txt
```

3. Run the development server:
```
reflex run
```

## Project Structure

* RISE_website/: Main application directory
    * pages/: Individual page components
        * index.py: Home page
        * about.py: About page
        * research.py: Research areas page
        * publications.py: Publications list page
        * people.py: Team members showcase page
    * components/: Reusable components (navbar, footer, etc.)
    * styles/: CSS styles
    * RISE_website.py: Main application file
* assets/: Static assets (images, scripts, etc.)
        * scripts/: Utility scripts (e.g., for fetching data)
* rxconfig.py: Reflex configuration file

## Contributing

We welcome contributions to the RISE Lab website! If you have suggestions or improvements, please open an issue or submit a pull request.

