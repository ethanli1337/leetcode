def convert_zigzag(s,num_rows):
    if num_rows == 1 or num_rows >= len(s):
        return s 
    
    result=['']*num_rows
    cur_row=0
    go_down=False

    for char in s: 
        result[cur_row]+=char 
        if cur_row==0 or cur_row == num_rows-1:
            go_down=not go_down 
        cur_row+=1 if go_down else -1 


    return ''.join(result)

teststr="PAYPALISHIRING"

print(convert_zigzag(teststr,4))