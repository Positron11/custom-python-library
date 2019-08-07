def fibonacci(limit):
    """Print all fibonacci numbers until <limit>"""
    current = 1
    previous = 0
    while current < limit:
        yield current
        current, previous = current + previous, current


def squares(limit):
    """Print all squares of whole numbers until <limit>"""
    for num in range(1, limit + 1):
        yield num ** 2


def print_all(values):
    """Print all values in list,as string, with values separated by commas"""
    print(", ".join(map(str, [val for val in values])))


def camel_case(string):
    """Converts a string to camel-case lettering"""
    return " ".join(["".join([x.upper() if word.index(x) == 0 else x for x in word]) for word in string.split()])


def filter_list(iterable, *args):
    """Filters a list for values in <*args>"""
    return [val for val in iterable if val not in [*args]]


def caesar_shift(string, shift, mode):
    """Encrypts/decrypts <string> with a caesar shift, the shift being <shift>"""
    alphabet = [chr(x) for x in range(97, 123)]
    shifted_alphabet = alphabet[(shift % 26):] + alphabet[:(shift % 26)]
    return "".join([(shifted_alphabet[alphabet.index(x)] if mode == "encrypt" else alphabet[shifted_alphabet.index(x)])
                    if x in alphabet else x for x in string])


def substitution_cipher(string, seed, mode):
    """Encrypts/decrypts text by substitution with shuffled alphabet"""
    import random
    alphabet = [chr(x) for x in range(97, 122)]
    shuffled_alphabet = list(alphabet)
    random.seed(seed)
    random.shuffle(shuffled_alphabet)
    random.seed()
    if mode == "encrypt":
        string = "".join([x + chr(random.randint(97, 122)) for x in string])
        string = string[::-1]
        string = "".join([shuffled_alphabet[alphabet.index(x)] if x in alphabet else x for x in string])
    else:
        string = "".join([alphabet[shuffled_alphabet.index(x)] if x in alphabet else x for x in string])
        string = string[::-1]
        string = string[::2]
    return string


def get_wikipedia_thumbnail(topic, file):
    """Gets thumbnail from requested wikipedia article"""
    import requests
    import bs4
    res = requests.get(f"https://en.wikipedia.org/wiki/{topic}", "lxml")
    page = bs4.BeautifulSoup(res.text, 'lxml')
    image_info = page.select(".infobox img") if page.select(".infobox") else page.select(".thumbimage")
    image_link = "https:" + image_info[0]["src"]
    image = requests.get(image_link, "lxml").content
    with open(f"{file}", "wb") as file:
        file.write(image)


def send_email(recipient, subject, body, password):
    """Sends an email to <recipient> with <subject> and <body>"""
    import smtplib
    email = smtplib.SMTP("smtp.gmail.com", 587)
    email.ehlo()
    email.starttls()
    email_account = recipient
    password = password
    email.login(email_account, password)
    from_address = "youdontknoweveryone@gmail.com"
    to_address = recipient
    subject = subject
    body = body
    message = "Subject: " + subject + "\n" + body
    email.sendmail(from_address, to_address, message)


def input_opt(prompt, valid):
    """Takes input with <prompt> and verifies validity of input against values in <valid>"""
    while True:
        x = input(prompt)  # Take user input
        if x.lower() in valid:  # If the user input is in the list of "valid" cases...
            return x  # Return user input
        else:  # Otherwise...
            print_between_lines("Invalid option. Choose again.")  # Print error message


def print_divider(length=80):
    """Prints a line of length <length> (default 80)"""
    print("-" * length)


def print_between_lines(text, length=10):
    """Prints <text> between lines of length <length> (default 10)"""
    print(f"{'-' * length}\n{text}\n{'-' * length}")


def remove_duplicates(values):
    """Removes duplicates from sets of data"""
    new_list = list()  # New empty list to contain individual values
    for value in values:  # For each value in original list...
        if value not in new_list:  # If the value is not already in the new list...
            new_list.append(value)  # Add value to new list
    return new_list  # Return new list


def modal_value(values):
    """Finds the modal value(s) in a set of data"""
    return [x for x in remove_duplicates(values) if values.count(x) == max([values.count(y) for y in remove_duplicates(values)])]
