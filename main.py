import matplotlib.pyplot as plt

seed = int(input('Insert the seed: '))

if (seed == 1):
    print('You entered 1, which is the end point for almost every number.')
elif (seed <= 0):
    print('This problem only applies to numbers greater or equal to 1.')
else:
    values = [seed]
    while (seed != 1):
        if (seed % 2 == 0):
            seed /= 2
        else:
            seed *= 3
            seed += 1
        
        values.append(seed)

    plt.plot(values, marker=".")
    plt.xlabel('Iterations')
    plt.ylabel('Values')
    plt.show()