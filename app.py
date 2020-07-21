import json 
import os
import random as rdm
if not os.path.exists('./data.json'):
    t = {}
    with open('./data.json', 'w') as f : 
        json.dump(t,f)

with open('data.json') as d :
    data = json.load(d)

if 'English' not in data :
    data['English'] = {} 
if 'Chinese' not in data :
    data['Chinese'] = {} 
if 'Radicals' not in data :
    data['Radicals'] = {}     
if 'Elements' not in data :
    data['Elements'] = {} 
if 'rmc' not in data :
    data['rmc'] = {} 
if 'rme' not in data :
    data['rme'] = {}     
if 'update' not in data :
    data['update'] = []     


def loadtsv(address) : 
    print('Not finished yet')

    return 0

#the removed list shows the translation of what you want removed, not a huge issue but being able to view what you feel you've accomplished would be nice, so perhaps fixing it

#this doesn't work for python 2 due to string encoding issue (although maybe cause terminal defaults to python 3 and updated as unicode seemingly while 2 doesn't assume that'
#TODO - add ability to add back from removed list (after removed list added to test)
#TODO - ask at end of input if input is correct
#TODO - make sure inputs are in right format.  
#TODO - add in ability for multiple english meanings
#TODO - add save feature // temp backup so you can undo changes
#TODO - if you add an element that has sub elements, perhaps have it ask if that is the subelement? 
#TODO - add specific test types (for always english question or always certain type of answer, etc)
#TODO - allow undoing one step when inputing characters rather than going back to start
#TODO - add exit() and back() and such by using a function to check. Maybe?    
#TODO - change radical to subchar? primitive maybe? not all do I remember with radicals, maybe elements would be best 
#TODO - ability to lookup multiple terms at once (such as if you want to compare words), maybe create list of similar words for each word to help compare later? Might be useful if you add a gui later
#TODO - add in colors
#TODO - add in options command to see list of options rather than listing them each time (back, exit, main, etc)
#TODO - store list of changes made in update so you can revert
#TODO in lookup use c r and e keys to only look up given type ? not sure this is useful actually

def test() : 
    score = 0
    Ekeys = list(data['English'].keys()) 
    Ckeys = list(data['Chinese'].keys())  
    for x in Ekeys :
        if x in data['rme'] :
            Ekeys.remove(x)
    for x in Ckeys :
        if x in data['rmc'] :
            Ckeys.remove(x)
    if len(Ekeys) > 0 : 
        prev = ''
        while True : 
            print( (Ekeys), (Ckeys))
            temp = ''
            r = rdm.randint(1,2)
            if r == 1 :
                r2 = rdm.randint(0,len(Ekeys)-1) 
                temp = data['English'][Ekeys[r2]]
                print('Type the radical or character meanings of the following word : ' + temp )
                input2 =  input() 
                if input2 == 'rm' :
                    rm( Ekeys[r2],Ekeys,Ckeys,0) 
                    continue                
                if input2 == 'rmp' :
                    rm(prev,Ekeys,Ckeys,temp)
                    input2 = input()              
                prev = temp 
                if input2 == 'exit()' :
                    exit()
                if input2 == data['Chinese'][temp] :
                    print('correct, +1 score')
                    score += 1
                    print(temp,Ekeys[r2],data['Radicals'][temp] )  
                else :
                    print('correct answer : ' )
                    print(temp,Ekeys[r2],data['Radicals'][temp] ) 
            else :  
                r2 = rdm.randint(0,len(Ckeys)-1) 
                temp = data['Chinese'][Ckeys[r2]]
                print('Type the meaning of the following character : ' + temp )
                input2 = input() 
                if input2 == 'rm' :
                    rm( Ckeys[r2],Ekeys,Ckeys,0) 
                    continue
                if input2 == 'rmp' :
                    rm(prev,Ekeys,Ckeys,temp)
                    input2 = input()     
                prev =  temp
                if input2 == 'exit()' :
                    exit()
                if input2 == Ckeys[r2] :
                    print('correct, +1 score')
                    score += 1
                    print(Ckeys[r2],temp,data['Radicals'][Ckeys[r2]] )  
                else :
                    print('correct answer : ' )
                    print(Ckeys[r2],temp,data['Radicals'][Ckeys[r2]] ) 
            print('rmp - remove previous from testing, rm - remove current, update() - add to update list and remove from tests')


