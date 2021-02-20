# def fib(n):
#     cache = {}
#     if n == 0 or n == 1:
#         return n

#     else:
#         if n in cache:
#             return cache[n]
#         else:
#             cache[n] = fib(n-1) + fib(n-2)

#         return cache[n]

# print(fib(155))


















def no_dups(s):
    r = ""
    returns = ""
    counts = {}
    for c in s:
        # When the alg hits a space it adds the characters before to the hashtable 
        if c == ' ':
            counts[r] = True
            r = ""            
        # Otherwise, adds the character to the current string.
        else:
            r += c
    counts[r] = 1


    for key in counts:
        returns += ' ' + key

    return returns[1:]

def no_dups(s):

    lst_of_keys = []
    if s == '':
        # Return empty string if it is given
        return ''
    # Split string input into a list
    l = s.split(' ')
    # Turning array into dict as keys removes duplicates
    a = dict.fromkeys(l)
    for key in a.keys():
        # Loops keys and appends them to List of keys
        lst_of_keys.append(key)
        #Join it all for the return with a space between ' ' in order to maintain space distance
    return ' '.join(lst_of_keys)