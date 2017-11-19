#my euler109.py solution works, this is taken from the forum, much MUCH shorter solution


doubles = list(range(2,41,2))
doubles.append(50)
all = list(range(0,21))
all.extend(doubles)
all.extend([i for i in range(3,61,3)])
all.append(25)
l = len(all)
print(sum([1 for i in range(l) for j in range(l) for d in doubles if all[i]+all[j]+d < 100 and j>=i]))