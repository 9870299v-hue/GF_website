import os
from flask import Flask, render_template

app = Flask(__name__)

# Your data
data = {
    "title": "For My Favorite Person ❤️",
    "date_met": "Day One",
    "message": "Every moment with you has been special. Here is a little piece of our story!",
    "memories": [
        {"title": "The Beginning", "desc": "Where it all started."},
        {"title": "Unforgettable Moments", "desc": "Making memories that last forever."},
        {"title": "Looking Ahead", "desc": "Excited for everything yet to come."}
    ]
}

@app.route('/')
def home():
    return render_template('index.html', data=data)

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
