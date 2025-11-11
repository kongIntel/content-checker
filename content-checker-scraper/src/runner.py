thonimport time
import json
from extractors.content_extractor import ContentExtractor
from notifications.email_sender import EmailSender

def load_config():
    with open('src/config/settings.json') as f:
        return json.load(f)

def monitor_changes():
    config = load_config()
    extractor = ContentExtractor(config['url'], config['selector'])
    email_sender = EmailSender(config['email'])

    while True:
        content = extractor.get_content()
        previous_content = extractor.get_previous_content()
        
        if content != previous_content:
            screenshot_url = extractor.take_screenshot()
            email_sender.send_email(content, previous_content, screenshot_url)
            extractor.save_content(content)
        
        time.sleep(config['interval'])

if __name__ == '__main__':
    monitor_changes()