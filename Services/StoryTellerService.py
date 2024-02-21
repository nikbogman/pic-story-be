import random
class StoryTellerService:
    def __init__(self, wordsArray):
        self.story = self.GenerateStory(wordsArray)

    def TellStory(self):
        return self.story
    
    def GenerateStory(self, wordsArray):
        random.shuffle(wordsArray)
        words = ' '.join(wordsArray)
        prompt = "Can you create a story using the following words: " + words
        # implement model here
        return prompt