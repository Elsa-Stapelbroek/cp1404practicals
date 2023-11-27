"""CP1404 practical 10 - Wikipedia"""

import wikipedia

phrase = input("search phrase: ")
while input != "":
    try:
        topic = wikipedia.page(phrase, auto_suggest=False)
        print(topic.title)
        print(topic.summary)
        print(topic.url)
    except wikipedia.exceptions.DisambiguationError as e:
        print(e.options)
    phrase = input("search phrase: ")
