out = []

for x in xrange(1,10000):
    out.append(x**2)
    
    
valid = set()

for x in xrange(10000):
    squareSumValue = 0
    count = 0
    for y in out[x-1:]:
        squareSumValue += y
        count += 1
        if count >= 2:
            if squareSumValue < 10**8:
                valid.add(str(squareSumValue))

print len(valid)

def isPalindrome(string):
    if len(string)%2 == 0:
        firstHalf = string[0:(len(string)/2)]
        secondHalf = string[:(len(string)/2)-1:-1]
        if firstHalf == secondHalf:
            return True
        else:
            return False
    else:
        firstHalf = string[0:len(string)/2]
        secondHalf = string[:(len(string)/2):-1]
        if firstHalf == secondHalf:
            return True
        else:
            return False

palindromeSum = 0

for x in valid:
    if isPalindrome(x):
        palindromeSum += int(x)
        
print palindromeSum

        