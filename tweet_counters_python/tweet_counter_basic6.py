from tkinter import *
from user_password_tweet import User, Password, TweetCounter
import py_compile

# Compile the imported module (Replace with your actual code's path)
py_compile.compile("YOUR CODE'S PATH HERE. example: C:\\Users\user1\\Desktop\python.py\\tweet_counter_basic6.py")

# Define User class to handle user-related operations
class User:
    def __init__(self):
        self.username = None

    def is_valid_username(self, username):
        if not username.startswith("@"):
            self.username_message = "Username must start with '@'."
            return False
        if username.count("@") != 1:
            self.username_message = "Username should have exactly one '@' symbol."
            return False
        if len(username) <= 1:
            self.username_message = "Username should have at least two characters."
            return False
        if not username[1:].isalnum():
            self.username_message = "Username should only contain letters and numbers after '@'."
            return False
        self.username_message = ""  # Reset the message when the username is valid
        return True

    def get_account_name(self):
        return self.username.capitalize()

# Define Password class to manage password-related operations
class Password:
    def __init__(self):
        self.password = None

    def is_valid_password(self, password):
        if len(password) < 8:
            self.password_message = "Password must have at least 8 characters."
            return False
        if not any(char.isdigit() for char in password):
            self.password_message = "Password must contain at least one digit."
            return False
        if not any(char.isalpha() for char in password):
            self.password_message = "Password must contain at least one letter."
            return False
        self.password_message = ""  # Reset the message when the password is valid
        return True

# Define TweetCounter class to track tweets and their count
class TweetCounter:
    def __init__(self):
        self.tweets = []

    def add_tweet(self, tweet):
        self.tweets.append(tweet)

    def get_tweet_count(self):
        return len(self.tweets)

    def get_tweets(self):
        return self.tweets

# Define TweetCounterGUI class to create the graphical user interface
class TweetCounterGUI:
    def __init__(self, master):
        # ... (Code to set up the graphical interface) ...
        self.master = master
        master.title("Tweet Counter v0.5")
        master.geometry("925x700")

        # Set font and background color for labels and buttons
        label_font = ("Helvetica", 14)
        button_font = ("Helvetica", 12)
        label_bg = "#F0F0F0"
        button_bg = "#3498db"
        canvas_bg = "#34495e"

        self.user = User()
        self.password = Password()
        self.tweet_counter = TweetCounter()

        self.canvas = Canvas(master, bg=canvas_bg)
        self.canvas.pack(fill="both", expand=True)

        self.tweet_label = Label(self.canvas, text="Tweet:", font=label_font, bg=label_bg)
        self.tweet_entry = Entry(self.canvas, font=label_font)
        self.tweet_button = Button(self.canvas, text="Tweet", command=self.tweet, font=button_font, bg=button_bg, fg="white")
        self.tweet_history_label = Label(self.canvas, text="Previous Tweets:", font=label_font, bg=label_bg)
        self.tweet_history_text = Text(self.canvas, height=5, state="disabled", font=label_font)

        self.username_label = Label(self.canvas, text="Username:", font=label_font, bg=label_bg)
        self.username_entry = Entry(self.canvas, font=label_font)
        self.password_label = Label(self.canvas, text="Password:", font=label_font, bg=label_bg)
        self.password_entry = Entry(self.canvas, show="*", font=label_font)
        self.login_button = Button(self.canvas, text="Login", command=self.login, font=button_font, bg=button_bg, fg="white")
        self.quit_button = Button(self.canvas, text="Quit", command=master.quit, font=button_font, bg="#e74c3c", fg="white")
        self.message_label = Label(self.canvas, text="", font=label_font, bg=canvas_bg, fg="#e74c3c")

        self.tweet_label.grid(row=0, column=0, pady=10, padx=10, sticky=E)
        self.tweet_entry.grid(row=0, column=1, pady=10, padx=10, sticky=W)
        self.tweet_button.grid(row=1, column=0, columnspan=2, pady=10)
        self.tweet_history_label.grid(row=2, column=0, columnspan=2, pady=10)
        self.tweet_history_text.grid(row=3, column=0, columnspan=2, pady=10, padx=10, sticky="ew")
        self.tweet_history_scrollbar = Scrollbar(self.canvas, orient="vertical", command=self.tweet_history_text.yview)
        self.tweet_history_text.config(yscrollcommand=self.tweet_history_scrollbar.set)

        self.username_label.grid(row=4, column=0, pady=(30, 10), padx=10, sticky=E)
        self.username_entry.grid(row=4, column=1, pady=(30, 10), padx=10, sticky=W)
        self.password_label.grid(row=5, column=0, pady=10, padx=10, sticky=E)
        self.password_entry.grid(row=5, column=1, pady=10, padx=10, sticky=W)
        self.login_button.grid(row=6, column=0, columnspan=2, pady=20)
        self.quit_button.grid(row=7, column=0, columnspan=2, pady=10)
        self.message_label.grid(row=8, column=0, columnspan=2, pady=(10, 0))

        self.tweet_history_label.grid(row=2, column=0, columnspan=2, pady=10)
        self.tweet_history_text.grid(row=3, column=0, columnspan=2, pady=10, padx=10, sticky="nsew")
        self.tweet_history_scrollbar.grid(row=3, column=2, pady=10, sticky="ns")

        self.tweet_entry.config(state="disabled")
        self.tweet_button.config(state="disabled")
        self.tweet_history_text.config(state="disabled")

    def login(self):
        # ... (Code to handle user login and update interface) ...
        username = self.username_entry.get()
        password = self.password_entry.get()

        if username and password:
            if self.user.is_valid_username(username) and self.password.is_valid_password(password):
                self.user.username = username
                message_text = f"Logged in as {self.user.get_account_name()}."
                self.username_entry.delete(0, 'end')
                self.password_entry.delete(0, 'end')
                self.tweet_entry.config(state="normal")
                self.tweet_button.config(state="normal")
                self.message_label.config(text=message_text, fg="#2ecc71")
            else:
                message_text = self.user.username_message or self.password.password_message
                self.message_label.config(text=message_text, fg="#e74c3c")
        else:
            message_text = "Please enter a username and password."
            self.message_label.config(text=message_text, fg="#e74c3c")

    def tweet(self):
        # ... (Code to handle tweeting and update interface) ...
        tweet = self.tweet_entry.get()
        if tweet:
            self.tweet_counter.add_tweet(tweet)
            message = f"Your tweet count is now {self.tweet_counter.get_tweet_count()}."
            self.message_label.config(text=message, fg="#2ecc71")
            self.update_tweet_history()

    def update_tweet_history(self):
        # ... (Code to update and display tweet history) ...
        self.tweet_history_text.config(state="normal")
        self.tweet_history_text.delete("1.0", "end")
        for idx, tweet in enumerate(self.tweet_counter.get_tweets(), start=1):
            self.tweet_history_text.insert("end", f"{idx}. {tweet}\n")
        self.tweet_history_text.config(state="disabled")

# Create the main application window
root = Tk()

# Initialize the TweetCounterGUI with the main window
my_gui = TweetCounterGUI(root)

# Start the event loop to run the application
root.mainloop()