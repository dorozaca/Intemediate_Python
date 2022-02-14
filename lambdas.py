
my_list=list(range(1,100))

my_list_prev=list(i**3 for i in my_list) #Para poder hacer el filtro sobre x**3 necesite hacer un paso previo
my_list_prev2=list(map(lambda x:x**3, my_list)) #ese mismo paso de arriba lo puedo obtenet pero con map

list1=list(filter(lambda x:x%2!=0, my_list_prev2)) #recien ahi aplico filter

list2=lambda x:x**3




print(list1)
print()
print(list2(9))