print("Nancy Srivastava 1900300109006")
def oldlist(l1,n):
   for i in range(n):
      print(l1[i], end = " ")
def newlist(l1, n):
    for i in range(n):
       if ((i + 1) % 2 == 0):
         l1[i] = "#"
    oldlist(l1, n)
l1 = [ 5,6,7,8,9 ]
n = len(l1)
newlist(l1, n)