#%%
import re
# myinput=input()
# Allowed *, /, +, -, %
# while myinput != 'exit':

def get_side_value(side):
    """
    Get final value for each side of calculator
    """
    side_clean=re.split('&',side)
    if len(side_clean)==2:
        print('detected whole number and fractions')
        side_clean_fractions=re.split('/',side_clean[1])
        print(f'Side Fractions after `&` {side_clean_fractions}')
        side_clean_fractions_value=int(side_clean_fractions[0])/int(side_clean_fractions[1])
        print(f'Side Fractions after `&` as number {side_clean_fractions_value}')
        final_side_value=int(side_clean[0])+side_clean_fractions_value
        print(f'Side Final Number:  {final_side_value}')
    else:
        print('No `&` detected...must be either fraction or whole number only')
        #Check if value is fraction:
        side_clean_fractions=re.split('/',side_clean[0])
        if len(side_clean_fractions)==2:
            print('Must have a fraction since able to split... this is now the final value on this side')
            final_side_value=int(side_clean_fractions[0])/int(side_clean_fractions[1])
            print(f'Side Final Number: {final_side_value}')
        else:
            print('Must have whole number')
            final_side_value=int(side_clean_fractions[0])
            print(f'Side Final Number: {final_side_value}')
    return final_side_value


def doSomethingCalculator(left_side_value,doSomething,right_side_value ):
    """
    Apply calculator on both sides to get final output
    """
    if doSomething=='*':
        final_number=left_side_value*right_side_value
        print(f'Multipied {left_side_value} * {right_side_value} = {final_number} ')
    elif doSomething=='/':
        final_number=left_side_value/right_side_value
        print(f'Divided {left_side_value} / {right_side_value} = {final_number} ')
    elif doSomething=='%':
        final_number=left_side_value%right_side_value
        print(f'Mode {left_side_value} % {right_side_value} = {final_number} ')
    elif doSomething=='+':
        final_number=left_side_value+right_side_value
        print(f'Added {left_side_value} + {right_side_value} = {final_number} ')
    elif doSomething=='-':
        final_number=left_side_value-right_side_value
        print(f'Subtracted {left_side_value} - {right_side_value} = {final_number} ')
    else:
        print('doSomething is not correct: {doSomething}')
        final_number=None
    return final_number

def calculator_execute(calculator_str):
    """
    Execute and put everything together to receive a str as input.
    """
    split_input=re.split('\s(\*|\+|-|%|/)\s',calculator_str)
    print(split_input)
    left_side=split_input[0]
    doSomething=split_input[1]
    right_side=split_input[2]

    #get actual values for both sides
    left_side_value=get_side_value(left_side)
    right_side_value=get_side_value(right_side)

    #Do something to provide final answer
    result=doSomethingCalculator(left_side_value,doSomething,right_side_value)
    print(f'Your final Value is: {result}')
    return result


#%%
if __name__=="__main__":
    print('Enter calculator ..ex (1/2 * 3&3/4):')
    #THIS WILL BE INPUT() function... in while loop...
    myinput='1/2 * 3&3/4'
    myinput='1/2 / 3&3/4'
    myinput='11 % 3'
    #myinput='1/2 * 3/4'
    #myinput='1/2 + 3&3/4'
    #myinput='1/2 - 3&3/4'
    #get user input
    
    while True:
        calculator_str = input("Enter Input ")
        
        if calculator_str == "exit":
            #name = True
            print("Good bye")
            break

        else:
            print(calculator_execute(calculator_str))
            print("Try again")
            

    
    


