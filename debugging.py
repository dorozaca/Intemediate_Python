def divisors(num):
    divisors=[]
    
    try:
        if num<0:
                raise ValueError('We dont accept negative numbers here!')
                for i in range(1,num+1):
                    if num%i==0:          
                        divisors.append(i) 
            
                return divisors

    except ValueError as ve:
        print(f'{ve}: Be aware!')

def run():
    try:
        num=int(input('Ingresa un numero: '))
        print(divisors(num))
        print('Termino mi programa')

    except ValueError as ve:
        print(f'{ve} You should enter a number')

if __name__== '__main__':
    run()