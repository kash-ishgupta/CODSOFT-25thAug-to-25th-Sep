"""QUIZ GAME"""
print("WELCOME")
print("Rules of the game are as follows: \n" 
      "1. correct answer giver you 2 points\n"
      "2. wrong answer deducts 1 point\n")
def main():
    name=input("Enter your name= ")
    print(f"Hi {name}\n")
    option=['a','b','c','d']
    answer=['correct','wrong']
    print("Let's start with the quiz\n"
        "All the best!\n")
    q1="An application used for picture editing?"
    q2="______ is used as the first code for every language"
    q3="An application used for online payments?"
    q4="A music playing application among the options is?"


    print(f"Q1.{q1}\n"
        "a.Udemy\n"
        "b.Photoshop\n"
        "c.Whatsapp\n"
        "d.Instagram")
    option=input("The answer is= ")
    if option=='b':
        print("correct\n")
        score1=2
    else:
        print("wrong\n")
        score1=-1

    print(f"Q2.{q2}\n"
        "a.Login\n"
        "b.Welcome\n"
        "c.Hello World\n"
        "d.Start")
    option=input("The answer is= ")
    if option=='c':
        print("correct\n")
        score2=score1+2
    else:
        print("wrong\n")
        score2=score1-1

    print(f"Q3.{q3}\n"
        "a.Paytm\n"
        "b.Twitter\n"
        "c.Subway Surfers\n"
        "d.Gmail")
    option=input("The answer is= ")
    if option=='a':
        print("correct\n")
        score3=score2+2
    else:
        print("wrong\n")
        score3=score2-1

    print(f"Q4.{q4}\n"
        "a.Photos\n"
        "b.Blinkit\n"
        "c.Camera\n"
        "d.Spotify")
    option=input("The answer is= ")
    if option=='d':
        print("correct\n")
        score4=score3+2
    else:
        print("wrong\n")
        score4=score3-1

    print("GAME ENDED")
    print(f"Your total score is= {score4}\n")

    again=input("Want to play again?   ")
    main()
main()
