import requests
from bs4 import BeautifulSoup
import re

def fetch_webpage(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.text
    except requests.RequestException as e:
        print(f"Error fetching {url}: {e}")
        return None

def extract_words(html_content):
    soup = BeautifulSoup(html_content, 'html.parser')
    text = soup.get_text()
    words = re.findall(r'\b\w+\b', text)
    return words

def write_words_to_file(words, filename):
    try:
        with open(filename, 'w') as file:
            for word in words:
                file.write(f"{word}\n")
        print(f"Words written successfully to {filename}")
    except IOError as e:
        print(f"Error writing to file {filename}: {e}")

def main():
    urls = [
        'http://192.168.112.130/index.php',
        'http://192.168.112.130/greatmenu.html',
        'http://192.168.112.130/commentforcarl.php'
    ]
    all_words = []
    
    for url in urls:
        html_content = fetch_webpage(url)
        if html_content:
            words_list = extract_words(html_content)
            all_words.extend(words_list)
        else:
            print(f"Failed to fetch or parse webpage content from {url}")
    
    if all_words:
        write_words_to_file(all_words, 'combined_words_list.txt')
    else:
        print("No words extracted to write to file.")

# Run the program
if __name__ == '__main__':
    main()
