#username and tweet for tweet counter.
def tweet_counter():
    tweet_count = 0
    error = 0
    entry = input("Please login with your username.:")
    while not ("@" in entry and "." in entry):
        error += 1
        if error > 2:
            return "You wrote wrong username for 3 times, please try later."
        print("This is not a username.")
        entry = input("Use a valid username:")
    else:
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
