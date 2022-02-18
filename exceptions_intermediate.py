def palindrome(string):
    
    try:   # TRY: En el try se coloca código que esperamos que pueda lanzar algún error.
        way_around=list(reversed(string)) #We could've used string==string[::-1] instead
        way_around="".join(way_around)
    
    
        if string==way_around:   
            raise ValueError('error')               
            print('It is palindrome')
        else:
            print('It is not palindrome')

    except TypeError as e:
        print(f'{e}: Please enter strings only!')

    except ValueError as ve:
        print(f'{ve}: Can\'t enter empty string')
        

def run():
    palindrome('')
    

if __name__== '__main__':
    run()