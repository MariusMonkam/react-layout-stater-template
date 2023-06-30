from jinja2 import Template


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