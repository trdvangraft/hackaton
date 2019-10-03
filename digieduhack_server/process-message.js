const { PythonShell } = require('python-shell')
const fs = require('fs');
const rawdata = fs.readFileSync('./messages.json')
const messageData = JSON.parse(rawdata)
// process-message.js
const processMessage = (message, metadata) => {
    matchinKey = null;
    // iterate over possible options
    for (key in messageData) {
        let obj = messageData[key]
        obj.matchers.some(el => message.includes(el)) ? matchinKey = key : null
    }

    if (matchinKey) {
        // tokenize the message and get the context
        console.log('We matched a key')
        // we extract the question from the json
        question = messageData[matchinKey]
        // Now we have to perform the deep match and do parameter extraction
        if (question.numvariables > 0) {
            // question has variables extract them
            // this is also the paramater vector
            let paramArr = new RegExp(question.regex)
                .exec(message)[0]
                .split(" ")
                .filter(el => !question.matchers.includes(el))
            
            callPython(paramArr)
            
            return returner(question.reply, "option", paramArr)
        }
        return returner(question.reply, "option", [])
    }

    return returner(["Couldn't understand you try again please"], "text", [])
   // we found no match program fallback message
}
 
const returner = (replyArr, type, paramArr) => {
    let rawReply = replyPicker(replyArr)
    const replacer = () => paramArr.shift()
    let reply = paramArr.length > 0 ? rawReply.replace(/{INPUT}/g, replacer) : rawReply

    return {
        reply,
        type
    }
}

const replyPicker = (arr) => arr[Math.floor(Math.random() * arr.length)]

const callPython = inputArr => {
    const options = {
        args: [inputArr]
    }

    PythonShell.run('./test.py', options, function (err, data) {
        if (err) console.log(err)
        console.log(data)
    });
}

 module.exports = processMessage;