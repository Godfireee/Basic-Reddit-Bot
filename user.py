import bot

# This is the main function of the bot
def main():
    while True:
        print("1. Scrape details of a subreddit")
        print("2. Reply")
        print("3. Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            bot.grab()
        elif choice == "2":
            bot.reply()
        elif choice == "3":
            exit()
        else:
            print("Invalid choice, please try again")
            main()
main()
