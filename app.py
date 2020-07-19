import json 
import random as rdm

with open('data.json') as d :
    data = json.load(d)
 
#TODO - add save feature
#TODO - add specific test types (for always english question or always certain type of answer, etc)
#TODO - allow undoing one step when inputing characters rather than going back to start
#TODO - add exit() and back() and such by using a function to check. Maybe?    
#TODO - change radical to subchar? primitive maybe? not all do I remember with radicals, maybe elements would be best 

i = 0
while i<100  :
    valid1 = ['1','2','3','4'] 
    print('Test = 1, Input = 2, Update = 3, Lookup = 4')
    input1 = input() 
    if input1 not in valid1 :
        print('Error')
        continue
    input1 = int(input1)
    print('Type exit() at any time to go back')
    if input1 == 1 : 
        Ekeys = data['English'].keys() 
        Ckeys = data['Chinese'].keys() 
        if len(Ekeys) > 0 : 
            j = 0
            while j < 100 : 
                r = rdm.randint(1,2)
                if r == 1 :
                    r2 = rdm.randint(0,len(Ekeys))
                    print('Type the radical or character meanings of the following word : ' + data['English'][r2] )
                    input2 = input() 
                else :      
                    r2 = rdm.randint(0,len(Ckeys))
                    print('Type the meaning of the following character : ' + data['Chinese'][r2] )
                    input2 = input()
                j+= 1     
                    
    elif input1 == 2 :
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
                print(input5)
            data['English'][input3] = input2
            data['Chinese'][input2] = input3 
            data['Radicals'][input2] = input5
            print(data)
            with open('data.json','w') as file :  
                json.dump(data,file)     
    elif input1 == 3 :
        print(0)
    elif input1 == 4 : 
        print('Enter word, character or imagery ')      
    i += 1

with open('data.json','w') as file : 
    json.dump(data,file) 