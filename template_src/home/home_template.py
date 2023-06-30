from jinja2 import Template

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
