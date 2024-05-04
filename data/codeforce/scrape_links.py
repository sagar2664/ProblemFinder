import requests
from bs4 import BeautifulSoup

def parse_website(url):
    headers = {
        'User-Agent': 'Your User Agent String Here',
    }
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        return soup
    else:
        print("Failed to retrieve webpage:", response.status_code)
        return None

def find_links_with_problem_pattern(soup):
    links = soup.find_all('a', href=lambda href: href and href.startswith("/problemset/problem"))
    return links

def save_links_to_file(links, filename):
    with open(filename, 'a') as file:  # Append mode to add links from multiple pages
        i=0       
        for link in links:
            if i%2:
                file.write("https://codeforces.com" + link.get('href') + '\n')
            i+=1

# Loop through page numbers from 1 to 51
for page_number in range(1, 51):
    url = f"https://codeforces.com/problemset/page/{page_number}"  # Update URL with current page number
    print(f"Scraping page {page_number}: {url}")
    
    parsed_html = parse_website(url)

    if parsed_html:
        problem_links = find_links_with_problem_pattern(parsed_html)
        print("Links on the webpage with href starting with '/problemset/problem':")
        # for link in problem_links:
        #     print(link.get('href'))

        # Save links to a text file
        save_links_to_file(problem_links, 'test_links.txt')
