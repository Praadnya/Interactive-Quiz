import random
import sys
import mysql.connector as sqltor


count=0
count1=0
count2=0

a=input('Hey there,enter your name: ')

def sql():
    mydb = sqltor.connect(host = "localhost", user = "root", passwd="tiger",database="lochan")
    mc = mydb.cursor()

    print(a,count)
    sql = "INSERT INTO user (Username, Marks_scored) VALUES (%s, %s)"
    val = (a, count)
    mc.execute(sql, val)

    mydb.commit()


print('Welcome to the quiz',a,'!!!')
print('''
These are the guidelines of the game:
   -There are 3 levels-easy, moderate and hard.
       -Each of the 8 questions in Level 1 has 1 point.
       -To clear Level 1 and proceed to Level 2 you must score a minimum of
        4 points.
       -Each of the 10 questions in Level 2 has 3 points.
       -To clear Level 2 and proceed to Level 3 you must score a minimum of
        12 points.
       -Each of the 12 questions in Level 3 has 5 points.
       -To clear Level 3 you must score a minimum of 20 points.
       -In all three each wrong answer warrants 1 negative point.
Enjoy the quiz!
''')
b=input('Are you ready to start-yes or no?: ')
print()
if b=='yes' or b=='YES':
    print('Ok, here is your first question...')
    print()
else:
    print('ok cool! See you later!!')
    sys.exit()

def level1():
    global count
    qlist=[e[0],e[1],e[2],e[3],e[4],e[5],e[6],e[7],e[8],e[9],e[10],e[11],e[12],e[13],e[14]]
    for c in range(0,8):
        rand=(random.choice(qlist))
        del qlist[qlist.index(rand)]
        d=list(rand)
        print(d[0])
        print(d[1])
        print(d[2])
        print(d[3])
        print(d[4])
        print()	
        ans=input("Answer:")
        if ans==d[5] or ans==d[6]:
            print('CORRECT ANSWER!!!')
            print()
            count+=1
            print('You have a total of',count,'points.')
            print()
        else:
           print('WRONG ANSWER')
           print()
           count=count-1
           print('Sorry you lost one point.You have a total of',count,'points.')
           print('The right answer is',d[5])
           print()
         	           
count=0    
e=[
['Which of these food items has different varieties such as:"Suji ka _______,"Aate ka _______,"Moong dal ka _________"and "Gajar ka _________"?',
 'A. Sharbat','B. Halwa','C. Pakora','D. Chaat','B','b'],
['Which of these is the name of a type of women’s clothing?',
 'A.Padmini','B.Man Bai','C.Jodha','D.Anarkali','D','d'],
['Which of these foods would complete the name of these three common dishes: Kadhai _______, Shahi _______, and Matar ______?',
 'A. Dahi','B. Ghee','C. Paneer','D. Khoya','C','c'],
['Which of these is a board game which can normally be played by only two opponents at a time?',
 'A. Snakes and Ladders','B. Chess','C. Ludo','D. Monopoly','B','b'],
['Which organization is the birthplace of World Wide Web?',
 'A.CERN','B.NASA','C.IUPAP','D.University of Cambridge','A','a'],
['What do koalas like to eat?',
 'A.carrots','B.yogurt','C.eucalyptus leaves','D.chives','C','c'],
['What is the correct synonym of "DEMENTED"?',
 'A.noisy','B.insane','C.dangerous','D.happy','B','b'],
['How many states make up the United States of America?',
  'A.39','B.49','C.27','D.50','D','d'],
['Complete the title of the play by Shakespeare –"The Merchant of _____"?',
  'A.Antium','B.Blackheath','C.Venice','D.Cyprus','C','c'],
['Brie and Camembert come under which category food?',
  'A.Breads','B.Cheese','C.Chocolates','D.Pies','B','b'],
['Which fictional detective lived at 221B Baker Street?',
  'A.Hercule Poirot','B.Abigail Adams','C.Sherlock Holmes','D.Jane Austen','C','c'],
['Where were croissants first baked?',
  'A.France','B.Argentina','C.Spain','D.Mexico','A','a'],
['The cartoon characters Minions are of what colour?',
  'A.Black','B.Yellow','C.Green','D.Pink','B','b'],
['What are cappuccino, espresso, latte and machiato types of?',
 'A.Tea','B.Coffee','C.Milk','D.Lemonade','B','b'],
['Which of these snakes is not venomous?',
 'A.Cobra','B.Common Krait','C.Anaconda','D.Python','D','d']
]

level1()
if count>=4:
    print('At the end of 8 questions you have scored',count,'points.Congrats you can now proceed to Level 2.Here is your first question...')
    print()
else:
    print('At the end of 8 questions you have scored',count,'points.To proceed to Level 2 you must score a minimum of 6 points.Thank you for playing!!')
    print()
    sql()
    sys.exit()

def level2():
    global count1
    global count
    qlist=[e[0],e[1],e[2],e[3],e[4],e[5],e[6],e[7],e[8],e[9],e[10],e[11],e[12],e[13]]
    for c in range(0,10):
        rand=(random.choice(qlist))
        del qlist[qlist.index(rand)]
        d=list(rand)
        print(d[0])
        print(d[1])
        print(d[2])
        print(d[3])
        print(d[4])
        print()
        ans=input("Answer:")
        if ans==d[5] or ans==d[6]:
            print('CORRECT ANSWER!!!')
            print()
            count1+=3
            print('You have a total of',count1,'points in this level.')
            print()
        else:
           print('WRONG ANSWER')
           print()
           count1=count1-1
           print('Sorry you lost one point.You have a total of',count1,'points in this level.')
           print('The right answer is',d[5])
           print()


