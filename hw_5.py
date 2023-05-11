
### Q2

def check_date(dateStr):
    if '/' in dateStr:
        day, month, year = dateStr.split('/')
    elif '.' in dateStr:
        day, month, year = dateStr.split('.')
    else:
        raise ValueError("Invalid date format")
        
    day, month, year = int(day), int(month), int(year)
    
    if not 1 <= month <= 12:
        raise ValueError("month out of range")
    
    days_in_month = [31, 29 if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0 else 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    
    if not 1 <= day <= days_in_month[month - 1]:
        raise ValueError("day out of range")
    
    return True

### Q3

def four_fibA(n):
    if n < 4:
        return n
    return four_fibA(n-1) + four_fibA(n-2) + four_fibA(n-3) + four_fibA(n-4)

def four_fibB(n, lookup=None):
    if lookup is None:
        lookup = {}
    if n < 4:
        return n
    if n not in lookup:
        lookup[n] = four_fibB(n-1, lookup) + four_fibB(n-2, lookup) + four_fibB(n-3, lookup) + four_fibB(n-4, lookup)
    return lookup[n]


### Q4

def climb_combinations(n, lookup=None):
    if lookup is None:
        lookup = {}
    if n <= 2:
        return n
    if n not in lookup:
        lookup[n] = climb_combinations(n-1, lookup) + climb_combinations(n-2, lookup)
    return lookup[n]
