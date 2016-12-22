import numpy as np
numbers=np.arange(101)
# print(numbers)

finding_number=int(input('Please Enter the number between 0 and 100 to find the position\n'))
min=0
max=100

index=int((min+max)/2)
iteration=0
while finding_number != numbers[index]:
    iteration+=1
    index=int((min+max)/2)
    if(finding_number == numbers[index]):
        print('Iteration  : ' + str(iteration))
        print('The number was '+str(finding_number))

        break

    elif(finding_number < numbers[index]):
        max=numbers[index]

    elif (finding_number > numbers[index]):
         min= numbers[index]




