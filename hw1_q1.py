def my_func(x1, x2, x3):
    if not all(isinstance(x, float) for x in (x1, x2, x3)):
        print("Error: parameters should be float")
        return None
    
    denominator = x1 + x2 + x3
    if denominator == 0:
        print("Not a number – denominator equals zero")
        return None
    
    result = ((x1 + x2 + x3) * (x2 + x3) * x3) / denominator
    return float(result)
