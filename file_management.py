def read():
    numbers=[]
    with open("./files/number.txt","r",encoding='utf-8') as f:
        for i in f:
            numbers.append(int(i))
        print(numbers)


def write():
    names=["Facundo", 'Paolo', 'Gianluca', 'Andre', 'Oreja', 'Benavente', 'Christian', 'Pena', 'Diego']
    with open('./files/names.txt','w',encoding='utf-8') as f:
        for i in names:
            f.write(i)
            f.write('\n')


def run():
    write()

if __name__== '__main__':
    run()