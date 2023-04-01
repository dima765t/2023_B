f_path= '/Users/dimalevin/Desktop/Education/Y3_S2/data_sc/text.txt'

def revword(word:str):
    word= word.lower()[::-1]
    return word

def countword():
    with open(f_path, 'r') as file:
        lines = file.readlines()

    word = lines[0].strip()
    count = 1 

    for line in lines[1:]:
        words_in_line = line.strip().split()
        for w in words_in_line:
            if revword(w) == word:
                count += 1

    return count

countword()    
