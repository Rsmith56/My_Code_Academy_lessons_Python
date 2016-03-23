#Test of Functions calling other Functions
def shout(phrase):
    if phrase == phrase.upper():
        return ("YOU'RE SHOUTING!")
    else:
        return ("Can you speak up?")

shout("I'm INTERESTED IN SHOUTING")
