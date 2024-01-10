import random
from gamedata import data




logo = """
    __  ___       __             
   / / / (_)___ _/ /_  ___  _____
  / /_/ / / __ `/ __ \/ _ \/ ___/
 / __  / / /_/ / / / /  __/ /    
/_/ ///_/\__, /_/ /_/\___/_/     
   / /  /____/_      _____  _____
  / /   / __ \ | /| / / _ \/ ___/
 / /___/ /_/ / |/ |/ /  __/ /    
/_____/\____/|__/|__/\___/_/     
"""

vs = """
 _    __    
| |  / /____
| | / / ___/
| |/ (__  ) 
|___/____(_)
"""

print(logo)




def celebrity_game():
     person1 = random.randint(0,25)
     person2 = random.randint(25,49)

     celebrity1_name = data[person1]["name"]
     celebrity1_follower_count = data[person1]["follower_count"]
     celebrity1_description = data[person1]["description"]
     celebrity1_country = data[person1]["country"]


     celebrity2_name = data[person2]["name"]
     celebrity2_follower_count = data[person2]["follower_count"]
     celebrity2_description = data[person2]["description"]
     celebrity2_country = data[person2]["country"]


     print("CELEBRITY 1")

     print(f'''
      Celebrity Name : {celebrity1_name}
      Celebrity Country: {celebrity1_country}
      Celebrity Description: {celebrity1_description}             
     ''')

     print(vs)


     print("CELEBRITY 2")

     print(f'''
     Celebrity Name : {celebrity2_name}
     Celebrity Country: {celebrity2_country}
     Celebrity Description: {celebrity2_description}             
     ''')

     choice = int(input("Enter Choice 1 or 2 ! "))
     user_guess = 0
     computer_guess = 0
     user_points = 0
     if choice == 1 :
        user_guess += celebrity1_follower_count 
        computer_guess += celebrity2_follower_count
     else:
        user_guess += celebrity2_follower_count
        computer_guess += celebrity1_follower_count
     if user_guess > computer_guess:
          user_points = user_points + 1
          print("Chips uh Added !")
          celebrity_game()
          print(f"Final Score: {user_points} ")
     else:
          print("Game Over!")     

celebrity_game()
       













