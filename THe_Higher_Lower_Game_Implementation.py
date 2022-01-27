logo1='''
  _    _ _       _                
 | |  | (_)     | |               
 | |__| |_  __ _| |__   ___ _ __  
 |  __  | |/ _` | '_ \ / _ \ '__| 
 | |  | | | (_| | | | |  __/ |    
 |_| _|_|_|\__, |_| |_|\___|_|    
    | |     __/ |                 
    | |    |___/_      _____ _ __ 
    | |    / _ \ \ /\ / / _ \ '__|
    | |___| (_) \ V  V /  __/ |   
    |______\___/ \_/\_/ \___|_| 
'''    
   
logo2=''' 
 __      __    
 \ \    / /    
  \ \  / /__   
   \ \/ / __|  
    \  /\__ \_ 
     \/ |___(_)
     
     '''
    
import random
from THe_Higher_Lower_Game_Data import data



print("Welcome to the Higher Lower Game:\n\n")


score=0
compare_A=[]
compare_B=[]

def compare_B_account():
    compare_B=random.choice(data)
    compare_B['value']='B'
    return compare_B


def compare_A_account():
    compare_A=random.choice(data)
    compare_A['value']='A'
    return compare_A

def compare_accounts(compare_A,compare_B):
    global logo2
    follower_A=int(compare_A['follower_count'])
    follower_B=int(compare_B['follower_count'])
    #print(follower_A)
    #print(follower_B)
    if follower_A==follower_B:
        while follower_A!=follower_B: 
            compare_A= compare_A_account() 
            compare_B= compare_B_account()   
            string_compare_A=f"{compare_A['name']}, {compare_A['description']}, from {compare_A['country']}."   
            print("Compare A:",string_compare_A)
            print(logo2)
            string_compare_B=f"{compare_B['name']}, {compare_B['description']}, from {compare_B['country']}."   
            print("Against B:",string_compare_B) 
          #  print(follower_A)
          #  print(follower_B)
    
    
    else:
     
       string_compare_A=f"{compare_A['name']}, {compare_A['description']}, from {compare_A['country']}."   
       print("Compare A:",string_compare_A)
       
       print(logo2)    
       string_compare_B=f"{compare_B['name']}, {compare_B['description']}, from {compare_B['country']}."   
       print("Against B:",string_compare_B)
 


is_correct=1

while is_correct==1:
       
    compare_A= compare_A_account()
    compare_B= compare_B_account()
    follower_A=int(compare_A['follower_count'])
    follower_B=int(compare_B['follower_count'])
    compare_accounts(compare_A,compare_B) 
    user_input=input("Who has more followers? Type 'A' or 'B':")
    
    if user_input=='A' and follower_A > follower_B:
        score+=1
        print(f"You gueseed it correct! Current Score:{score}")

        
    elif user_input=='B' and follower_B > follower_A:
        score+=1
        print(f"\nYou gueseed it correct! Current Score:{score}\n\n")

    else:
           print(f"\n\nSorry! you are wrong. Total Score:{score}\n") 
           is_correct=0
        
        
    
    
    
    
