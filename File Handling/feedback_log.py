# User Feedback
feedback = input("Enter your feedback: ")

with open("File Handling/feedback_log.txt", "a") as log:
    log.write(feedback + "\n")

print("Thanks! Your feedback saved.")
# Enter your feedback: boring
# Thanks! Your feedback saved.
