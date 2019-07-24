bye = 0
while bye != "q" : # 'q' used for ending simulation
    import random # import random package
    print ("This is a dice rolling simulation program")
    print ("press enter to roll")
    input () #leaving space  
    number = random.randint (1,6)
    if number == 1:
        print("[------------]")
        print("[            ]")
        print("[     O      ]")
        print("[            ]")
        print("[------------]")
        print("Input 'q' to exit simulation")
        print ()
        bye = input()
    if number == 2:
        print("[------------]")
        print("[            ]")
        print("[    O O     ]")
        print("[            ]")
        print("[------------]")
        print("Input 'q' to exit simulation")
        bye = input()
    if number == 3:
        print("[------------]")
        print("[            ]")
        print("[    O  O    ]")
        print("[    O       ]")
        print("[------------]")
        print("Input 'q' to exit simulation")
        bye = input()
    if number == 4:
        print("[------------]")
        print("[            ]")
        print("[    O  O    ]")
        print("[    O  O    ]")
        print("[------------]")
        print("Input 'q' to exit simulation")
        bye = input()
    if number == 5:
        print("[------------]")
        print("[    O       ]")
        print("[    O  O    ]")
        print("[    O  O    ]")
        print("[------------]")
        print("Input 'q' to exit simulation")
        bye = input()
    if number == 6:
        print("[------------]")
        print("[    O  O    ]")
        print("[    O  O    ]")
        print("[    O  O    ]")
        print("[------------]")
        print("Input 'q' to exit simulation")
        bye = input()
        
