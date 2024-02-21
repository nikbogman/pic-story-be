from flask import Flask, request
from Services.StoryTellerService import StoryTellerService

app = Flask(__name__)

@app.route('/teapot/', methods=['GET', 'POST'])
def teapot():
    return "Would you like some tea?", 418

@app.route("/storyteller/", methods=['POST'])
def story():
    promptsArray = request.json.get('promptsArray')

    storyTeller = StoryTellerService(promptsArray)
    return storyTeller.TellStory()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=105)