def strip_comments(strng: str, markers: str):
    # flag and res string
    rm_flag: bool = False
    res_strng = ""

    # traverse thorugh the string
    for char in strng:
        if char == '\n':
            rm_flag = False
        elif char in markers:
            rm_flag = True
        
        if rm_flag == True:
            continue
        else:
            res_strng += char
    
    # remove whitespaces from res_strng
    res_strng = '\n'.join([line.rstrip() for line in res_strng.split('\n')])

    return res_strng

print(strip_comments('apples, pears # and bananas\ngrapes\nbananas !apples', ['#', '!']))