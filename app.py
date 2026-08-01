from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    data = {
        "title": "Happy Girlfriend's Day, Baby! ❤️",
        "subtitle": "Forever & Always",
        "intro": "I wanted to give you a small piece of my heart on our special day. Here is a little letter for you...",
        "cards": [
            {
                "title": "To My Whole World 🌹",
                "text": "Happy Girlfriends Day, baby! I’m just completely overwhelmed by everything today... I honestly don’t think I could ever put into words how much you truly mean to me. I love everything about who you are and everything about who we are together. You are truly the bestest girlfriend in the entire world!"
            },
            {
                "title": "Where It All Began 🗓️",
                "text": "I still catch myself thinking about how I never imagined you’d become mine, but I remember the exact moment we met, and that unforgettable night you officially became my girlfriend on 20/03/2026—literally the best day of my life."
            },
            {
                "title": "Standing Solid Together 💫",
                "text": "Our journey from that night to where we are now wasn't always easy, but we stayed solid through every single second, and that means everything to me. I pray we stay like this forever and never, ever give up on each other (we won't right, baccha? 😉)."
            },
            {
                "title": "Our Future Together 💍",
                "text": "We are going to marry each other no matter what hardships come our way, and we’ll conquer every single one of them together. I love you so much, and I always will, babyyy! ❤️"
            }
        ]
    }
    return render_template('index.html', data=data)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
    
