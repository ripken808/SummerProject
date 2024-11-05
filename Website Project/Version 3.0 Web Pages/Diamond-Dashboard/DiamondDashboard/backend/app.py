from fastapi import FastAPI, HTTPException, Query
import feedparser
import ssl
import urllib.request
import os
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv
import requests

# Load environment variables from .env file
load_dotenv()

app = FastAPI()

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# OpenWeather API key
WEATHER_API_KEY = os.getenv("OPENWEATHER_API_KEY")


# Function to fetch and parse the RSS feed for tweets
def fetch_tweets():
    rss_url = "https://nitter.privacydev.net/Yankees/rss"
    ssl_context = ssl._create_unverified_context()  # Create an unverified SSL context

    try:
        with urllib.request.urlopen(rss_url, context=ssl_context) as response:
            rss_data = response.read()
    except Exception as e:
        return {"error": f"Error fetching RSS feed: {e}"}

    # Parse the RSS feed
    feed = feedparser.parse(rss_data)
    if "bozo_exception" in feed:
        return {"error": f"Error occurred: {feed.bozo_exception}"}

    # Extract and format the tweet data
    tweets = []
    for entry in feed.entries:
        tweet = {
            "title": entry.title,
            "summary": entry.summary,
        }
        tweets.append(tweet)

    return tweets


# Route to get the latest tweets
@app.get("/api/team/Yankees")
def get_latest_tweets():
    tweets = fetch_tweets()
    if "error" in tweets:
        raise HTTPException(status_code=500, detail=tweets["error"])
    return tweets


# Route to get current weather data based on latitude and longitude
@app.get("/api/weather")
def get_weather(lat: float = Query(...), lon: float = Query(...)):
    url = f"http://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={WEATHER_API_KEY}&units=imperial"

    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an error for bad status codes
        weather_data = response.json()
    except requests.RequestException as e:
        raise HTTPException(
            status_code=500, detail=f"Error fetching weather data: {str(e)}"
        )

    return {
        "temperature": weather_data["main"]["temp"],
        "weather": weather_data["weather"][0]["description"],
        "city": weather_data["name"],
    }
