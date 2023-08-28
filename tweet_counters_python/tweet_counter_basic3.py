#username, password and tweet for tweet counter.
class User:
    def __init__(self):
        self.tweet_count = 0

    def login(self):
        error_name = 0
        entry = input("Please login with your username: ")
        while True:
            if entry.count("@") != 1 or entry[0] != "@" or entry.split("@")[1] == "":
                error_name += 1
                if error_name > 3:
                    return "You wrote the wrong username 3 times. Please try later."
                if entry == "":
                    entry = input("Please write something: ")
                    continue
                if entry.count("@") != 1:
                    entry = input("Please enter a string that contains the '@' character only once: ")
                elif entry[0] != "@" or entry.split("@")[1] == "":
                    entry = input("Please use the '@' character at the beginning: ")
            else:
                account_name = entry.split("@")[1]
                print("Welcome {}! Nice to see you.".format(account_name))
                break

class Password:
    def __init__(self):
        self.password = None

    def enter_password(self):
        error_passw = 0
        while True:
            entry = input("Please enter your password: ")
            if len(entry) < 4:
                error_passw += 1
                if error_passw > 2:
                    return "You wrote the wrong password 3 times. Please try later."
                elif len(entry) < 4 and entry != "":
                    print("Your password needs to be longer than 3 characters.")
                elif entry == "":
                    print("Please enter some characters for the password.")
            else:
                return entry

class TweetCounter:
    def __init__(self):
        self.tweet_count = 0

    def tweet(self):
        while True:
            tweet = input("You can write now or quit with 'q': ")
            if tweet.lower() == 'q':
                return "Successfully quit."
            elif tweet:
                self.tweet_count += 1
                print("Your tweet count is now {}.".format(self.tweet_count))
            else:
                print("Please write something.")

def main():
    user = User()
    user.login()

    password = Password()
    password.enter_password()

    tweet_counter = TweetCounter()
    tweet_counter.tweet()

if __name__ == "__main__":
    main()