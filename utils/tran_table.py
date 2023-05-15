import random
import string
import language_tool_python
from faker import Faker
from datetime import datetime, timedelta
import random


# To generate a date between two ranges
def generate_date_string(start_date, end_date):
    """Generates a date string in the format 'day month year' from a given date range."""
    start_date = datetime.strptime(start_date, "%d-%m-%Y")
    end_date = datetime.strptime(end_date, "%d-%m-%Y")
    days = (end_date - start_date).days
    random_day = start_date + timedelta(days=random.randint(0, days))
    month = random_day.strftime("%b")
    day = random_day.strftime("%d")
    year = random_day.strftime("%Y")
    return f"{day} {month} {year}"


# Generate a transaction string
def generate_transaction_string(words_list, length=10):
    """Generates a string starting with 'TO TRANSFER-INB' or 'BY TRANSFER-INB',
    followed by a sentence generated from a list of words (without repeating words),
    and a random alphanumeric string of the specified length at the end.
    """
    prefix = random.choice(["TO TRANSFER-INB", "BY TRANSFER-INB"])
    sentence_words = random.sample(
        words_list, k=min(random.randint(3, 10), len(words_list))
    )
    sentence = " ".join(word.capitalize() for word in sentence_words)
    suffix = "".join(random.choices(string.ascii_letters + string.digits, k=length))

    # Use language_tool_python library to verify the sentence is grammatically correct
    tool = language_tool_python.LanguageTool("en-US")
    num_attempts = 5
    for i in range(num_attempts):
        matches = tool.check(sentence)
        if len(matches) == 0:
            return f"{prefix} {sentence} {suffix}"
        sentence_words = random.sample(
            words_list, k=min(random.randint(3, 10), len(words_list))
        )
        sentence = " ".join(word.capitalize() for word in sentence_words)

    # If we haven't found a grammatically correct sentence after num_attempts, return the last sentence generated
    return f"{prefix} {sentence} {suffix}"


# generate a random string
def generate_random_string(length=10):
    """Generates a random alphanumeric string of the specified length."""
    return "".join(random.choices(string.ascii_letters + string.digits, k=length))


# A Cheque String
def generate_cheque_string():
    """Generates a random transaction string with a format similar to the provided examples."""
    # Generate the first line of the transaction string
    first_line_prefix = random.choice(["GRPT INB:", "GRPT OUTB:"])
    first_line_igm = "".join(
        random.choices(string.ascii_uppercase + string.digits, k=10)
    )
    first_line_suffix = "".join(random.choices(string.digits, k=2))
    first_line = f"{first_line_prefix}\n{first_line_igm}{first_line_suffix}"

    # Generate the second line of the transaction string
    second_line_prefix = random.choice(["TRANSFER TO", "TRANSFER FROM"])
    second_line = (
        f"{second_line_prefix}\n{''.join(random.choices(string.digits, k=13))}"
    )

    # Generate the third line of the transaction string
    third_line = "M/S PAYTM" if random.random() < 0.5 else "IRCTC POOL"

    # Generate the fourth line of the transaction string
    fourth_line = "COMMISSION A/C" if random.random() < 0.5 else "ACCOUNT"

    # Generate the final string
    return f"{first_line}\n{second_line}\n{third_line}\n{fourth_line}\n{generate_random_string()}"


# Generate Trasaction Item List for a given number
def generate_transaction_items(num_items):
    """Generates a list of transaction-related items using the Faker library."""
    fake = Faker()
    items = []

    # Add ATM, PAYTM, SBI CRED, and GRPT to the list of items
    items.extend(["ATM", "PAYTM", "SBI CRED", "GRPT"])

    # Generate additional items using the Faker library
    for i in range(num_items - 4):
        item = ""

        # Randomly select a category of transaction-related item
        category = random.choice(["merchant", "bank", "currency", "transaction_type"])

        # Generate an item based on the selected category
        if category == "merchant":
            item = fake.company()
        elif category == "bank":
            item = fake.bank_name()
        elif category == "currency":
            item = fake.currency_name()
        elif category == "transaction_type":
            item = random.choice(["Purchase", "Refund", "Transfer", "Withdrawal"])

        # Add the generated item to the list of items
        items.append(item)

    return items


# Generate random number between range
def generate_random_number(start, end, decimal=False, decimal_places=2):
    """Generates a random number between start and end, with optional decimal point and decimal places."""
    rand_num = random.uniform(start, end)
    if decimal:
        rand_num = round(rand_num, decimal_places)
    return rand_num


# print(generate_transaction_string(["ATM", "PAYTM", "SBI CRED", "GRPT"]))
# print(generate_cheque_string())
