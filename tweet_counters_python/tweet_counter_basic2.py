#username and tweet for tweet counter.
def tweet_counter():
    tweet_count = 0
    error = 0
    entry = input("Please login with your username.:")
    while not (entry.count("@") == 1 and entry[0] == "@"):
        if entry.count("@") != 1:
            entry = input("Please enter a string that contains the '@' character only once:")
        elif entry[0] != "@" or entry.split("@")[1] == "":
            entry = input("Please use the '@' character at the beginning:")
        error += 1
        if error > 2:
            return "You wrote wrong username for 3 times, please try later."
        print("This is not a username.")
    else:
        entry = entry.split("@")[1]
        print("Welcome {}! Nice to see you.".format(entry))

    while True:
        tweet = input("You can write now or quit with using 'q' button.:")
        if tweet.lower() == 'q':
            return "Successfully quited"
        elif tweet != "":
            tweet_count += 1
            print("Your tweet count is now {}.".format(tweet_count))
        else:
            print("Please write something.")

print(tweet_counter())
