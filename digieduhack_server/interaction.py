import sys

def getPrerequisitesName(course):
    for pre in course["prerequisites"]:
        print(pre["name"])



botQuestionKey, userInput = sys.argv[1], sys.argv[2]

result = {
    "output": userInput
}

print(str(result))
sys.stdout.flush()