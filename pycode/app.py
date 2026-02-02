import os
from flask import Flask, render_template

# Reconfigure paths to look up one level from 'pycode'
app = Flask(__name__, 
            template_folder=os.path.join('..', 'templates'),
            static_folder=os.path.join('..', 'static'))

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run()
