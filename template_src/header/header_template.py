from jinja2 import Template

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
