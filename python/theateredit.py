import sys

print()
print()
print()
print("Welcome to Fordox Uncommons Cinema!".upper().center(70))
print()
print("To celebrate summer we are selling all tickets for $7!".center(70))
print("Children & adults!".center(70))
print("The movies that are showing today are:".center(70))
print("Alice in Wonderland 2, Finding Dory,".center(70))
print("Nerve, Titanic, and Adventure Time".center(70))
print()
movie_price = 7
whatmovie = input("What movie will you be seeing today?").lower().strip()
if whatmovie == "alice in wonderland 2":
    print()
    print("""                             龴ↀ◡ↀ龴
                         ,------------.
                         |   Alice's   `.
                         | Adventures in |
                         |  Wonderland   |
                         `---------------' \n""")

    print("   Goood Choice! The Mad Hatter is madder than ever before!\n")
elif whatmovie == "finding dory":
    print("""
                                  O  o
                             _\_   o
                          /\/  o\ .
                          \/\___='""".center(70))
    print()
    print("Great choice! If you liked Finding Nemo you'll LOVE this!\n")
elif whatmovie == "nerve":
    print()
    print("""
                          ,   ,
                         /(   )\-
                         \ \_/ /   , /\ ,
                         /_   _\  /| || |\-
                        | \> </ | |\_||_/|
                        (_  ^  _)  \____/
                      /`\|IIIII|/`\ _\/_
                      \  \_____/  /  ()
                      /\   )=(   /\  ()
                     /  `-.\=/.-'  \ ()""")
    print()
    print("                Ahh, bit of a Dare Devil, eh?")
    print()
elif whatmovie == "titanic":
    print()
    print('''
                          ,:',:`,:'
                        ___||__||_||_||___
                ____["""["]""""["]"""["]"""]___
                \ " '''
          ''''''
          ''''''
          '''""""""""""""""""""""""""" |
                 ------------------------------
          ~^~~^~^~^^~^~^~^~^~^~^~^~~^~^~^~^~~^~^~~^~~''')
    print()
    print("                            CLASSIC! ")
    print()
elif whatmovie == "adventure time":
    print("\n                 What Time Is It? You already know!")
    print("      |(•◡•)| ▬▬ι═══════ﺤ  ADVENTURE TIME!  -═══════ι▬▬ (❍ᴥ❍ʋ)\n")
else:
    print("                  Sorry, That Movie Isn't In Right Now.")
    print("""                              ¯\_(ツ)_/¯ """)
    print("                       Try entering another one!")
    print()
    whatmovie = input("What movie will you be seeing today?").lower().strip()
    if whatmovie == "alice in wonderland 2":
        print()
        print("""                                龴ↀ◡ↀ龴
                            ,------------.
                            |   Alice's   `.
                            | Adventures in |
                            |  Wonderland   |
                            `---------------' \n""")

        print("   Goood Choice! The Mad Hatter is madder than ever before!\n")
    elif whatmovie == "finding dory":
        print("""
                                      O  o
                                 _\_   o
                              /\/  o\ .
                              \/\___='""".center(70))
        print()
        print("Great choice! If you liked Finding Nemo you'll LOVE this!\n")
    elif whatmovie == "nerve":
        print()
        print("""
                              ,   ,
                             /(   )\-
                             \ \_/ /   , /\ ,
                             /_   _\  /| || |\-
                            | \> </ | |\_||_/|
                            (_  ^  _)  \____/
                          /`\|IIIII|/`\ _\/_
                          \  \_____/  /  ()
                          /\   )=(   /\  ()
                         /  `-.\=/.-'  \ ()""")
        print()
        print("                Ahh, bit of a Dare Devil, eh?")
        print()
    elif whatmovie == "titanic":
        print()
        print('''
                              ,:',:`,:'
                            ___||__||_||_||___
                    ____["""["]""""["]"""["]"""]___
                    \ " '''
              ''''''
              ''''''
              '''""""""""""""""""""""""""" |
                     ------------------------------
              ~^~~^~^~^^~^~^~^~^~^~^~^~~^~^~^~^~~^~^~~^~~''')
        print()
        print("                            CLASSIC! ")
        print()
    elif whatmovie == "adventure time":
        print("\n                 What Time Is It? You already know!")
        print(
            "      |(•◡•)| ▬▬ι═══════ﺤ  ADVENTURE TIME!  -═══════ι▬▬ (❍ᴥ❍ʋ)\n")
    else:
        print("Sorry, I don't think that movie is in.")
        print(
            "               If you are having trouble, please speak\n               with one of our workers. If not go back\n              to home and press start again. Thank You(:")
        sys.exit()
ticketnumber = input("How many tickets will you be buying?")
print("awesome!".capitalize())
print()

print(str.center("=======(New Addition: Candy! $8)=======", 70))
print()
#difference between movietheater.py and this is this one
#has a list below
price_list = [["Soft Drinks: $", 2], ["Popcorn: $", 3], ["Sweet tea: $", 2],
              ["Candy: $", 8]]

