import random
BotNumber = random.randint(1,101)
UserInput  =int(input("Enter Your Value:-"))
if UserInput>BotNumber:
    print("Bot Number is:-",BotNumber)
    print("Sorry Your Number is Higher than the Bot🥲")
elif BotNumber>UserInput:
    print("Bot Number is:-", BotNumber)
    print("Sorry Your Number is Lower than the Bot🥲")
else:
    print("Bot Number is:-", BotNumber)
    print("Hurreeehh! You Guessed it Right💖")
