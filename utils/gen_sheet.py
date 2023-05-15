import os

# from openpyxl import Workbook
import csv
from datetime import datetime, timedelta
import random

from tran_table import (
    generate_cheque_string,
    generate_random_number,
    generate_transaction_string,
)


def gen_date(start_date, end_date):
    """
    Returns a random date between start_date and end_date
    """
    time_between = end_date - start_date
    days_between = time_between.days
    random_number_of_days = random.randrange(days_between)
    random_date = start_date + timedelta(days=random_number_of_days)
    return random_date.strftime("%m/%d/%Y")


def gen_transaction():
    """
    Returns a random transaction name
    """
    transaction_names = ["Payment", "Deposit", "Withdrawal", "Transfer"]
    length = 10
    return generate_transaction_string(words_list=transaction_names, length=length)


def gen_chequeno():
    """
    Returns a random 6-digit check number
    """
    return generate_cheque_string()


def gen_debit():
    """
    Returns a random debit amount between 10 and 1000
    """
    return generate_random_number(start=100, end=3000, decimal=True, decimal_places=2)


def gen_credit():
    """
    Returns a random credit amount between 10 and 1000
    """
    return generate_random_number(start=100, end=3000, decimal=True, decimal_places=2)


def gen_balance():
    """
    Returns a random balance amount between 1000 and 10000
    """
    return generate_random_number(start=100, end=8000, decimal=True, decimal_places=2)


def generate_csv_files(num_files, num_rows):
    """
    Generates num_files CSV files, each containing num_rows rows of data
    """
    try:
        # Create the output folder if it doesn't exist
        if not os.path.exists("output"):
            os.makedirs("output")

        # Write data to each file
        for i in range(num_files):
            # Generate data rows
            start_date = datetime.strptime("01/01/2020", "%m/%d/%Y")
            end_date = datetime.strptime("12/31/2020", "%m/%d/%Y")
            rows = [
                [
                    gen_date(start_date, end_date),
                    gen_transaction(),
                    gen_chequeno(),
                    gen_debit(),
                    gen_credit(),
                    gen_balance(),
                ]
                for _ in range(num_rows)
            ]

            # Save the CSV file
            file_name = f"data_{i+1}.csv"
            file_path = os.path.join("output", file_name)
            with open(file_path, mode="w", newline="") as csv_file:
                writer = csv.writer(csv_file)
                writer.writerow(
                    ["Date", "transactions", "cheque_no", "debit", "credit", "balance"]
                )
                for row in rows:
                    writer.writerow(row)

    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    num_files = 3
    num_rows = 15
    generate_csv_files(num_files, num_rows)
