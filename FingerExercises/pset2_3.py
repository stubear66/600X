balance = 320000; annualInterestRate = 0.2
epsilon = 0.01
monthlyInterest = annualInterestRate / 12.0

low = balance / 12.0
high = balance * ((1 + monthlyInterest) ** 12) / 12.0
payment = (low + high) / 2.0

def calcInterest(balance, apr):
    interest = balance * (apr/12.0)
    return interest

newBalance = balance
while abs(newBalance) > epsilon:
    newBalance = balance
    for month in range(1, 13):
        newBalance -= payment
        newBalance += calcInterest(newBalance, annualInterestRate)
    if abs(newBalance) > epsilon:
         if newBalance < 0:
             high = payment
         else:
             low = payment
         payment = (low + high) / 2.0
         
         
payment = round(payment,2)
print "Lowest Payment: " + str(payment)