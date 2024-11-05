import feedparser
import ssl
import urllib.request

# URL for the Yankees' RSS feed from the Nitter instance
rss_url = "https://nitter.privacydev.net/Yankees/rss"

# Create an unverified SSL context
ssl_context = ssl._create_unverified_context()

# Fetch the RSS feed using urllib with the unverified SSL context
try:
    with urllib.request.urlopen(rss_url, context=ssl_context) as response:
        rss_data = response.read()
except Exception as e:
    print(f"Error fetching RSS feed: {e}")
    exit()

# Parse the fetched RSS feed using feedparser
feed = feedparser.parse(rss_data)

# Check if the feed was parsed successfully
if "bozo_exception" in feed:
    print(f"Error occurred: {feed.bozo_exception}")
else:
    # Print feed details to check if it was fetched correctly
    print(
        f"Feed title: {feed.feed.title if 'title' in feed.feed else 'No title found'}"
    )

# Check if the feed has entries
if len(feed.entries) == 0:
    print("No entries found in the feed.")
else:
    for entry in feed.entries:
        print(f"Title: {entry.title}")
        print(f"Link: {entry.link}")
        print(f"Published: {entry.published}")
        print(f"Summary: {entry.summary}")
        print("-" * 40)
