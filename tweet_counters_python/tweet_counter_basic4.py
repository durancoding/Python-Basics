#username, password and tweet for tweet counter.
import sys

class User:
    def __init__(self):
        self.username = ""
        self.tweet_count = 0

    def login(self):
        max_attempts = 3
        for _ in range(max_attempts):
            entry = input("Please login with your username: ")
            if self.is_valid_username(entry):
                self.username = entry
                print(f"Welcome {self.get_account_name()}! Nice to see you.")
                return
            else:
                print("Invalid username. Please try again.")
        print(f"You wrote the wrong username {max_attempts} times. Please try later.")
        sys.exit()

    def is_valid_username(self, username):
        return username.startswith('@') and len(username) > 1

    def get_account_name(self):
        return self.username[1:]

class Password(User):
    def __init__(self):
        super().__init__()
        self.password = ""

    def enter_password(self):
        max_attempts = 3
        for _ in range(max_attempts):
            entry = input("Please enter your password: ")
            if self.is_valid_password(entry):
                self.password = entry
                return
            else:
                print("Invalid password. Please try again.")
        print(f"You wrote the wrong password {max_attempts} times. Please try later.")
        sys.exit()

    def is_valid_password(self, password):
        return len(password) >= 4

class TweetCounter(User):
    def __init__(self):
        super().__init__()

    def tweet(self):
        while True:
            tweet = input("You can write now or quit with 'q': ")
            if tweet.lower() == 'q':
                print("Successfully quit.")
                return
            elif tweet:
                self.tweet_count += 1
                print(f"Your tweet count is now {self.tweet_count}.")
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