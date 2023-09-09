#Compiler code of tweet_counter_basic6.py
import py_compile
# Compile the imported module (Replace with your actual code's path)
py_compile.compile("YOUR CODE'S PATH HERE. example: C:\\Users\user1\\Desktop\python.py\\user_password_tweet.py")
class User:
    def __init__(self):
        self.username = None

    def is_valid_username(self, username):
        return len(username) > 0

    def get_account_name(self):
        return self.username.capitalize()

class Password:
    def __init__(self):
        self.password = None

    def is_valid_password(self, password):
        return len(password) > 0

class TweetCounter:
    def __init__(self):
        self.tweet_count = 0
