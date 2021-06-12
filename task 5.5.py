print("Nancy Srivastava 1900300109006")
def copyandcloning(cl):
   copylist = cl[:]
   return copylist
A=list()
n1=int(input("Enter the size of the List ::"))
print("Enter the Element of List ::")
for i in range(int(n1)):
   k=int(input(""))
   A.append(k)
clon = copyandcloning(A)
print("Before Cloning The List Is:", A)
print("After Cloning The List Is:", clon)