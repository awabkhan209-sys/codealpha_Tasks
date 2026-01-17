import re

# input file open karo
with open("email.txt", "r") as file:
    text = file.read()

# email pattern
emails = re.findall(r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}", text)

# output file mein save karo
with open("found_emails.txt", "w") as file:
    for email in emails:
        file.write(email + "\n")

print("Emails extract ho kar found_emails.txt mein save ho gayi hain")
