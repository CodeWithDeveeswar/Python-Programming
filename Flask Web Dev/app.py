# Import Flask class and render_template function
from flask import Flask, render_template

# Create Flask application object
app = Flask(__name__)

# Route for Home page (URL: /)
@app.route('/')
def home():
    # Render index.html from templates folder
    return render_template("index.html")

# Route for About page (URL: /about)
@app.route('/about')
def about():
    # Render about.html from templates folder
    return render_template("about.html")

# Run the Flask app
if __name__ == '__main__':
    # debug=True enables auto reload and error messages
    app.run(debug=True)