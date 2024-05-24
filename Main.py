
def printNum():
    for i in range(1,101):
        print('FizzBuzz' if i%3==0 and i%5==0 else 'Buzz' if i%5==0 else 'Fizz' if i%3==0 else i)
printNum()

print("-------------------------------------")

def countChar():
    string=input("enter string \n")
    dictionary=dict() 
    for s in string:
        val= [k for k in dictionary.keys() if k==s]
        if val:
            dictionary[s]=dictionary[s]+1
        else :
            dictionary[s]=1
    print(dictionary)
    for k,v in dictionary.items():
        print(k,"=>",v)

countChar()


print("-------------------------------------")

def isPalindrome(s):
    normalized_str = ''.join(char.lower() for char in s if char.isalnum())
    return normalized_str == normalized_str[::-1]

test_str = "Was it a car or a cat I saw"
#test_str = "Hello python"
if isPalindrome(test_str):
    print(f'"{test_str}" is a palindrome.')
else:
    print(f'"{test_str}" is not a palindrome.')



