import json
import random

j = json.loads(open('information.json').read())

def getRandomItem(items):
    return items[random.randint(0, len(items) - 1)]

def getIdea():
    mood = getRandomItem(j["mood"])
    theme1 = getRandomItem(j["theme"])
    random.seed()
    theme2 = getRandomItem(j["theme"])
    genre1 = getRandomItem(j["genre"])
    random.seed()
    genre2 = getRandomItem(j["genre"])
    perspective = getRandomItem(j["perspective"]);
    character = getRandomItem(j["character"]["description"]) + ' ' + getRandomItem(j["character"]["nature"]) + ' ' + getRandomItem(j["character"]["description_post"])
    setting = getRandomItem(j["settings"]["place"]).format(description = getRandomItem(j["settings"]["description"]))
    goal = getRandomItem(j["goal"])
    wildcard = getRandomItem(j["wildcard"])

    return getRandomItem(j["template"]).format(mood = mood,
                                              theme1 = theme1,
                                             theme2 = theme2,
                                             perspective = perspective,
                                            genre1 = genre1,
                                            genre2 = genre2,
                                           character = character,
                                          setting = setting,
                                          wildcard = wildcard,
                                          goal = goal)

print(getIdea())
while True:
    input()
    print(getIdea())

