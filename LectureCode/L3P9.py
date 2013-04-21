#L3 Problem 9 - Guess the number

low = 0
high = 100

print "Please think of a number between 0 and 100!"
while True:
    guess = (low + high) / 2
    response = 'a'
    while response not in ('hlc'):
       print "Is your secret number " + str(guess) + "?" 
       response = raw_input( "Enter 'h' to indicate the guess is too high.  Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. " )
       if response not in ('hlc'):
           print "Sorry, I did not understand your input."
    
    if response == 'h':
        high = guess
    elif response == 'l':
        low = guess
    elif response == 'c':
        break
    

print "Game over.  Your secret number was: " + str(guess)
