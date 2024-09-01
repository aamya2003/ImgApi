import requests


url = "https://cc2ca387-a708-4faa-a211-38a865dc110e-00-2590kbzlqvknl.riker.replit.dev/api/rand-image"


res = requests.get(url)

cont = res.content


myfile = open("myphoto.jpg", "wb")

myfile.write(cont)