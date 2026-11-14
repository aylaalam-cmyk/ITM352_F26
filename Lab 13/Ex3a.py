import requests
from flask import Flask, render_template_string

app = Flask(__name__)

MEME_API_URL = "https://meme-api.com/gimme/wholesomememes"

PAGE = """
<!doctype html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>Wholesome Meme</title>
</head>
<head>
   <title>Memes'R'Us</title>
   <meta charset="UTF-8" name="viewport" content="width=device-width, initial-scale=0.8">
   <meta http-equiv="refresh" content="10; url=http://127.0.0.1:5000" />
</head>

<body>
    <h1>Wholesome Meme</h1>
    {% if meme_url %}
        <h2>{{ title }}</h2>
        <img src="{{ meme_url }}" alt="{{ title }}" style="max-width: 100%;">
        <p><a href="{{ url_for('home') }}">Get another meme</a></p>
    {% else %}
        <p>{{ error }}</p>
        <p><a href="{{ url_for('home') }}">Try again</a></p>
    {% endif %}
</body>
</html>
"""


@app.route("/")
def home():
    try:
        response = requests.request("GET", MEME_API_URL, timeout=10)
        response.raise_for_status()
        meme = response.json()
        if not isinstance(meme, dict):
            raise ValueError("The meme service returned an unexpected response.")

        meme_url = meme.get("url")
        if not isinstance(meme_url, str) or not meme_url:
            raise ValueError("The meme service did not return an image URL.")

        return render_template_string(
            PAGE,
            meme_url=meme_url,
            title=meme.get("title") or "Wholesome meme",
            error=None,
        )
    except (requests.RequestException, ValueError) as error:
        return render_template_string(
            PAGE,
            meme_url=None,
            title=None,
            error=f"Could not retrieve a meme: {error}",
        )


if __name__ == "__main__":
    app.run(debug=True)
