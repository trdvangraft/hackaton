import json


def getPrerequisitesName(courses, key):
    prerequisitesNames = []
    prerequisites = courses[key]["prerequisites"]
    for prerequisiteID in prerequisites:
        if prerequisiteID != "none":
            try:
                prerequisitesNames.append(courses[prerequisiteID]["name"])
            except:
                print("does not exists")
    return prerequisitesNames


if __name__ == '__main__':

    # with open('../digieduhack/database/courses2.json', encoding="utf8") as \
    #         json_file:
    #     courses = json.load(json_file)
    #     #print(json.dumps(courses["CS-A1110"], indent=4))
    #     getPrerequisitesName(courses["CS-A1110"])

    json_file = open('../digieduhack/database/courses2.json', encoding="utf8")
    courses = json.load(json_file)
    # print(json.dumps(courses["CS-A1110"], indent=4))
    names = getPrerequisitesName(courses, "ARTS-A0501")
    for i in names:
        print(i)
    json_file.close()

#from rake_nltk import Rake
