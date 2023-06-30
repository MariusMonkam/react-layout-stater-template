from jinja2 import Template

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