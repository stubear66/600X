def isMyNumber(guess):
    number = 250
    if guess < number:
        return -1
    elif guess > number:
        return 1
    else:
        return 0


def jumpAndBackpedal(isMyNumber):
    '''
    isMyNumber: Procedure that hides a secret number. 
     It takes as a parameter one number and returns:
     *  -1 if the number is less than the secret number
     *  0 if the number is equal to the secret number
     *  1 if the number is greater than the secret number
 
    returns: integer, the secret number
    ''' 
    guess = 1
    if isMyNumber(guess) == 0:
        return guess
    foundNumber = False
    while not foundNumber:  
        sign = isMyNumber(guess)
        if sign == -1:
            guess *= 2
        elif sign == 1:
            guess -= 1
        else:
            foundNumber = True
    return guess



def generateForm(story, listOfAdjs, listOfNouns, listOfVerbs):
    """ 
    story: a string containing sentences
    listOfAdjs: a list of valid adjectives
    listOfNouns: a list of valid nouns
    listOfVerbs: a list of valid verbs

    For each word in story that is in one of the lists,
    * replace it with the string '[ADJ]' if the word is in listOfAdjs
    * replace it with the string '[VERB]' if the word is in listOfVerbs
    * replace it with the string '[NOUN]' if the word is in listOfNouns

    returns: string, A Mad-Libs form of the story. 
    """
    # Your Code Here
    words = story.split(' ')
    form = ''
    for word in words:
        if word in listOfAdjs:
            form += '[ADJ] '
        elif word in listOfVerbs:
            form += '[VERB] '
        elif word in listOfNouns:
            form += '[NOUN] '
        else:
            form += word + ' '      

    return form


def generateTemplates(madLibsForm):
    """ 
    madLibsForm: string, in a Mad-Lib form. See output of `generateForm`

    returns: a list of '[ADJ]', '[VERB]', and '[NOUN]' strings, in
    the order they appear in the madLibsForm.
    """
    # Your Code Here
    words = madLibsForm.split()
    #print words
    templateStrings = ['[ADJ]', '[VERB]', '[NOUN]' ]
    templateList = [] 
    for word in words:
        if word in templateStrings:
            templateList.append(word)

    return templateList


        
def verifyWord(userWord, madTemplate, listOfAdjs, listOfNouns, listOfVerbs):
    """ 
    userWord: a string, the word the user inputted
    madTemplate: string, the type of word the user was supposed to input
    listOfAdjs: a list of valid adjectives
    listOfNouns: a list of valid nouns
    listOfVerbs: a list of valid verbs):

    returns: Boolean, whether or not the word is valid
    """
    # Your Code Here
    if madTemplate == '[ADJ]':
        if userWord in listOfAdjs:
            return True
    elif madTemplate == '[NOUN]':
        if userWord in listOfNouns:
            return True
    elif madTemplate == '[VERB]':
        if userWord in listOfVerbs:
            return True

    return False

def numPens(n):
    """
    n is a non-negative integer

    Returns True if some non-negative integer combination of 5, 8 and 24 equals n
    Otherwise returns False.
    """
    if n == 0:
        return True
    # Your Code Here
    if  n < 5:
        return False

    if n % 5 == 0 or n % 8 == 0:
        return True
    # otherwise
    # 24 is irrelevant if I can get there with 24 I can get there with 8
    if n > 8:
        return numPens(n-8)
    else:
        return numPens(n-5)
    

    

    
    

    
    


    

    


