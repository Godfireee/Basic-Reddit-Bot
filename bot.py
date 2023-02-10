import praw
import config
import re
import os
import csv

def login():
    r = praw.Reddit(username = config.username,
                password = config.password,
                client_id=config.client_id,
                client_secret=config.client_pass,
                user_agent="godfire's test script")
    return r

r = login()

def grab():
    subreddit = r.subreddit(input("Enter the subreddit: "))
    for submission in subreddit.hot(limit=10):
        print(submission.title)
        print(submission.score)
        print(submission.id)
        print(submission.url)
        print(submission.num_comments)
        print(submission.selftext)
        print(submission.created)

def reply():
    subreddit = r.subreddit(input("Enter the subreddit: "))
    keyword = input("Enter the keyword: ")
    reply = input("Enter the reply: ")
    if not os.path.isfile("posts_replied_to.txt"):
        posts_replied_to = []

    else:
        with open("posts_replied_to.txt", "r") as f:
            posts_replied_to = f.read()
            posts_replied_to = posts_replied_to.split("\n")
            posts_replied_to = list(filter(None, posts_replied_to))

    for submission in subreddit.hot(limit=10):
        if submission.id not in posts_replied_to:

            if re.search(keyword, submission.title, re.IGNORECASE):
                replied = submission.reply(reply)
                print("Bot replying to : ", submission.title)
                store_reply(submission.title, replied.id)
                posts_replied_to.append(submission.id)


    with open("posts_replied_to.txt", "w") as f:
        for post_id in posts_replied_to:
            f.write(post_id + "\n")

def store_reply(submission_title, reply_id):
    if not os.path.isfile("replies.csv"):
        with open("replies.csv", "w", newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(['Submission Title', 'Reply ID'])

    with open("replies.csv", "a", newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow([submission_title, reply_id])


