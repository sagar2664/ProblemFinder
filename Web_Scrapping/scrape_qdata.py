import os
import requests
from bs4 import BeautifulSoup

def parse_website(url):
    headers = {
        'User-Agent': 'Your User Agent String Here',
    }
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        return response.content
    else:
        print("Failed to retrieve webpage:", response.status_code)
        return None

def scrape_and_save_problem_statement(links_file, output_folder):
    # Create the output folder if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    with open(links_file, 'r') as file:
        for idx, link in enumerate(file, start=4675):
            link = link.strip()  # Remove leading/trailing whitespace and newline characters
            print(f"Scraping problem statement from link {idx}: {link}")
            html_content = parse_website(link)
            if html_content:
                try:
                    soup = BeautifulSoup(html_content, 'html.parser')
                    # Find all elements with class 'problem-statement' and extract text
                    problem_statement = soup.find(class_='problem-statement').get_text()
                    # Generate a filename for the text file
                    filename = os.path.join(output_folder, f'problem_statement_{idx}.txt')
                    # Save the problem statement text to a file
                    with open(filename, 'w', encoding='utf-8') as text_file:
                        text_file.write(problem_statement)
                    print(f"Problem statement saved to: {filename}")
                except (AttributeError, UnicodeEncodeError):
                    # Handle cases where the problem statement cannot be found or encoding error occurs
                    print(f"Unable to save problem statement for link {idx}")
                    filename = os.path.join(output_folder, f'problem_statement_{idx}.txt')
                    with open(filename, 'w', encoding='utf-8') as text_file:
                        text_file.write("")  # Write an empty file

# Define paths and filenames
links_file = 'problem_links_2.txt'  # File containing the list of links
output_folder = 'qdata'  # Folder to save problem statement files

# Scrape problem statement text from links and save to separate files
scrape_and_save_problem_statement(links_file, output_folder)