print("Here are our concessions:")
for i in range(len(price_list)):
    print(price_list[i][0], price_list[i][1])
print()
concessions = input(
    "Will you be buying any concessions to go along with your movie?").lower(
    ).strip()
if (concessions == "yes"):
    print("GREAT!".lower().capitalize())
    drinks = input("How many drinks are you buying?")
    corn = input("How many popcorn boxes are you buying?")
    candy = input("How many bags of candy are you buying?")

    print()
    drink_price = 2
    corn_price = 3
    candy_price = 8
    drinks2 = (str(int(drinks) * drink_price))
    corn2 = (str(int(corn) * corn_price))
    candy2 = (str(int(candy) * candy_price))
    ticketnumber2 = (str(int(ticketnumber) * movie_price))
    print(
        "==========================================================================")
    print(str.center("   (っ◕‿◕)っhere's your receipt!", 60).upper())
    print("                    Your drink total will be: $" + (str(int(
        drinks) * drink_price)))
    print("                    Your popcorn total will be: $" + (str(int(
        corn) * corn_price)))
    print("                    Your candy total will be: $" + (str(int(
        candy) * candy_price)))
    print("                    Your movie total will be: $" + (str(int(
        ticketnumber) * movie_price)))
    print("                        Complete Total: $" + (str(float(
        drinks2) + float(corn2) + float(candy2) + float(ticketnumber2))))
    print()
    print("                          Enjoy the movie!")
    print()

    print(
        "==========================================================================")
elif (concessions == "no"):
    print("Thats fine. Maybe next time?")
    print()
    print(
        "========================================================================")
    print(str.center("     (っ◕‿◕)っhere's your receipt!", 60).upper())
    print("                    Your movie total will be: $" + (str(int(
        ticketnumber) * movie_price)))
    print()
    print("                    ~Have a Fordox Fantastic Day!~")
    print()
    print(
        "========================================================================")
else:
    print()
    print()
    print()
    print(str.center("Sorry I don't understand. Please type yes or no.", 70))
    print()

    print(str.center("=======(New Addition: Candy! $8)=======", 70))
    print()
    #difference between movietheater.py and this is this one
    #has a list below
    price_list = [["Soft Drinks: $", 2], ["Popcorn: $", 3],
                  ["Sweet tea: $", 2], ["Candy: $", 8]]

    print("Here are our concessions:")
    for i in range(len(price_list)):
        print(price_list[i][0], price_list[i][1])
    print()
    concessions = input(
        "Will you be buying any concessions to go along with your movie?").lower(
        ).strip()
    if (concessions == "yes"):
        print("GREAT!".lower().capitalize())
        print()
        drinks = input("How many drinks are you buying?")
        corn = input("How many popcorn boxes are you buying?")
        candy = input("How many bags of candy are you buying?")

        print()
        drink_price = 2
        corn_price = 3
        candy_price = 8
        drinks2 = (str(int(drinks) * drink_price))
        corn2 = (str(int(corn) * corn_price))
        candy2 = (str(int(candy) * candy_price))
        ticketnumber2 = (str(int(ticketnumber) * movie_price))
        print(
            "==========================================================================")
        print(str.center("   (っ◕‿◕)っhere's your receipt!", 60).upper())
        print("                    Your drink total will be: $" + (str(int(
            drinks) * drink_price)))
        print("                    Your popcorn total will be: $" + (str(int(
            corn) * corn_price)))
        print("                    Your candy total will be: $" + (str(int(
            candy) * candy_price)))
        print("                    Your movie total will be: $" + (str(int(
            ticketnumber) * movie_price)))
        print("                        Complete Total: $" + (str(float(
            drinks2) + float(corn2) + float(candy2) + float(ticketnumber2))))
        print()
        print("                          Enjoy the movie!")
        print()

        print(
            "==========================================================================")
    elif (concessions == "no"):
        print("Thats fine. Maybe next time?")
        print()
        print(
            "========================================================================")
        print(str.center("     (っ◕‿◕)っhere's your receipt!", 60).upper())
        print("                    Your movie total will be: $" + (str(int(
            ticketnumber) * movie_price)))
        print()
        print("                    ~Have a Fordox Fantastic Day!~")
        print()
        print(
            "========================================================================")
    else:
        print()
        print("                 Sorry, I still didn't get your input.")
        print("                If you are having trouble, please speak")
        print("                   with one of our workers. Thank you.")
        print(
            "========================================================================")
        print(str.center("     (っ◕‿◕)っhere's your receipt!", 60).upper())
        print("                    Your movie total will be: $" + (str(int(
            ticketnumber) * movie_price)))
        print()
        print("                    ~Have a Fordox Fantastic Day!~")
        print()
        print(
            "========================================================================")
        sys.exit
