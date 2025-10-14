from flask import Flask, render_template
import requests, json
# Create the Flask app


def get_meme():
    url = "https://meme-api.com/gimme"
    response = requests.request("GET", url)
    data = json.loads(response.text)
    meme_large = data["preview"][-2]
    subreddit = data["subreddit"]
    return meme_large, subreddit
    
app = Flask(__name__)

# Define a route
@app.route("/")
def index():
    meme_pic, subreddit = get_meme()
    return render_template("meme_index.html", meme_pic=meme_pic, subreddit=subreddit)

# Run the app
if __name__ == "__main__":
    app.run(port=8080)