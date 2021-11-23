import re
import sys

def runpizzabot(input):

    current = [0,0]
    deliverPizza = {}
    ordersPositions = []
    tableSize = []
    positions = []
    output = ''

    #set the variables for tablesize and possition from the input string
    tableSize = [int(i) for i in re.split('x',input[0:3]) if i != '']
    positions = [int(i) for i in re.split('[(),\s]',input[3:]) if i != '']

    #append the deliver pizza coordinates in a list
    for i in range(0,len(positions),2):
        ordersPositions.append([positions[i],positions[i+1]])

    #loop the order positions and set them as key - values pairs 
    for i in ordersPositions:
        if i[0] in deliverPizza:
            deliverPizza[i[0]].append(i[1])
        else:
            deliverPizza[i[0]] = [i[1]]

    #find the path
    for i in deliverPizza:
        if i > tableSize[0]:
            break

        while current[0] != i:
            if current[0] < i:
                output += 'E'
                current[0] += 1
            elif current[0] > i:
                output += 'W'
                current[0] -= 1

        for j in deliverPizza[i]:
            if j > tableSize[1]:
                break

            while current[1] != j:
                if current[1] < j:
                    output += 'N'
                    current[1] += 1
                elif current[1] > j:
                    output += 'S'
                    current[1] -= 1

            if current[1] in deliverPizza[i]:
                output += 'D'
                current[1] = j

    return output