e=[ 
['Which state is known as ‘The Empire State’?',
'A. Washington DC',' B.The New York City ','C. California State',' D.Chicago','B','b'],
 ['Which is the executive office and residence of the Korean President?',
'A.White House','B.Blue House','C.Golden House','D.Green House','B','b'],
 ['Grand Central Terminal, Park Avenue, New York is the',
'A.largest railway station','B.highest railway station','C.longest railway station','D.None of the above','A','a'],
['For which of the following disciplines is Nobel Prize awarded? ',
'A.Physics and Chemistry','B.Physiology and Medicine','C.Literature,Peace and Economics','D.All of the above','D','d'],
 ['Which country invented football ',
'A.England','B.USA','C.Africa','D.Germany','A','a'],
 ['Which place on earth is the coldest to live? ',
'A.Oymyakon-Russia','B.Antartica','C.Gobi desert','D.Ireland','A','a'],
 ['How many squares are there in the chessboard?',
'A.48','B.56','C.64','D.128','C','c'],
 ['Which blood type is known as the universal blood donor?',
'A.B-','B.O-','C.O+','D.A-','C','c'],
 ['Name two countries that allow taking a nap during work?',
'A.Italy and Spain','B.Australia and Austria','C.Mexico and Texas','D.America and France','A','a'],
 ['Which country developed the Skype software?',
'A.Estonia','B.Japan','C.Germany','D.USA','A','a'],
 ['Which country owns every panda in the world?',
'A.Russia','B.USA','C.China','D.Nepal','C','c'],
 ['Which fish will evaporate if left in the Sun?',
'A.Blowfish','B.Jellyfish','C.Goldfish','D.Catfish','B','b'],
 ['Which action burns more calories?',
'A.Watching TV','B.Sleeping','C.Talking','D.Writing','B','b'],
 ['What two letters never appear on the telephone? ',
'A.Q and K','B.Q and P','C.S and R','D.Q and Z','D','d'],
]

level2()
count+=count1
if count>=15:
    print('At the end of 10 qa you have scored',count1,'points.Congrats you can now proceed to Level 3.Here is your first question...')
    print()
else:
    print('At the end of 10 qa you have scored',count1,'points.To proceed to Level 3 you must score a minimum of 16 points.Thank you for playing!!')
    print()
    sql()
    sys.exit()


    
def level3():
    global count
    global count2
    qlist=[e[0],e[1],e[2],e[3],e[4],e[5],e[6],e[7],e[8],e[9],e[10],e[11],e[12],e[13],e[14]]
    for c in range(0,12):
        rand=(random.choice(qlist))
        del qlist[qlist.index(rand)]
        d=list(rand)
        print(d[0])
        print(d[1])
        print(d[2])
        print(d[3])
        print(d[4])
        print()
        ans=input("Answer:")
        if ans==d[5] or ans==d[6]:
            print('CORRECT ANSWER!!!')
            print()
            count2+=5
            print('You have a total of',count2,'points in this level.')
            print()
        else:
           print('WRONG ANSWER')
           print()
           count2=count2-1  
           print('Sorry you lost one point.You have a total of',count2,'points in this level.')
           print('The right answer is',d[5])
           print()

e=[
["The language spoken by people in Pakistan is ?",
"a.Hindi","b.Sindhi","c.Palaun","d.Naraun","B","b"],
["Which animal has three hearts?",
"a.Whale","b.Dolphin","c.Starfish","d.None of these","D","d"],
["Which country is Prague in?",
"a.Czech Republic","b.Croatia","c.Finland ","d.Guyana","A","a"],
["Who was the First Commander in Chief of the Kaurava Army?" ,
"a.Drona","b.Bheeshma","c.Karna","d.Ashvathama","B","b"],
["The language of Lakshadweep. a Union Territory of India, is",
"A.Tamil","B.Hindi","C.Malayalam","D.Telugu","A","a"],
["The western ghats in Maharashtra is known as...?", 
"a.Nilgiris","b.Sahyadri","c.Cardomom Hills","d.Anamalai Hills","B","b"],
["Researchers of which institute has designed a paper-based sensor to detect the quality of milk?",
"A.IIT Hyderabad","B.IIT Bombay","C.IIT Guwahati","D.IIT Delhi","C","c"],
["Which is the longest snake in the world?",
"a.Anaconda","b.Reticulated Python","c.Black Mamba","d.Puffer Adder","B","b"],
["How many bones are in the human adult body?",
"a.202","b.204","c.200","d.206","D","d"],
["Which of the following is radioactive?",
"a.Caesium","b.Germanium","c.Aluminium","d.Magnesium","A","a"],
["Who is the founder of AIADMK?",
"a.M.G.Ramachandran","b.Jayalalitha","c.Annadurai","d.None of the above","A","a"],
["What is the name of the disease that arises due to vitamin B1 deficiency?",
"a.Scurvy","b.Beribri","c.Pellagra","d.Gingivitis","B","b"],
["When did Gandhiji win the nobel peace prize?",
    "a.1937","b.1936","c.1939","d.Never","D","d"],
["When was Apollo 11 launched?",
"a.1968","b.1969","c.1869","d.1972","B","b"],
["Which one of the following artists was the first female with 2 million selling singles?",
"a.Whitney Houston","b.Celien Dion","c.Christina Augirela","d.Britney Spears","B","b"],]
level3()
count+=count2

if count>=30:
    print('At the end of 12 qa you have scored',count2,'points.Congrats you passed the level!!')
    print()
else:
    print('At the end of 12 qa levels you have scored',count2,'points.To win you have to score a minimum of 36 points.Thank you for playing!!')
    print()
    sql()
    sys.exit()





