class Email:
    def __init__(self, sender, receiver, content):
        self.sender = sender
        self.receiver = receiver
        self.content = content
        self.is_sent = False

    def send(self):
        self.is_sent = True

    def get_info(self):
        return f"{self.sender} says to {self.receiver}: {self.content}. Sent: {self.is_sent}"

some_information = input()

final_email = []

while some_information != "Stop":
    tokens = some_information.split(" ")
    sender = tokens[0]
    receiver = tokens[1]
    content = tokens[2]

    the_email = Email(sender, receiver, content)
    final_email.append(the_email)

    some_information = input()

email_indices = list(map(int, input().split(", ")))

for current_indice in email_indices:
    final_email[current_indice].send()

for current_email in final_email:
    print(current_email.get_info())