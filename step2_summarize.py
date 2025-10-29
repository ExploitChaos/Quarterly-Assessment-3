"""
step2_summarize.py
This file contains the functions for:
1. Scraping the full text of an article from its URL.
2. Summarizing that text using the OpenAI LLM.
"""

from openai import OpenAI
import requests
from bs4 import BeautifulSoup
import apikeymain
import os

# --- Configuration ---
# Set up the OpenAI client
try:
    client = OpenAI(api_key=apikeymain.OPENAI_API_KEY)
except Exception as e:
    print(f"Error initializing OpenAI client: {e}")
    print("Make sure your OPENAI_API_KEY is correct in apikeymain.py")
    client = None

# --- Function to Scrape Article Text ---
def get_article_text(url):
    """
    Fetches and extracts the main text content from a news article URL.
    """
    try:
        # Some sites block default 'requests' user-agents
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        }
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()
        
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # Find all paragraph <p> tags
        # This is a generic scraper and may not work for all sites.
        paragraphs = soup.find_all('p')
        
        article_text = ' '.join([p.get_text() for p in paragraphs])
        
        if not article_text:
            print(f"  Warning: Could not find <p> tags at {url}. Scraping may have failed.")
            return None

        # Limit text to a reasonable amount to avoid huge API costs
        return article_text[:15000] 
    
    except requests.exceptions.RequestException as e:
        print(f"  Error scraping {url}: {e}")
        return None

# --- Function to Summarize Text ---
def summarize_text_with_llm(text):
    """
    Uses OpenAI's gpt-3.5-turbo to summarize a block of text.
    """
    if not text:
        return "Error: No text provided to summarize."
    
    if not client:
        return "Error: OpenAI client not initialized."
        
    try:
        # Truncate to fit model context limit (approx 4096 tokens for gpt-3.5)
        # 1 token ~= 4 chars, so 15000 chars is safe
        truncated_text = text[:15000]

        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful assistant. Summarize the following news article into a concise, email-friendly paragraph (3-4 sentences)."},
                {"role": "user", "content": truncated_text}
            ]
        )
        summary = response.choices[0].message.content
        return summary
    except Exception as e:
        print(f"  Error summarizing text: {e}")
        return "Error: Could not generate summary."

# --- Test This Step ---
if __name__ == "__main__":
    print("\n--- Step 2: Scraping and Summarizing Test ---")
    
    TEST_URL = "https://www.theverge.com/2023/11/21/23970227/openai-scared-me-sam-altman-fired-q-star" # Example
    
    print(f"Testing with URL: {TEST_URL}")
    article_content = get_article_text(TEST_URL)
    
    if article_content:
        print(f"\nSuccessfully scraped text (first 200 chars):")
        print(article_content[:200] + "...")
        
        summary = summarize_text_with_llm(article_content)
        print("\n--- SUMMARY ---")
        print(summary)
    else:
        print(f"Could not scrape text from {TEST_URL}.")