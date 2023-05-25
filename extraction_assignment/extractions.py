
import re
import requests
from bs4 import BeautifulSoup
import os
import sys 


def data_extraction(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    phone_numbers = re.findall(r'\+?\d{10}(?:\s+\d{3}-\d{3}-\d{4})?\b', soup.get_text())
    # emails = re.findall(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b', soup.get_text())
    emails = re.findall(r"[A-Za-z0-9%_+-.]+"
                     r"@[A-Za-z0-9.-]+"
                     r"\.[A-Za-z:;*$#]{2,6}",soup.get_text())
    links = [link.get('href') for link in soup.find_all('a', href=True)]
    return phone_numbers, emails, links


def save_emails(emails, filename):
    with open(os.path.join(sys.path[0], "exmails.txt"), 'w') as c2file:
        for email in emails:
            c2file.write(email + '\n')


# url = input("Enter the website URL: ")
# filename = input("Enter the filename to save the emails: ")

def executable():
    url = input("Enter the website URL: ")
    filename = input("Enter the filename to save the emails: ")

    phone_numbers, emails, links = data_extraction(url)
    print("Phone Numbers:")
    print(phone_numbers)
    print("Emails:")
    print(emails)
    print("Links:")
    print(links)

    save_emails(emails, filename)
    print(f"Emails saved to '{filename}'.")
    input("Press Enter to exit...")


if __name__ == '__main__':
    executable()
