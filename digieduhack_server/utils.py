

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


