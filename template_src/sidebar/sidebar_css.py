from jinja2 import Template

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