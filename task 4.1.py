print("Nancy Srivastava 1900300109006")
start = int(input("Enter the start of range: "))
end = int(input("Enter the end of range: "))

# iterating each number in list
for n in range(start, end + 1):

    # checking condition
    if (n% 2!=0):
        continue
    print(n, end=" ")