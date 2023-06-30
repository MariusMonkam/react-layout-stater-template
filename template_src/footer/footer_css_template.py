from jinja2 import Template

# Define the CSS file for the Footer component
footer_css_template = Template('''
.footer {
    background-color: #f1f1f1;
    padding: 20px;
    text-align: center;
}

@media only screen and (max-width: 600px) {
    .footer {
        background-color: #f1f1f1;
        padding: 10px;
    }
}
''')