def question(arr,) : 
    r2 = rdm.randint(0,len(arr)-1) 
    print('Type the radical or character meanings of the following word : ' + temp )
    input2 =  input() 
    if input2 == 'rm' :
        rm( Ekeys[r2],Ekeys,Ckeys,0) 
        continue                
    if input2 == 'rmp' :
        rm(prev,Ekeys,Ckeys,temp)
        input2 = input()              
    prev = temp 
    if input2 == 'exit()' :
        exit()
    if input2 == data['Chinese'][temp] :
        print('correct, +1 score')
        score += 1
        print(temp,Ekeys[r2],data['Radicals'][temp] )  
    else :
        print('correct answer : ' )
        print(temp,Ekeys[r2],data['Radicals'][temp] ) 


def rm(pr,e,c,t) :
    if pr in e : 
        data['rme'][pr] = 1
        e.remove(pr) 
    elif pr in c : 
        data['rmc'][pr] = 1
        c.remove(pr)
    if t is not 0 :
        print('entry removed from test')
        print('Type the meaning of the following character : ' + t )
    with open('data.json','w') as file :  
        json.dump(data,file)  


def add() :
    while True : 
        print('Type a character or type bk to go back')
        input2 = input()
        if input2 == 'bk' :
            break 
        print('Type the chacters English meaning') 
        input3 = input()
        if input3 == 'bk' :
            break
        print('How many radicials does the character have?')
        valid2 = ['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20'] 
        input4 = input()
        if input4 == 'bk' :
            break
        elif input4 not in valid2 :
            print('Invalid input')
            continue
        input4 = int(input4)
        input5 = []
        for i in range( input4) :
            print('Input comma seperated Image list for radical ' + str(i+1) + ' :')
            if input5 == 'bk' :
                break
            temp = input().split(',' ) 

            input5.append( [k.strip() for k in temp] )   
        data['English'][input3] = input2
        data['Chinese'][input2] = input3 
        data['Radicals'][input2] = input5
        for j in input5 : 
            for r in j :
                if r in data['Elements'] :
                    data['Elements'][r].append(input2)
                else :
                    data['Elements'][r] = [input2]     
        with open('data.json','w') as file :  
            json.dump(data,file)  


#TODO - finish this, so it can actually update
def update() :
    print("Items added to the update list may be deleted or altered here")  
    print('Type shw to show update list, or type a character to or word to update it')
    ukeys = list(data['update'].keys())
    input2 = input()
    if input2 == 'shw' or input2 == 'Shw' :
        for i in range(len(ukeys)) :
            print(i + ' : ' + ukeys[i], data['Chinese'][ukeys[i]],data['Radicals'][ukeys[i]]) 
    elif input2 in data['Chinese'] :
        print(input2, data['Chinese'][input2],data['Radicals'][input2])  
        print('Type del to delete. ' )   
    elif input2 in data['English'] :
        print(data['English'][input2],input2,data['Radicals'][data['English'][input2]])        

def lookup() :
    while True : 
        print('Enter word, character or imagery. back() to return to previous, exit() to quit')  
        input2 = input()
        if input2 == 'back()' :
            break 
        if input2 == 'exit()' :
            exit()              
        if input2 in data['Chinese'] :
            print(input2,data['Chinese'][input2],data['Radicals'][input2])
        elif input2 in data['English'] or input2 in data['Elements']: 
            if input2 in data['English'] :
                temp = data['English'][input2]
                print(temp,data['Chinese'][temp],data['Radicals'][temp]) 
            if input2 in data['Elements'] : 
                for e in data['Elements'][input2] :
                    print(e,data['Chinese'][e],data['Radicals'][e]) 
        else :
            print('input not found in database')                  


#TODO - make into a loop
def load() : 
    print('Please provide file name in current folder') 
    input2 = input()
    if os.path.exists('./' + input2) :
        loadtsv('./' + input2)
        print('Table loaded')
    else : 
        print('No file with the given name was found')  



while True  :
    cmds = ['exit()','back()','prev()']
    valid1 = ['1','2','3','4','5'] 
    valid2 = [1,2,3,4,5]
    print('Test = 1, Input = 2, Update = 3, Lookup = 4, Load from file = 5')
    input1 = input() 
    if input1 not in valid1 and input1 not in valid2:
        print('Error')
        continue
    input1 = int(input1)
    print('Type exit() at any time to go back')
    if input1 == 1 : 
        test()
    elif input1 == 2 :
        add()
    elif input1 == 3 :
        update()
    elif input1 == 4 : 
        lookup()
    elif input1 == 5 :
        load()     