import json
from utils import *


if __name__ == '__main__':

    # with open('../digieduhack/database/courses2.json', encoding="utf8") as \
    #         json_file:
    #     courses = json.load(json_file)
    #     #print(json.dumps(courses["CS-A1110"], indent=4))
    #     getPrerequisitesName(courses["CS-A1110"])

    courses_file = open('../digieduhack/database/courses.json',
                        encoding="utf8")
    courses = json.load(courses_file)
    users_file = open('../digieduhack/database/users.json',encoding="utf8")
    users = json.load(users_file)
    credits = 5
    filteredCourses = filterOutMissingPrerequisitesAndCredits(users,
                                                              courses, credits)


    #courseAndInterest = {}
    #for course in filteredCourses:
    #    keywords = extractKeywords(course)
    #    interestsOfCourse = keywords2interest(keywords)
    #    courseAndInterest[course["id"]] = interestOfCourse

    # Make the matching here between users and courses based on interest
    # similarity

    users_file.close()
    courses_file.close()

    # print(len(filteredCourses))
    # print(len(courses.keys()))

    # print(json.dumps(courses["CS-A1110"], indent=4))
    # prerequisitesNames = getPrerequisitesName(courses, "ARTS-A0501")
    # for n in prerequisitesNames:
    #     print(n)



#from rake_nltk import Rake
