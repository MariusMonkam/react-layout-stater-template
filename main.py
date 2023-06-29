import os
import subprocess
from jinja2 import Template
import warnings



import os

import os

# Prompt the user to enter the project name and path
project_name = input("Enter the name of the React project: ")
project_path = input("Enter the desired path for the project (leave blank for the current directory): ")

# If no project path is provided, use the current directory as the default
if not project_path:
    project_path = os.getcwd()

# Check if the generator is located within the 'node_modules' directory
if 'node_modules' in os.getcwd().split(os.sep):
    # Move up one level to the parent directory
    project_path = os.path.abspath(os.path.join(os.getcwd(), os.pardir))

# Create the full path to the project directory
project_dir = os.path.join(project_path, project_name)

# Create the project directory if it doesn't exist
if not os.path.exists(project_dir):
    os.makedirs(project_dir)

# Change the current working directory to the project directory
os.chdir(project_dir)




# Run the create-react-app command to create a new React project
subprocess.call(['npx', 'create-react-app', '.'], shell=True)

# Define the directory path for the components
component_dir = './src/components'

# Create the components directory if it doesn't exist
if not os.path.exists(component_dir):
    os.makedirs(component_dir)

# Define the logo component template
logo_template = Template('''
<svg height="30" width="200">
  <text x="0" y="15" fill="red">I love SVG!</text>
</svg>
''')

# Define the navbar component template
navbar_template = Template('''
<nav class="navbar">
  <div class="navbar__logo">
    $logo
  </div>
  <ul class="navbar__list">
    <li><a href="#">Home</a></li>
    <li><a href="#">About</a></li>
    <li><a href="#">Contact</a></li>
  </ul>
</nav>
''')

# Define the Header component template
header_template = Template('''
import React from 'react';
import './Header.css';

function Header({logo,navbar}) {
  return (
    <header>
      <div class="logo">
        ${logo}
      </div>
      ${navbar}
    </header>
  );
}

export default Header;
''')

# Define the CSS file for the Header component
header_css_template = Template('''
header {
  display: flex;
  flex-direction: row;
  justify-content: space-between;
  align-items: center;
  padding: 10px;
  background-color: #f1f1f1;
}

nav {
  display: flex;
  flex-direction: row;
  align-items: center;
}

nav ul {
  list-style: none;
  margin: 0;
  padding: 0;
  display: flex;
  flex-direction: row;
  align-items: center;
}

nav ul li {
  margin-left: 20px;
}

@media only screen and (max-width: 768px) {
  header {
    flex-direction: column;
    align-items: stretch;
  }

  nav {
    margin-top: 10px;
    order: 2;
  }

  nav ul {
    flex-direction: column;
    align-items: stretch;
  }

  nav ul li {
    margin: 0;
    padding: 10px 0;
    border-top: 1px solid #ccc;
  }
}
''')

# Generate the CSS file for the Header component
with open(os.path.join(component_dir, 'Header.css'), 'w') as f:
    f.write(header_css_template.render())

# Define the default logo properties
default_logo_src = 'https://via.placeholder.com/150x50.png?text=Logo'
default_logo_height = '50'
default_logo_width = '150'

# render logo component
logo_component = logo_template.render(logo_text='My Logo')
with open(os.path.join(component_dir, 'logo.svg'), 'w') as f:
    f.write(logo_component)

# render navbar component
navbar_component = navbar_template.render()
with open(os.path.join(component_dir, 'Navbar.js'), 'w') as f:
    f.write(navbar_component)


# render header component with logo and navbar
header_component = header_template.render(logo=logo_component, navbar=navbar_component)
with open(os.path.join(component_dir, 'Header.js'), 'w') as f:
    f.write(header_component)

# Define the template for the Sidebar component
sidebar_template = Template('''
import React from 'react';
import './Sidebar.css';

function Sidebar() {
  return (
    <div className="sidebar">
      <h1>Sidebar Component</h1>
    </div>
  );
}

export default Sidebar;
''')

# Generate the Sidebar component
with open(os.path.join(component_dir, 'Sidebar.js'), 'w') as f:
    f.write(sidebar_template.render())

# Define the CSS file for the Sidebar component
sidebar_css = '''
.sidebar {
  background-color: #f1f1f1;
  padding: 20px;
  float: left;
  width: 25%;
}

@media screen and (max-width: 768px) {
  .sidebar {
    width: 100%;
    float: none;
  }
}
'''

# Generate the Sidebar CSS file
with open(os.path.join(component_dir, 'Sidebar.css'), 'w') as f:
    f.write(sidebar_css)

# Define the template for the Footer component
footer_template = Template('''
import React from 'react';
import './Footer.css';

function Footer() {
  return (
    <div className="footer">
      <h1>Footer Component</h1>
    </div>
  );
}

export default Footer;
''')

# Generate the Home component
home_template = Template('''
import React from 'react';
import '../components/Home.css';

function Home() {
  return (
    <div className="home">
      <h1>Welcome to the Home Page</h1>
    </div>
  );
}

export default Home;
''')

with open(os.path.join(component_dir, 'Home.js'), 'w') as f:
    f.write(home_template.render())

# Define the CSS file for the Home component
home_css_template = Template('''
.home {
  background-color: #f1f1f1;
  padding: 20px;
  text-align: center;
}

@media only screen and (max-width: 600px) {
  .home {
    background-color: #f1f1f1;
    padding: 10px;
  }
}
''')

with open(os.path.join(component_dir, 'Home.css'), 'w') as f:
    f.write(home_css_template.render())

# Generate the Footer component
with open(os.path.join(component_dir, 'Footer.js'), 'w') as f:
    f.write(footer_template.render())

# Define the CSS file for the Footer component
footer_css_template = Template('''
.footer {
    background-color: #f1f1f1;
    padding: 20px;
    text-align: center;
}

@media only screen and (max-width: 600px) {
    .footer {
        background-color: #f1f1f1;
        padding: 10px;
    }
}
''')

# Generate the CSS file for the Footer component
with open(os.path.join(component_dir, 'Footer.css'), 'w') as f:
    f.write(footer_css_template.render())

# Define the path to the App.js file
app_file = './src/App.js'

# Define the template for the App.js file
app_template = Template('''
import React from 'react';
import Header from './components/Header';
import Sidebar from './components/Sidebar';
import Home from './components/Home';
import Footer from './components/Footer';

import './components/Header.css';
import './components/Sidebar.css';
import './components/Home.css';
import './components/Footer.css';

function App() {
    return (
        <div className="App">
            <Header />
            <Sidebar />
             <Home />
            <Footer />
        </div>
    );
}

export default App;
''')

# Replace the contents of the App.js file with the template
with open(app_file, 'w') as f:
    f.write(app_template.render())

# Run the npm command to start the development server
subprocess.call(['npm', 'start'], shell=True)
