from runPizzaBot import runpizzabot

def main():

    #Test case 1 : 
    input = '5x5 (0, 0) (1, 3) (4, 4) (4, 2) (4, 2) (0, 1) (3, 2) (2, 3) (4, 1)'

    output = runpizzabot(input)

    try:
        assert output == 'DNDENNDEEENDSSDDSDWNDWND'
        print ('Test Case 1 - OK')
    except:
        print ('Test Case 1 - Failed')
        print (' ')

    #Test case 2 - x coordinates not sorted:
    input = '5x5 (0, 0) (5, 5) (0,1)'

    output = runpizzabot(input)

    try:
        assert output == 'DNDEEEEENNNND'
        print ('Test Case 2 - OK')
    except:
        print ('Test Case 2 - Failed')
        print (' ')

    #Test case 3 - y coordinate not sorted
    input = '5x5 (0, 0) (1, 1) (1, 5) (1, 3) (1,2)'

    output = runpizzabot(input)

    try:
        assert output == 'DENDNNNNDSSDSD'
        print ('Test Case 3 - OK')
    except:
        print ('Test Case 3 - Failed')
        print (' ')

    #Test case 4 - missing coordinates
    input = '5x5'

    output = runpizzabot(input)

    try:
        assert output == ''
        print ('Test Case 4 - OK')
    except:
        print ('Test Case 4 - Failed')
        print (' ')

    #Test case 4 - missing coordinates
    input = '5x5 (6 , 3)'
    output = runpizzabot(input)

    try:
        assert output == ''
        print ('Test Case 5 - OK')
    except:
        print ('Test Case 5 - Failed')
        print (' ')

if __name__ == '__main__':

    main()