# A Callback function is a function that you pass as an argument to another function,
# so that it can be called (executed) later, usually after some action is completed.

def on_button_click(callback): # show_message
    print("🖱 Button clicked") # Once this print got executed
    callback()

def show_message():
    print("👋 Hello Devesh, Welcome!")

on_button_click(show_message) # 🖱 Button clicked
                              # 👋 Hello Devesh, Welcome!
