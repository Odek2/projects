import random
def main():
    playgame()
    pass 
player= input("Please enter your name: ")
answer = input("Do you want to play a game: ").lower()

def playgame():
    pass
if answer != "yes":
    print(f"Hello, {player.title()} see you next time. Bye!")
else:


    game_quiz=input(f"Hello,{player.title()} how many questions are you willing to answer?")
    game_quiz=int(game_quiz)
    # check the number of games the person is willing to play-done 
    #ask the person random question n number of times-done 
    total=game_quiz
    score=0
    quiz_1= f"{player.title()},what is CPU"
    answer_1= "central processing unit"
    quiz_2= f"{player.title()},What is ALU"
    answer_2="arithmetic and logic unit"
    quiz_3=f"{player.title()},at is UPS"
    answer_3= "uninterupted power supply"
    quiz_4= f"{player.title()},What is RAM"
    answer_4="random access memory"

    quiz_5= f"{player.title()},What is ROM"
    answer_5="read only memory"
    quiz_6= f"{player.title()},What is VM"
    answer_6= "virtual machiene"
    while game_quiz >0:
        
        questions= [quiz_1,quiz_2,quiz_3,quiz_4,quiz_5,quiz_6]
        question= random.choice(questions)
        #randomizing questions to ask 
        print(question)
        player_answer= input(f"{player}, Enter your answer: ").lower()
        
        if question ==quiz_1:
            if player_answer==answer_1:
                print("correct!!")
                score+=1
            else:
                print("Your answer is not correct!!") 

        elif question==quiz_2:
        
           if player_answer==answer_2:
               print("Correct!!")
               score+=1
           else:
                print("Your answer is not correct!!")


        elif question==quiz_3:
        
           if player_answer==answer_3:
               print("Correct!!")
               score+=1
           else:
                print("Your answer is not correct!!")
        elif question==quiz_4:
        
           if player_answer==answer_4:
               print("Correct!!")
               score+=1
           else:
                print("Your answer is not correct!!") 
        elif question==quiz_5:
        
           if player_answer==answer_5:
               print("Correct!!")
               score+=1
           else:
                print("Your answer is not correct!!") 
        elif question==quiz_6:
        
           if player_answer==answer_6:
               print("Correct!!")
               score+=1
           else:
                print("Your answer is not correct!!")                             


               
           
               
           
        
    

        game_quiz -=1 


percentage= (score/total)*100 

if percentage>= 60:

    print(f"Congratulations!!! Your score is {percentage}%")   

else:
    print(f"Your score is {percentage}%, Please try again!!!")    

    #check to congratulate more than 60 percent, invite the player again less than 60 percent 
#implement a quiting mechanism

if __name__=="__main__":
    main()
    

 
#implement the main function to make it a packages 
        

    

    
