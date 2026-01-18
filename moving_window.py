def len_longest_substr(str):
    char_set=set()
    left=0
    max_len=0 

    for right in range(len(str)):
        while str[right] in char_set:
            char_set.remove(str[left])
            left+=1
        char_set.add(str[right])
        max_len=max(max_len,right-left+1)

    return max_len 

letters="pwwkew"

print(len_longest_substr(letters))

