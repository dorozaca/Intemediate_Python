def divisors(num):
    
    divisors=[]
       
    for i in range(1,num+1):
        if num%i==0:          
            divisors.append(i) 
    return divisors

    
def run():
    num=(input('Ingresa un numero: '))                    #Se quita el casteo a int 
    assert num[0]!='-','Needs to be a positive number'    #Assert para negativos
    assert num.isnumeric(),'Needs to be an integer'       #Aca no se usa type(num) porque recibiremos una string y queremos convertirla a int
                                                          #es distinto al caso de asserts.py en donde el parameter es string
    
    print(divisors(int(num)))                       #una vez que se confirma k el valor en #rico, tons casteamos antes de pasarlo   
    print('Termino mi programa')

if __name__== '__main__':
    run()