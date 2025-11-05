import requests
import os
import apikeymain
import sys

# It's best practice to set this as an environment variable
# --- Configuration ---
# These are used when testing this file directly
NEWS_API_KEY = apikeymain.NEWS_API_KEY
TOPIC = apikeymain.TOPIC
ARTICLE_COUNT = apikeymain.ARTICLE_COUNT
DOMAINS_LIST = apikeymain.REPUTABLE_DOMAINS

# --- Function to Fetch News ---
def fetch_top_articles(api_key, domains_list, topic, count):
    """
    Fetches a specified number of top articles for a topic from NewsAPI.
    """
    # URL for the 'top-headlines' endpoint, sorted by relevance
    url = (f"https://newsapi.org/v2/everything?"
           f"q={topic}&"
           f"domains={domains_list}&"  # <-- ADDED THIS LINE
           f"sortBy=publishedAt&"
           f"pageSize={count}&"
           f"language=en&"
           f"apiKey={api_key}")
    
    try:
        response = requests.get(url)
        response.raise_for_status() # Raises an error for bad responses (4xx or 5xx)
        
        data = response.json()
        
        if data["status"] == "ok":
            print(f"Successfully fetched {len(data['articles'])} articles.")
            return data["articles"]
        else:
            print(f"Error from NewsAPI: {data.get('message')}")
            return []

    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: {e}")
        return []
    except KeyError:
        print("Error: 'articles' key not found in response. Check API key and query.")
        return []

# --- Test This Step ---
if __name__ == "__main__":
    print("--- Step 1: Fetching Articles ---")
    articles = fetch_top_articles(NEWS_API_KEY, TOPIC, ARTICLE_COUNT)
    
    if articles:
        for i, article in enumerate(articles):
            print(f"\nArticle {i+1}:")
            print(f"  Title: {article['title']}")
            print(f"  Source: {article['source']['name']}")
            print(f"  URL: {article['url']}")
            # The 'content' field is often just a snippet. 
            # We'll need the URL to scrape the full text in the next step.
            print(f"  Snippet: {article['description']}")
    else:
        print("No articles found or error occurred.")