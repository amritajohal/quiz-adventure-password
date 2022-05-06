from PIL import Image 
'''
image1 = Image.open('dog.jpeg')
image1.show()
image1 = Image.open('cat.jpeg')
image1.show()
'''

score = 0
def quiz():
    global score 
    global percent
    score = 0
    image1 = Image.open('dog.jpeg')
    image1.show()   
    q1 = input('what animal is this: ').upper()
    q1a = 'dog'.upper()
    image2 = Image.open('cat.jpeg')
    image2.show()
    q2 = input('is this a dog or cat?: ').upper()
    q2a = 'cat'.upper()
    q3 = input('what colour comes after orange in the rainbow?: ').upper()
    q3a = 'yellow'.upper()
    q4 = input('what colour are leaves and grass?: ').upper()
    q4a = 'green'.upper()
    q5 = input('what is a colour that represents sadness?: ').upper()
    q5a = 'blue'.upper()
    q6 = input('what colour is my water bottle?: ').upper()
    q6a = 'purple'.upper()
    q7 = input('is an apple a fruit(yes/no)?: ').upper()
    q7a = 'yes'.upper()
    q8 = input('is an orange a fruit(yes/no)?: ').upper()
    q8a = 'yes'.upper()
    q9 = input('is a carrot a fruit(yes/no)?: ').upper()
    q9a = 'no'.upper()
    q10 = input('is a cucumber a fruit(yes/no)?: ').upper()
    q10a = 'no'.upper()

    if q1 == q1a:
        score = score + 1
    if q2 == q2a:
        score = score + 1
    if q3 == q3a:
        score = score + 1
    if q4 == q4a:
        score = score + 1
    if q5 == q5a:
        score = score + 1
    if q6 == q6a:
        score = score + 1
    if q7 == q7a:
        score = score + 1
    if q8 == q8a:
        score = score + 1
    if q9 == q9a:
        score = score + 1
    if q10 == q10a:
        score = score + 1
    percent = score * 10
    return score 
#add feature where if a str letter is put where there should be a number, u get kicked out 

def play():
    print('your final score is ', quiz(), "out of 10")
    print('or', percent, "%")

def game():
    while True:
        again = input('would u like to play the quiz again y/n? ')
        if again == 'y':
            play()
        elif again == 'n':
            print('ok bye :-]')
            return False 
        else:
            print('try again._.')
            continue 
play()
game()