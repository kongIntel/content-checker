thonimport smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

class EmailSender:
    def __init__(self, email_config):
        self.email_config = email_config

    def send_email(self, content, previous_content, screenshot_url):
        msg = MIMEMultipart()
        msg['From'] = self.email_config['from_email']
        msg['To'] = self.email_config['to_email']
        msg['Subject'] = 'Content Change Detected'
        
        body = f"""
        Content has changed!

        Previous Content:
        {previous_content}

        New Content:
        {content}

        Screenshot:
        {screenshot_url}
        """
        msg.attach(MIMEText(body, 'plain'))

        with smtplib.SMTP(self.email_config['smtp_server'], self.email_config['smtp_port']) as server:
            server.starttls()
            server.login(self.email_config['from_email'], self.email_config['password'])
            text = msg.as_string()
            server.sendmail(self.email_config['from_email'], self.email_config['to_email'], text)