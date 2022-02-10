def run():

    # nums=[]
    # for i in range(1,101):
    #     if i%3 != 0:
    #         nums.append(i**2)

    nums=list(i for i in range(1,101) if i%3 != 0)

    print(nums)
if __name__== '__main__':
    run()