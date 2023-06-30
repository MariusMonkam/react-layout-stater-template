from jinja2 import Template

# Define the template for the App.js file
app_template = Template('''
import React from 'react';
import Header from './components/Header';
import Sidebar from './components/Sidebar';
import Home from './components/Home';
import Footer from './components/Footer';

import './components/Header.css';
import './components/Sidebar.css';
import './components/Home.css';
import './components/Footer.css';

function App() {
    return (
        <div className="App">
            <Header />
            <Sidebar />
             <Home />
            <Footer />
        </div>
    );
}

export default App;
''')