m=input("Enter the selected captions :\n")
lst=m.split()

def isPalindrome(mystr):
    if mystr==mystr[::-1]:
        return True
    else:
        return False

print(lst)
result=[]
for ele in lst:
    if isPalindrome(ele):
        result.append(ele)

print(result)
if len(result)>0:
    print("The palindrome caption(s) : ",result)
else:
    print("There is no palindrome captions")
