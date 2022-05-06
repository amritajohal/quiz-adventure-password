from PIL import Image 

def greet():
    global name 
    while True:
        name = input("what is ur name?: ")
        if all(x.isalpha() or x.isspace() for x in name):
            print('hello, ', name,'!')
            break
        else:
            print("oops! not a name.")
            continue 

def invalid():
    print('that was invalid, so ur ded._.')

greet()

def game():
    global image1, image2, image3, image4
    while True:
        print(name, ' spawns in the middle of a forebst. there are a bunch of apple trees around u. ')
        image1 = Image.open('apples.jpeg')
        image1.show()
        apples = input('ur starving... do u eat one? (y/n): ').upper()
        
        if apples == 'y'.upper():
            print('u suddenly gain a ton of energy! u stumble upon a bridge.')
            image3 = Image.open('bridge.jpeg')
            image3.show()
            run = input('do u... cross it(a) or keep walking(b)?:').upper()
            
            if run == 'a'.upper():
                print('u cross it and reach a body of water.')
                image2 = Image.open('boat.jpeg')
                image2.show()
                boat = input('how do u escape?: SWIM or BOAT ?: ').upper()
                
                if boat == 'BOAT'.upper():
                    print('the boat led u all the way to civilization! but theres a storm.')
                    image4 = Image.open('storm.jpeg')
                    image4.show()
                    keepgoing = input('do u keep going (a) or wait for the storm to pass (b)?:  ').upper()
                    
                    if keepgoing == 'a'.upper():
                        print('congrats, ', name, '! ur hard work payed off, u made it back home. :-]')
                    elif keepgoing == 'b': 
                        print('err... the storm got u. ur ded ._.')
                    else:
                        invalid()
                        break
                
                elif boat == 'SWIM': 
                    print('uhhh... what... u drowned ._.')
                else:
                    invalid()
                    break
                    
            elif run == 'b'.upper():
                print('nope that was useless... ur ded ._.')
                break 
            else:
                invalid()
                break

        elif apples == 'n'.upper():
            print('well there was nothing else... so u starved. ur ded ._.')
        else:
            invalid()
            break
    
game()

def ask():
    while True: 
        playagain = input('wanna try again(y/n)?: ').upper()
        if playagain == 'y'.upper():
            game()
        else:
            print('ok... have a good day!')
            break 

while True:
    ask()
    break


