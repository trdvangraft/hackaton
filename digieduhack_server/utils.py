import json

dict = {'Art' : [1, 2], 'Design': [1, 2], 'Architecture': [1, 2], 'Film': [1, 2], \
           'Television': [1, 2],
            'Scenography': [1, 2], 'Media': [1, 2],
                'Management': [1, 2], 'Finance': [1, 2], 'Accounting': [1, 2], 'Marketing': [1, 2], 'Sales': [1, 2], 'Economics': [1, 2], 'Entrepreneurship': [1, 2],
                'Chemical': [1, 2], 'Bioproducts': [1, 2], 'Biosystems': [1, 2],
                'Communications': [1, 2], 'Electrical': [1, 2], 'Networking': [1, 2], 'Automation': [1, 2], 'Electronics': [1, 2], 'Signal': [1, 2], 'Acoustics': [1, 2],
                'Engineering': [1, 2], 'Mechanical': [1, 2], 'Physics': [1, 2],'Mathematics': [1, 2],
            'Industrial': [1, 2], 'Neuroscience': [1, 2], 'Computer': [1, 2]}



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

def importCourses():
    with open('../digieduhack/database/courses.json', encoding="utf8") as json_file:
        courses = json.load(json_file)
        return courses

def computeScore(replies, dict, key):
    indices = dict[key]
    ret = 0
    for i in indices:
        ret += replies[i]
    return ret

# call with user = users["id"]
def computeScores(user, psyReplies):
    u = user["interest"]
    u["art"] = computeScore(psyReplies, dict, "art")
    u["design"] =  computeScore(psyReplies, dict, "design")
    u["architecture"] = computeScore(psyReplies, dict, "architecture")
    u["film"] = computeScore(psyReplies, dict, "film")
    u["television"] = computeScore(psyReplies, dict, "television")
    u["scenography"] = computeScore(psyReplies, dict, "scenography")
    u["media"] = computeScore(psyReplies, dict, "media")
    u["management"] = computeScore(psyReplies, dict, "management")
    u["finance"] = computeScore(psyReplies, dict, "finance")
    u["accounting"] = computeScore(psyReplies, dict, "accounting")
    u["sales"] = computeScore(psyReplies, dict, "sales")
    u["economics"] = computeScore(psyReplies, dict, "economics")
    u["entrepreneurship"] = computeScore(psyReplies, dict, "entrepreneurship")
    u["chemical"] = computeScore(psyReplies, dict, "chemical")
    u["bioproducts"] = computeScore(psyReplies, dict, "bioproducts")
    u["biosystems"] = computeScore(psyReplies, dict, "biosystems")
    u["communications"] = computeScore(psyReplies, dict, "communications")
    u["electrical"] = computeScore(psyReplies, dict, "electrical")
    u["networking"] = computeScore(psyReplies, dict, "networking")
    u["automation"] = computeScore(psyReplies, dict, "automation")
    u["electronics"] = computeScore(psyReplies, dict, "electronics")
    u["signal"] = computeScore(psyReplies, dict, "signal")
    u["acoustics"] = computeScore(psyReplies, dict, "acoustics")
    u["engineering"] = computeScore(psyReplies, dict, "engineering")
    u["mechanical"] = computeScore(psyReplies, dict, "mechanical")
    u["physics"] = computeScore(psyReplies, dict, "physics")
    u["mathematics"] = computeScore(psyReplies, dict, "mathematics")
    u["industrial"] = computeScore(psyReplies, dict, "industrial")
    u["neuroscience"] = computeScore(psyReplies, dict, "neuroscience")
    u["computer"] = computeScore(psyReplies, dict, "computer")
    return u
