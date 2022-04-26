import os

token = os.environ['TOKEN']
channel_id = os.environ['CHANNEL_ID']

user_agent = os.environ['USER_AGENT']

login_data = {
    'customer[email]': os.environ['EMAIL'],
    'customer[password]': os.environ['PASSWORD']
}

