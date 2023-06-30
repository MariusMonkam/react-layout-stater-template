from jinja2 import Template


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