#Mathias-Nerd
#Week 10: Question 2
#Interleaving string validator

def is_interleave(s1, s2, s3, i=0, j=0):

    k = i + j
    #Base case
    if k == len(s3):
        return True

    if i < len(s1) and s3[k] == s1[i]:
        if is_interleave(s1, s2, s3, i + 1, j): 
            return True

    if s3[k] == s2[j]:
        res = is_interleave(s1, s2, s3, i, j + 1)
        if res: return res


    return False


s1 = "abc"
s2 = "def"
s3 = "adbcef"
print(is_interleave(s1, s2, s3))