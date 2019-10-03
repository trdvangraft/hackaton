import sys
import utils


botQuestionKey, userInput = sys.argv[1], sys.argv[2]


result = {
    "output": userInput
}

print(str(result))
sys.stdout.flush()