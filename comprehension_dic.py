def run():
    
    dict={i:i**2 for i in range(1,101) if i%2==0}
    list=[i for i in range(1,101) if i%2==0]
    
    
    print(dict)
    print()
    print(list)

if __name__== '__main__':
    run()