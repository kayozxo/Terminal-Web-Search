import webbrowser
import sys
import colorama
from colorama import Fore

colorama.init(autoreset = True)

site = sys.argv[1]

if site == "sp":
  print(Fore.GREEN + "Searching Spotify...")
  url = 'https://open.spotify.com/search/'

if site == "yt":
  print(Fore.GREEN + "Searching YouTube...")
  url = 'https://www.youtube.com/results?search_query='

if site == "md":
  print(Fore.GREEN + "Searching Medium...")
  url = 'https://www.medium.com/search?q='

if site == "rt":
  print(Fore.GREEN + "Searching Reddit...")
  url = 'https://www.reddit.com/search/?q='

if site == "g":
  print(Fore.GREEN + "Searching Google...")
  url = 'https://www.google.com/search?q='

if site == "pt":
  print(Fore.GREEN + "Searching Pinterest...")
  url = 'https://www.pinterest.com/search/pins?q='

if site == "wk":
  print(Fore.GREEN + "Searching Wikipedia...")
  url = 'https://en.wikipedia.org/wiki/'

if site == "x":
  print(Fore.GREEN + "Searching Twitter...")
  url = 'https://www.twitter.com/search?q='

if site == "gt":
  print(Fore.GREEN + "Searching Github...")
  url = 'https://www.github.com/search?q='

def create_query():
  query = sys.argv[2:]
  return ' '.join(query)

def create_url():
  if len(sys.argv[2:]) == 0:
    print(Fore.RED + "Error: Please enter a valid search query.")
  else:
    final_url = url + create_query()
    webbrowser.open(final_url)

create_url()