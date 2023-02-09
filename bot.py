import praw
import config

def login():
    praw.Reddit(username = config.username,
                password = config.password,
                client_id=config.client_id,
                client_secret=config.client_pass,
                user_agent="godfire's test script")
login()