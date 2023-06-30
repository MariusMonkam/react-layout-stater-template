from jinja2 import Template

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