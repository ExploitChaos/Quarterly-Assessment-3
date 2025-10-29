"""
newsapi.py
This file uses the SendGrid API to send the newsletter.
This is more reliable than using Gmail's SMTP.

Remember to install the library:
pip install sendgrid
"""

from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail
import apikeymain
import os

# --- Configuration ---
SENDER_EMAIL = apikeymain.SENDER_EMAIL
RECIPIENT_EMAIL = apikeymain.RECIPIENT_EMAIL
SENDGRID_API_KEY = apikeymain.SENDGRID_API_KEY

def send_newsletter_email(recipient, email_content_html):
    """
    Sends an HTML-formatted email using the SendGrid API.
    """
    if not SENDGRID_API_KEY or "YOUR_SENDGRID_API_KEY_HERE" in SENDGRID_API_KEY:
        print("Error: SENDGRID_API_KEY not set in apikeymain.py")
        print("Please add your SendGrid API key to apikeymain.py to send emails.")
        return

    # Create the email message object
    message = Mail(
        from_email=SENDER_EMAIL,
        to_emails=recipient,
        subject="Your AI-Powered News Newsletter",
        html_content=email_content_html
    )

    try:
        # Initialize the SendGrid client
        sg = SendGridAPIClient(SENDGRID_API_KEY)
        
        # Send the email
        print("Connecting to SendGrid API...")
        response = sg.send(message)
        
        print(f"Email sent successfully! (Status code: {response.status_code})")
        
    except Exception as e:
        print(f"Error: Unable to send email. {e}")
        if hasattr(e, 'body'):
            print(f"Error details: {e.body}")

# --- Test This Step ---
if __name__ == "__main__":
    print("\n--- Step 3: Sending Email (with SendGrid) ---")
    
    test_html = """
    <html>
      <body>
        <h2>Hello from SendGrid!</h2>
        <p>This is a test email from your Python script.</p>
        <p>If you see this, your SendGrid integration is working.</p>
      </body>
    </html>
    """
    
    print(f"Attempting to send a test email to {RECIPIENT_EMAIL}...")
    
    # Uncomment the line below to send a real test email
    # Make sure your credentials are set in apikeymain.py first
    
    # send_newsletter_email(RECIPIENT_EMAIL, test_html)
    
    print("\nTest complete.")
    print("To send a real test, uncomment the 'send_newsletter_email' line inside this file.")
