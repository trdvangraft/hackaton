import json
from utils import *


if __name__ == '__main__':

    # with open('../digieduhack/database/courses2.json', encoding="utf8") as \
    #         json_file:
    #     courses = json.load(json_file)
    #     #print(json.dumps(courses["CS-A1110"], indent=4))
    #     getPrerequisitesName(courses["CS-A1110"])

    json_file = open('../digieduhack/database/courses.json', encoding="utf8")
    courses = json.load(json_file)
    # print(json.dumps(courses["CS-A1110"], indent=4))
    prerequisitesNames = getPrerequisitesName(courses, "ARTS-A0501")
    for n in prerequisitesNames:
        print(n)
    json_file.close()



#from rake_nltk import Rake
