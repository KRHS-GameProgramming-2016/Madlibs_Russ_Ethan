def isSwear(word):
    swearList = ["poop",
                 "pee"
                 "shit"
                 "ass"
                 "fuck"
                 "bitch"
                 "faggot"
                 "anus"
                 "nigger"
                 "kike"
                 "dyke"
                
                 "penis"
                 "dick"
                 "cock"
                 "vagina"
                 "pussy"
                 "cunt"
                 "chink"
                 "masterbation"
                 "Im an alabama friend and I wanna be free"
                 
                 ]
    if word in swearList:
        return True
    else:
        return False

def getMenuOption():
    goodInput = False
    goodResponses = ["1",
                     "2",
                     "3",
                     "q"]
    while not goodInput:
        response = raw_input("Make a selection: ")
        if response.lower() in goodResponses:
            goodInput = True
        else:
            print "Please make a valid selection!"
    return response.lower()

def getWord(prompt):
    goodInput = False
    while not goodInput:
        response = raw_input(prompt)
        goodInput = True
        if isSwear(response):
            goodInput = False
            print "BAD, UR TRASH, DON'T SAY THAT"
        return response

def getNumber(prompt):
    goodInput = False
    numbers = "0123456789."
    while not goodInput:
        response = raw_input(prompt)
        goodInput = True
        for character in response:
            if character not in numbers:
                goodInput = False
                print "Only numbers dipshit"
    return response
        
        



















