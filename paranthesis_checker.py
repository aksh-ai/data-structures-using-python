def check_paranthesis(my_string): 
    brackets = ["()", "{}", "[]"] 
    
    while any(x in my_string for x in brackets): 
        for br in brackets: 
            my_string = my_string.replace(br, '') 
    
    return not my_string 
   
expression = input("Enter the expression: ")

print("Balanced" if check_paranthesis(expression) else "Unbalanced")