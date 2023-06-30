import os
import subprocess

from template_src.utils.utils import component_dir,default_logo_height,default_logo_src,default_logo_width,app_file


from template_src.logo.logo_template import logo_template

from template_src.navbar.navbar_template import navbar_template

from template_src.header.header_css_template import header_css_template
from template_src.header.header_template import header_template

from template_src.sidebar.sidebar_template import sidebar_template
from template_src.sidebar.sidebar_css import sidebar_css

from template_src.footer.footer_template import footer_template
from template_src.footer.footer_css_template import footer_css_template

from template_src.home.home_css_template import home_css_template
from template_src.home.home_template import home_template

from template_src.app.app_template import app_template

import warnings

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

# Create the components directory if it doesn't exist
if not os.path.exists(component_dir):
    os.makedirs(component_dir)

# Generate the CSS file for the Header component
with open(os.path.join(component_dir, 'Header.css'), 'w') as f:
    f.write(header_css_template.render())


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

# Generate the Sidebar component
with open(os.path.join(component_dir, 'Sidebar.js'), 'w') as f:
    f.write(sidebar_template.render())

# Generate the Sidebar CSS file
with open(os.path.join(component_dir, 'Sidebar.css'), 'w') as f:
    f.write(sidebar_css)

with open(os.path.join(component_dir, 'Home.js'), 'w') as f:
    f.write(home_template.render())

with open(os.path.join(component_dir, 'Home.css'), 'w') as f:
    f.write(home_css_template.render())

# Generate the Footer component
with open(os.path.join(component_dir, 'Footer.js'), 'w') as f:
    f.write(footer_template.render())

# Generate the CSS file for the Footer component
with open(os.path.join(component_dir, 'Footer.css'), 'w') as f:
    f.write(footer_css_template.render())

# Replace the contents of the App.js file with the template
with open(app_file, 'w') as f:
    f.write(app_template.render())

# Run the npm command to start the development server
subprocess.call(['npm', 'start'], shell=True)
