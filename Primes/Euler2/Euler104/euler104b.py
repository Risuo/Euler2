
tableOfFib = [1,1,2,3]

#rewrite some things to make the table dynamically update, run it for two, run the test, if no good, create a third, and remove the first, and repeat until good

#fibIndex = n+1, so, fibonacci 100 == index 99

bothGood = False
n = 0
while bothGood == False:
    n += 1
    if len(tableOfFib) == 4:
        tableOfFib.remove(tableOfFib[0])
        tableOfFib.append((tableOfFib[2])+(tableOfFib[1]))
    else:
        tableOfFib.append((tableOfFib[2])+(tableOfFib[1]))
    original = tableOfFib[3]
    last9 = str(original%10**9)
    value = 0
    for x in last9:
        if last9.count(str(x)) == 1 and str(x) != '0': 
            value += 1
            if value == 9:
                print last9, n, 'back 9'
                value = 0
                front9 = original
                while front9 > 10**9:
                    front9 = front9/10
                front9 = str(front9)
                for x in front9:
                    if front9.count(str(x)) == 1 and str(x) != '0':
                        value += 1
                    else:
                        break
                    if value == 9:
                        print front9, n, 'front 9'
                        bothGood = True
                        break
                    
        else:
            break


