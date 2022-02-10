from optparse import Values


def run():
    # my_list=[1,"Hello",True,4.5]
    # my_dict={"firstname":"Facundo","lastname":"Garcia"}

    # super_list=[
    #     {"firstname":"Facundo","lastname":"Garcia"},
    #     {"firstname":"Jose","lastname":"Tello"},
    #     {"firstname":"Enzo","lastname":"Perez"},
    #     {"firstname":"Eddy","lastname":"Roman"},
    #     {"firstname":"Diego","lastname":"Oroza"}
    # ]

    # super_diccionario={
    #     "natural_nums":[1,2,3,4,5],
    #     "integer_nums":[-1,-2,0,1,2],
    #     "floating_nums":[1.1,4.5,6.43]
    # }

    # for i, j in super_diccionario.items():
    #     print(f'{i} and {j}')

    my_list=list(range(1,101))
    my_list2=list(i**2 for i in my_list)
    print(my_list2)


if __name__== "__main__":
    run()