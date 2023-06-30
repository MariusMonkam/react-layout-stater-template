from jinja2 import Template
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