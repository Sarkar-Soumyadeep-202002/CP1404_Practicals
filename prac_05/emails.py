"""
Name: Soumyadeep Sarkar
Description: Program to store email ids and names of users in a dictionary.
"""


def name(email):
    """Find out the names of users from their email ids."""
    s = ""
    index = email.find('@')
    fullname = email[:index]
    names = fullname.split('.')
    for item in names:
        s += item
        s += ' '
    s = s.title()
    reply = input("Is your name {} ? (Y/N) ".format(s))
    reply = reply.upper()
    if reply == 'Y' or reply == '' or reply == "YES":
        return s
    else:
        actual_name = input("Name: ")
        return actual_name


def main():
    """Start the program"""
    email = input("Email: ")
    email_notebook = {}
    while email != "":
        email_notebook[email] = name(email)
        email = input("Email: ")
    for k, v in email_notebook.items():
        print("{} ({})".format(v, k))


main()
