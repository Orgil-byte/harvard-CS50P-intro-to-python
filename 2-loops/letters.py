message_structure= [{
    "sender": "orgil","receiver":"Luigi"},
    {"sender": "orgil","receiver":"fewf"},
    {"sender": "orgil", "receiver":"e32w"}]

list= ["Luigi", "fewf", "e32w"]

def main():
    for message in message_structure:
        print(write_letter( message["sender"], message["receiver"]))

    for receivers in list:
        print(write_letter("orgil", receivers))


def write_letter(sender, receiver):
    return f"U r dmb fck {receiver}, sent by {sender}"

main()