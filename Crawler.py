import requests
from bs4 import BeautifulSoup
import os
import time
from colorama import Fore, Style




def print_with_animation(text):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(0.03)  # Adjust the sleep duration for speed
    print()
    
def print_colored_figlet_text(text, color):
    os.system(f"figlet -f slant '{text}' > temp_figlet.txt")  # Generate figlet text to a temporary file
    with open("temp_figlet.txt", "r") as file:
        figlet_output = file.read()
    os.remove("temp_figlet.txt")  # Remove temporary file

    colored_text = f"{color}{figlet_output}{Style.RESET_ALL}"  # Apply color after figlet
    print(colored_text) 










print_colored_figlet_text("KORISHEE THE CYBERMASTER", Fore.GREEN)
print_with_animation(f"{Fore.RED}PRESENTING A AUTOMATED WEB LINKS CRAWLER")
def extract_links(url):
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'html.parser')
        links = [link.get('href') for link in soup.find_all('a')]
        return links
    except Exception as e:
        print(f"Error: {e}")
        return []

def crawl(url, depth):
    if depth == 0:
        return

    links = extract_links(url)
    print(f"Links extracted from {url}:")
    for link in links:
        if link and 'http' in link:  # Filter out non-HTTP links
            print(link)  # Print each link individually
            crawl(link, depth - 1)

if __name__ == "__main__":
    starting_url = input("Enter the domain name (e.g., https://example.com): ")
    max_depth = 2  # Set the maximum depth of crawling, change as needed

    crawl(starting_url, max_depth)
