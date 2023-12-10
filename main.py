# Text Adventure Game 🎮-------------
Answer = input("Do You Want To Play This Game? [Yes/No] : ")

if Answer =="Yes":
    print("Welcome To the Game!")
    Answer = input("Do You want to go jungle or Cave? [Jungle/ Cave] : ")
    if Answer == "Jungle":
        print("You See the hungry Tiger To The Jungle And He Also Attacked Them, So You Are Loss Please Try Again")
    elif Answer == "Cave":
        print("Then Their are a Bear Sleeping")
        Answer = input("So You Fight The Bear or Run! [Fight/Run]: ")
    if Answer == "Fight":
        print("The Bear So Strong and He Also Kill You, So You are Loss Them.")
        
    if Answer == "Run":
        print("So You Are Already Save To The Bear")
        Answer = input("So You Can Safe Properly, Then You Go Home Or Again Go the Bear? [Home/Again Cave] : ")
    if Answer == ("Home"):
        print("Congratulations You Are Win")
    if Answer == "Again Cave":
        print("You Loss The Game Please Try Again")
else:
    print("The Game Closed")
