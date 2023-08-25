"""Let's create a random password generator"""
import random
import string
print("WELCOME! Let's create a password generator")
def main():
    length=int(input("Enter the length you desire your password to be= "))
    uppercase=string.ascii_uppercase
    lowercase=string.ascii_lowercase
    digits=string.digits
    symbols=string.punctuation
    combine=uppercase+lowercase+digits+symbols
    finalresult=random.sample(combine,length)
    password="".join(finalresult)
    print(password)
    main()
main()









































# """PASSWORD GENERATOR"""
# import random
# import string
# print("WELCOME!")
# def main():
#     length=int(input("Enter the length you desire for your password= "))
#     uppercase= string.ascii_uppercase
#     lowercase= string.ascii_lowercase
#     digits= string.digits
#     symbols= string.punctuation
#     combine=uppercase+lowercase+digits+symbols
#     finalresult=random.sample(combine,length)
#     password="".join(finalresult)
#     print(password)
#     main()
# main()

