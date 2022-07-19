import random
response='y'


while response == 'y':
    no= random.randint(1,6)
    if no == 1:
        print('[     ]')
        print('[     ]')
        print('[  0  ]')
        print('[     ]')
        print('[     ]') 
    elif no == 2:
        print('[     ]')
        print('[     ]')
        print('[ 00  ]')
        print('[     ]')
        print('[     ]') 
    elif no == 3:
        print('[     ]')
        print('[     ]')
        print('[ 000 ]')
        print('[     ]')
        print('[     ]') 
    elif no == 4:
        print('[     ]')
        print('[ 00  ]')
        print('[ 00  ]')
        print('[     ]')
        print('[     ]') 
    elif no == 5:
        print('[     ]')
        print('[ 00  ]')
        print('[  0  ]')
        print('[ 00  ]')
        print('[     ]') 
    else:
        print('[     ]')
        print('[ 00  ]')
        print('[ 00  ]')
        print('[ 00  ]')
        print('[     ]') 
    respone="n"
    
response = input("Do you want to roll the dice ")
print("\n")
