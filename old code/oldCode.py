def dictionary():
  cubes = { }
  i = 0
  while True:
  	i+=1
  	index = ''.join(sorted(str(i**3)))
  	if index not in cubes:
  		cubes.update({index : {"count" : 1, "number" : [i], "cube" : [i**3]}})
  	else:
  		cubes[index]["number"].append(i)
  		cubes[index]["cube"].append(i**3)
  		cubes[index]["count"] = len(cubes[index]["cube"])
  		if cubes[index]["count"] == 5:
  			print (str(cubes[index]["number"][0]) + "^3 = " + str(cubes[index]["cube"][0]) + " " + str(cubes[index]["number"]))
  			break 
  			
			
def euler75():
  def gcd(a,b):
    while b: a, b = b, a%b
    return abs(a)
  
  table = {}
   
  def findCoPrimes(limit):
    a = 0
    b = 0
    c = 0
    for n in xrange(1,limit):
      for m in xrange(n,limit):
        if m**2 + n**2 > limit/2:
          break
        else:
          if m > 1 and m > n:
            if gcd(m,n) == 1:
              if (m-n)%2 != 0:
                for z in xrange(1, limit):
                  a = z*(m**2 - n**2)
                  b = z*(2*m*n)
                  c = z*(m**2 + n**2)
                  if (a+b+c) > limit:
                    break
                  else:
                    if a+b+c in table:
                      table.update({(a+b+c):{"total":[2]}})
                      for k in xrange(2,limit):
                        if k*(a+b+c) > limit:
                          break
                        else:
                          if k*(a+b+c) in table:
                            table.update({(k*(a+b+c)):{"total":[2]}})
                          else:
                            table.update({(k*(a+b+c)):{"total":[1]}})
                    else:
                      table.update({(a+b+c):{"total":[1]}})
    return table
  
  # table.update({12:{"sides":[3, 4, 5], "total":[1]}})
  
  findCoPrimes(450)
  count = 0
  for x in table:
    count += table[x]["total"][0]
  print count
 
print euler75()