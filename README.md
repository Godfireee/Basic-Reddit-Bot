
# Python Reddit Bot

This is a simple Reddit bot written in Python using the PRAW (Python Reddit API Wrapper) library. It allows you to scrape details of a subreddit and reply to a post.

**Requirements**
Python 3
PRAW library
Reddit account

**Configuration**
Before running the bot, you need to configure the config.py file with your Reddit account credentials and API keys. Replace them with your actual values.

To run the bot, simply run the user.py file

## Getting Reddit API Secret ID and Client ID

To get the Reddit API secret id and client id, follow these steps:

1. Go to the Reddit Developer Portal by following this link: [https://www.reddit.com/prefs/apps](https://www.reddit.com/prefs/apps)
2. Sign in to your Reddit account.
3. Click on the "Create App" or "Create Another App" button.
4. Fill in the details for your Reddit app, such as its name, description, and the type of app you are creating.
5. Once you have created the app, you will be provided with a client ID and secret key that you can use in your code.

**Note**: It is important to keep your secret id and client id secure and not to share it with anyone. You can use the `getpass` library to hide the password while taking it as input from the user in your code.
