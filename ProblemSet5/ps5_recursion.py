# 6.00x Problem Set 5
#
# Part 2 - RECURSION

#
# Problem 3: Recursive String Reversal
#
def reverseString(aStr):
    """
    Given a string, recursively returns a reversed copy of the string.
    For example, if the string is 'abc', the function returns 'cba'.
    The only string operations you are allowed to use are indexing,
    slicing, and concatenation.
    
    aStr: a string
    returns: a reversed string
    """
    # empty or 1 character string, return itself
    # print aStr
    if len(aStr) <= 1:
        return aStr
    else:
        return aStr[-1] + reverseString(aStr[1:-1]) + aStr[0]
       


#
# Problem 4: X-ian
#
def x_ian(x, word):
    """
    Given a string x, returns True if all the letters in x are
    contained in word in the same order as they appear in x.

    >>> x_ian('eric', 'meritocracy')
    True
    >>> x_ian('eric', 'cerium')
    False
    >>> x_ian('john', 'mahjong')
    False
    
    x: a string
    word: a string
    returns: True if word is x_ian, False otherwise
    """
    if len(x) == 0:
        return True
    if len(word) == 0:
        return False

    if x[0] == word[0]: # matched a letter
        return x_ian(x[1:], word[1:]) # move on to the next letter in both
    else:
        return x_ian(x, word[1:]) # same x, next letter in word


#
# Problem 5: Typewriter
#
def insertNewlines(text, lineLength):
    """
    Given text and a desired line length, wrap the text as a typewriter would.
    Insert a newline character ("\n") after each word that reaches or exceeds
    the desired line length.

    text: a string containing the text to wrap.
    line_length: the number of characters to include on a line before wrapping
        the next word.
    returns: a string, with newline characters inserted appropriately. 
    """
    #print text, lineLength
    if len(text) < lineLength:
        return text + "\n"

    if text[lineLength -1] == ' ':
        return insertNewlines(text[lineLength:], lineLength) 
    else:
        return insertNewlines(text, lineLength + 1)
