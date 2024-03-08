

"""
All functions work the same way. First, they check whether the list is empty. Then, they check whether 
# there are non-numerical values and raise error specifying the first non-numerical value they detect. 
# If the list is not empty and all values in the list are int or float, they perform the calculation.
"""



def sumvalues(values):
    """
    Calculate the sum of the values in the list.
    
    Parameters:
    values (list of int/float): The list of numbers.

    Returns:
    int/float: The sum of all values in the list.

    Raises:
    ValueError: If the list is empty or contains non-numerical values.
    """
    
    if len(values) == 0:
        raise ValueError("The input list is empty, this operation cannot be performed.")

    for v in values:
        if not isinstance(v, (int, float)):
            raise ValueError(f"Non-numerical value presented: {v}. Please make sure all items in your list/array are int and float.")
            
    sumV = sum(values)
    print("The summary of your input is: " + str(sumV))
    return(sumV)
        


def maxvalue(values):
    """
    Find the maximum value in the list.
    
    Parameters:
    values (list of int/float): The list of numbers.

    Returns:
    int/float: The maximum value in the list.

    Raises:
    ValueError: If the list is empty or contains non-numerical values.
    """

    if len(values) == 0:
        raise ValueError("The input list is empty, this operation cannot be performed.")

    for v in values:
        if not isinstance(v, (int, float)):
            raise ValueError(f"Non-numerical value presented: {v}. Please make sure all items in your list/array are int and float.")

    maxV = max(values)
    print("The mamximum value amongst your input is: " + str(maxV))
    return(maxV)



def minvalue(values):
    """
    Find the minimum value in the list.
    
    Parameters:
    values (list of int/float): The list of numbers.

    Returns:
    int/float: The minimum value in the list.

    Raises:
    ValueError: If the list is empty or contains non-numerical values.
    """

    if len(values) == 0:
        raise ValueError("The input list is empty, this operation cannot be performed.")

    for v in values:
        if not isinstance(v, (int, float)):
            raise ValueError(f"Non-numerical value presented: {v}. Please make sure all items in your list/array are int and float.")

    minV = min(values)
    print("The minimum value amongst your input is: " + str(minV))
    return(minV)



def meanvalue(values):
    """
    Calculate the mean of the values in the list.
    
    Parameters:
    values (list of int/float): The list of numbers.

    Returns:
    float: The mean of all values in the list.

    Raises:
    ValueError: If the list is empty or contains non-numerical values.
    """

    if len(values) == 0:
        raise ValueError("The input list is empty, this operation cannot be performed.")

    for v in values:
        if not isinstance(v, (int, float)):
            raise ValueError(f"Non-numerical value presented: {v}. Please make sure all items in your list/array are int and float.")

    meanV = sum(values)/len(values)
    print("The average of your input is: " + str(meanV))
    return(meanV)



def countvalue(values, xw):
    """
    Count the occurrences of a value in the list.
    
    Parameters:
    values (list of int/float): The list of numbers.
    xw (int/float): The number to count occurrences of.

    Returns:
    int: The count of the number in the list.

    Raises:
    ValueError: If the list is empty or contains non-numerical values.
    """

    if len(values) == 0:
        raise ValueError("The input list is empty, this operation cannot be performed.")

    for v in values:
        if not isinstance(v, (int, float)):
            raise ValueError(f"Non-numerical value presented: {v}. Please make sure all items in your list/array are int and float.")

    countV = values.count(xw)
    print(str(xw) + " appears " + str(countV) + " times in the list/array")
    return(countV)





