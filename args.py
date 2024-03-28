def my_function(*nums):
    num=int(nums[0])
    for i in range(1,num+1):
        print(nums[i])

my_function("2", "3 2 1", "5 6 7")
