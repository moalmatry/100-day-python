print(
    """
                _
                ;`',
                `,  `,
                 ',   ;   ,,-""==..,
                  \    ','          \
          ,-""'-., ;    '    __.-="-.;
        ," ,,_    "V      _."
       ;,'   ''-,          "=--,_
              ,-''    _  _       `,
             /   ,.-+(_)(_)�--.,   ;
            ,'  /   ; (_)       `\ ,
            ; ,/    ;._.;         ;
            !,'     ;   ;
            V'      ;   ;
                    ;._.;
                    ;   ;
                    ;   ;        ~
     ~              ;._.;
               ~    ;   ;
                   .�   `.                ~
             __,.--;.___.;--.,___
       _,,-""      ;     ;       ""-,,_
   .-��            ;     ;             ``-.
  ",              �       `               ,"        ~
    "-_                                _-"
~       ``----..,_          __,,..bmw-�
                  ```''''���                  ~
                              ~
             ~
      """
)

print("Welcome to the Treasure Island. \nYour mission is to find the treasure.")
choice1 = input(
    "You're at a crossroad, where do you want to go? Type 'left' or 'right' "
)
if choice1 == "left":
    choice2 = input("Stay or wait for a boat? Type 'wait' or 'swim' ")
    if choice2 == "wait":
        choice3 = input("Which door do you choose? Type 'red', 'blue' or 'yellow' ")
        if choice3 == "yellow":
            print("You Win!")
        elif choice3 == "blue":
            print("Eaten by beasts. Game Over")
        elif choice2 == "red":
            print("Burned by a fire. Game Over")
        else:
            print("Game Over")
    elif choice2 == "swim":
        print("Attacked by trout. Game Over")
    else:
        print("Game Over you entered an invalid choice")
elif choice1 == "right":
    print("Fall into a hole. Game Over")
else:
    print("Game Over you entered an invalid choice")
