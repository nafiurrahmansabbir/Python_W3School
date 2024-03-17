class ChatGPT:
    def __init__(self):
        self.user_info = {
            "name": "",
            "university": "",
            "current_semester": ""
        }

    def greet(self):
        return "Hi! What can I do for you?"

    def remember_user(self, name, university, current_semester):
        self.user_info["name"] = name
        self.user_info["university"] = university
        self.user_info["current_semester"] = current_semester

    def get_user_info(self):
        return self.user_info

    def change_semester(self, new_semester):
        self.user_info["current_semester"] = new_semester
        return f"Your current semester has been updated to {new_semester}."

# Main program
def main():
    chatbot = ChatGPT()
    print(chatbot.greet())

    name = input("Enter your name: ")
    university = input("Enter your university: ")
    current_semester = input("Enter your current semester: ")

    chatbot.remember_user(name, university, current_semester)
    print("Thanks for your information.")

    print(chatbot.get_user_info())

    new_semester = input("Enter your new semester: ")
    print(chatbot.change_semester(new_semester))

if __name__ == "__main__":
    main()
