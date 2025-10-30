# Quarterly-Assessment-3

AI-Powered News Newsletter Generator

A Python application that automates the creation and delivery of a personalized news newsletter. This script fetches the latest articles on a specific topic, uses an LLM to scrape and summarize them, and emails the compiled digest to a recipient list.

Project Overview

This project solves the problem of staying up-to-date on specific topics by automating the entire news-gathering process. It's built in three modular stages, as recommended by the project assignment:

Fetch: Grabs the latest headlines and URLs from the NewsAPI.

Summarize: Uses BeautifulSoup to scrape the full text of each article and then leverages the OpenAI API (GPT-3.5-Turbo) to generate a concise summary.

Deliver: Formats the summaries into a clean HTML email and sends it via the SendGrid API.

Features

Modular Design: Each core step (fetch, summarize, send) is contained in its own Python file for easy testing and debugging.

Config-Driven: All API keys, topics, and email addresses are stored in a central apikeymain.py file, so no credentials are hard-coded.

Web Scraping: Intelligently scrapes article content from URLs, bypassing simple "description" snippets for higher-quality summaries.

AI Summarization: Uses gpt-3.5-turbo for high-quality, email-friendly summaries of long articles.

HTML Formatting: Generates a clean, readable HTML email with styled headlines, links, and source attribution.

Robust Error Handling: Includes try...except blocks for API-level errors, request failures, and scraping issues.

Project Structure

The application is broken down into the following key files:

.
├── main.py               # The main executable script that runs the entire pipeline
├── fetch_news.py         # (Step 1) Fetches articles from NewsAPI
├── step2_summarize.py    # (Step 2) Scrapes URLs and summarizes text with OpenAI
├── newsapi.py            # (Step 3) Sends the final email using SendGrid
├── apikeymain.py         # Configuration file for API keys, topic, and emails
└── requirements.txt      # List of all Python dependencies


Note: The file newsapi.py contains the SendGrid (email) logic, not the NewsAPI (fetching) logic.

Setup and Installation

Follow these steps to get the project running on your local machine.

1. Clone the Repository

git clone [https://your-repository-url.git](https://your-repository-url.git)
cd ai-powered-newsletter


2. Install Dependencies

It's highly recommended to use a Python virtual environment.

# Create a virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install the required packages
pip install -r requirements.txt


(You will need to create a requirements.txt file with the following content):

# requirements.txt
requests
openai
sendgrid
beautifulsoup4


3. Configure API Keys

Create a file named apikeymain.py in the root of the project and add the following content. This file is required for the application to run.

# apikeymain.py

# Step 1: NewsAPI Key ([https://newsapi.org/](https://newsapi.org/))
NEWS_API_KEY = "YOUR_NEWSAPI_KEY_HERE"

# Step 2: OpenAI API Key ([https://platform.openai.com/account/api-keys](https://platform.openai.com/account/api-keys))
OPENAI_API_KEY = "YOUR_OPENAI_API_KEY_HERE"

# Step 3: SendGrid API Key ([https://app.sendgrid.com/settings/api_keys](https://app.sendgrid.com/settings/api_keys))
SENDGRID_API_KEY = "YOUR_SENDGRID_API_KEY_HERE"
SENDER_EMAIL = "your-verified-sender-email@example.com"
RECIPIENT_EMAIL = "recipient-email@example.com"

# Project Settings
TOPIC = "artificial intelligence"
ARTICLE_COUNT = 5


How to Use

You can either run the entire pipeline at once or test each module individually.

Running a Single Test

This is useful for debugging one part of the process.

# Test Step 1: Fetching articles
python fetch_news.py

# Test Step 2: Scraping and summarizing a test URL
python step2_summarize.py

# Test Step 3: Sending a test email (uncomment the send line in the file)
python newsapi.py


Running the Full Application

This will execute the entire process from fetching to sending the final email.

python main.py


The script will output its progress to the console, and the recipient email should receive the newsletter shortly.

Automation (Optional)

To fully automate this script as the assignment suggests, you can schedule it to run daily.

On macOS/Linux (using cron)

Open your crontab editor: crontab -e

Add the following line to run the script every day at 8:00 AM. (Make sure to use the absolute paths to your Python executable and main.py script).

# Run the AI newsletter script every day at 8:00 AM
0 8 * * * /path/to/your/venv/bin/python /path/to/your/project/main.py


On Windows (using Task Scheduler)

Open Task Scheduler.

Click Create Basic Task...

Name it "AI Newsletter" and set the Trigger to "Daily" at your desired time (e.g., 8:00:00 AM).

For the Action, select "Start a program".

In "Program/script", browse to the absolute path of your python.exe (e.g., C:\path\to\project\venv\Scripts\python.exe).

In "Add arguments (optional)", put the absolute path to your script (e.g., C:\path\to\project\main.py).

Click Finish.