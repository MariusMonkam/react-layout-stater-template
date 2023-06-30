from jinja2 import Template


# Define the logo component template
logo_template = Template('''
<svg height="30" width="200">
  <text x="0" y="15" fill="red">I love SVG!</text>
</svg>
''')