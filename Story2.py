from input import *

#Written by Russell Mellott
def story():
    location1 = getWord("Enter a location: ")
    adjective1 = getWord("Enter a adjective: ")
    name1 = getWord("Enter a name: ")
    name2 = getWord("Emter a name: ")
    adjective2 = getWord("Enter an adjective: ")
    food1 = getWord ("Enter an food: ")
    amountoftime1 = getWord ("Enter an amount of time: ") 
    activeverb1 = getWord ("Enter an active verb: ")
    verb1 = getWord ("Enter a past tense verb")
    amountoftime2 = getWord ("Enter an amount of time")
    sport1 = getWord ("Enter a sport")
    animal1 = getWord ("Enter an animal")
    
    
    text = ""
    text += "There was once a lad named Dirty Dan, who lived in" + location1
    text += ". Dans house was " + adjective1
    text += ". Dirt McDan lived in the house with" + name1 
    text += " and" + name2 
    text += ".  " + name1 
    text += "was really" + adjective2
    text += "and would bring " + food1
    text += "to cookouts every " + amountoftime1 
    text += ". One day however everything went wrong." + name2 
    text += " decided that he was going to crash the cook out by" + activeverb1
    text += "everyone there. " + name2
    text += "wanted to do this because Dirty Dan had " + verb1 
    text += "his cat" + amountoftime2 
    text += "ago. As a result of this and" + name2  
    text += "'s actions, the two of them decided to play a match of " + sport1  
    text += ". While they did this Dirty Dan was slain in one on one combat against a" + animal1   
    text += "and " + name2 
    text += "was crowned grand champion of" + location1 
    text += ". "   
    
    return text

