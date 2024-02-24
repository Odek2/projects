import random
def main():
    playgame()
    score_board()
player= input("Please enter your name: ")
answer = input("Do you want to play a game: ").lower()
def playgame():
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
    hint_1= "i am central for all processes to work "
    answer_1= "central processing unit"
    quiz_2= f"{player.title()},What is ALU"
    hint_2= "I do arithmetics and logical operations "
    answer_2="arithmetic and logic unit"
    
    quiz_3=f"{player.title()},what is UPS"
    answer_3= "uninterupted power supply"
    hint_3= "I supply the power without interaption "
    quiz_4= f"{player.title()},What is RAM"
    answer_4="random access memory"
    hint_4= "I am accessed randomly and am volotile "

    quiz_5= f"{player.title()},What is ROM"
    answer_5="read only memory"
    hint_5= "You can only read me "
    quiz_6= f"{player.title()},What is VM"
    answer_6= "virtual machiene"
    hint_6= "I am a machiene inside a machiene  "
    while game_quiz >0:
        
        questions= [quiz_1,quiz_2,quiz_3,quiz_4,quiz_5,quiz_6]
        question= random.choice(questions)
        #randomizing questions to ask 
        print(question)
        player_answer= input(f"{player}, Enter your answer for hint press h each hint will cost you 0.5 ").lower()
        
        if question ==quiz_1:
            if player_answer==answer_1:
                print("correct!!")
                score+=1
            else:
                if player_answer=="h":
                    score -= 0.5 
                    print(f"Your hint is: {hint_1}")
                else:


                    print("Your answer is not correct!!") 
            
        


        elif question==quiz_2:
        
           if player_answer==answer_2:
               print("Correct!!")
               score+=1
           else:
                if player_answer=="h":
                    score -= 0.5 
                    print(f"Your hint is: {hint_2}")
                else:


                    print("Your answer is not correct!!")


        elif question==quiz_3:
        
           if player_answer==answer_3:
               print("Correct!!")
               score+=1
           else:
                if player_answer=="h":
                    score -= 0.5 
                    print(f"Your hint is: {hint_3}")
                else:


                    print("Your answer is not correct!!")
        elif question==quiz_4:
        
           if player_answer==answer_4:
               print("Correct!!")
               score+=1
           else:
                if player_answer=="h":
                    score -= 0.5 
                    print(f"Your hint is: {hint_4}")
                else:


                    print("Your answer is not correct!!") 
        elif question==quiz_5:
        
           if player_answer==answer_5:
               print("Correct!!")
               score+=1
           else:
                if player_answer=="h":
                    score -= 0.5 
                    print(f"Your hint is: {hint_5}")
                else:


                    print("Your answer is not correct!!") 
        elif question==quiz_6:
        
           if player_answer==answer_6:
               print("Correct!!")
               score+=1
           else:
                if player_answer=="h":
                    score -= 0.5 
                    print(f"Your hint is: {hint_6}")
                else:


                    print("Your answer is not correct!!")                            


               
           
               
           
        
    

        game_quiz -=1 


    percentage= (score/total)*100 

    if percentage>= 60:

         print(f"Congratulations!!! Your score is {percentage}%")   

    else:
         print(f"Your score is {percentage}%, Please try again!!!")    

    #check to congratulate more than 60 percent, invite the player again less than 60 percent 
#implement a quiting mechanis
         
def score_board():
    """
    writes you current score,username to the database 
    """
    pass 



if __name__=="__main__":
    main()
    
