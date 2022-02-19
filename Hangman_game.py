import random
import os

def opening_file():
    words=[]
    with open('./data.txt','r',encoding='utf-8') as f:  #keyword is "encoding"
        for i in f:
            words.append(i.strip('\n'))                 #removing '\n' from strings with strip

    return words  



def select_word(list):
    target_word=[]
    container=random.choice(list)      
    
    counter=len(container)
    i=0
    while i<=(counter-1):
        target_word.append(container[i])
        i+=1
                        
    return target_word



def guessing(target_word):
    
    #print(target_word)                                  #para ver el target
    counter=len(target_word)
    
    hiding=[]
    i=0 
    while i<=counter-1:
        hiding.append('-')
        i+=1
                                        
    hiding_provisonal = "".join(hiding)
    print(hiding_provisonal.replace(""," "))      #para ver el hiding inicial como en Platzi - Mejorar
    print()
       
    list_numbered=list(enumerate(target_word)) #IMPORTANTE: No te olvides que enumerate necesita LIST
    
      
    while hiding != target_word:
        char_guesser=input('Enter a letter: ')
        for i in list_numbered:
            if i[1] == char_guesser:
                hiding[i[0]]=i[1]

               
        os.system('clear')
        hiding_converted_string = "".join(hiding)
        hiding_converted_string = hiding_converted_string.upper() #no olvidarse del () al final del upper
        print('Guess the word!')
        print(hiding_converted_string.replace(""," "))   #How to add spaces within a string
        print()
    
    print('****** You Guessed it! ******\n')    #como usar \n dentro de string
    
    

def run():
    
    target_word=select_word(opening_file())
    print('Guess the word!')
    guessing(target_word)
    
    

if __name__== '__main__':
    run()
