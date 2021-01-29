import random
player_name =input("What is your name....?\n>>>")
print("Are you ready to play with me....\nLet's start then.......")
comp_score=0
user_score=0
while(comp_score<10)and(user_score<10):
    comp_val=random.choice(["rock","paper","scissor"])
    user_val=input("rock..paper..scissor\n>>>")
    print(comp_val)
    if(user_val=="rock"):
        if(comp_val=="rock"):
            print("...........")
        elif(comp_val=="paper"):
            print("ooohhh....!!")
            comp_score+=1
        else:
            print("yeah....!!")
            user_score+=1
    if(user_val=="paper"):
        if(comp_val=="rock"):
            print("yeah.......!!")
            user_score+=1
        elif(comp_val=="paper"):
            print(".......!!")
        else:
            print("noooooo...!!")
            comp_score+=1
    if(user_val=="scissor"):
        if(comp_val=="rock"):
            print("noooo.....!!")
            comp_user+=1
        elif(comp_val=="paper"):
            print("yeahhhh....!!")
            user_score+=1
        else:
            print("........!!")
    print(f"{player_name} score: {user_score},python score: {comp_score}")
if(comp_score==10):
    print(player_name,"you lost.....\nBetter luck next time...!!")
elif(user_score==10):
    print(player_name,"kudos....you won..!!")
    
    
