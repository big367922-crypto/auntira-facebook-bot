
def get_reply(message):
    message = message.lower().strip()

    if message in ["hi", "hello", "হাই"]:
        return "Hello! Welcome to my Bot ❤️"

    elif message == "help":
        return "How can I help you?"

    elif message == "bye":
        return "Goodbye! See you again ❤️"

    else:
        return "Sorry, I don't understand."


print("Auntira Bot Started!")

while True:
    user_message = input("You: ")

    if user_message.lower() == "exit":
        print("Bot বন্ধ হয়েছে!")
        break

    reply = get_reply(user_message)
    print("Bot:", reply)
