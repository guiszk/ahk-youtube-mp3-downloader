from youtube_search import YoutubeSearch
from getfromyt import getfromyt
import sys
 
if len(sys.argv) != 2:
    print("Usage: ytsearch.py <query>")
    sys.exit(1)  
results = YoutubeSearch(sys.argv[1], max_results=10).to_dict()
 
for j,i in enumerate(results):
    print(j, i["title"], "|", i["duration"], "|", i["views"], "|", i["channel"])
 
chosen = int(input("> "))
 
getfromyt(results[chosen]["id"])
