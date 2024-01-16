import webbrowser
import sys

site = sys.argv[1]

if site == "sp":
  print("Searching Spotify...")
  url = 'https://open.spotify.com/search/'

if site == "yt":
  print("Searching YouTube...")
  url = 'https://www.youtube.com/results?search_query='

if site == "md":
  print("Searching Medium...")
  url = 'https://www.medium.com/search?q='

if site == "rt":
  print("Searching Reddit...")
  url = 'https://www.reddit.com/search/?q='

if site == "g":
  print("Searching Google...")
  url = 'https://www.google.com/search?q='

def create_query():
  query = sys.argv[2:]
  return ' '.join(query)

def create_url():
  if len(sys.argv[2:]) == 0:
    print("Error: Please Enter a valid search query.")
  else:
    final_url = url + create_query()
    webbrowser.open(final_url)

create_url()