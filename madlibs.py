from splash import *
from input import *
import story1
import Story2

def madlibs():
    print splash()
    raw_input()
    end = False
    while not end:
        print menu()
        option = getMenuOption()
        if option == "q":
            end = True
        elif option == "1":
            print story1.story()
            raw_input()
        elif option == "2":
            print Story2.story()
            raw_input()
    print "Good Bye!"
    

    
madlibs()
