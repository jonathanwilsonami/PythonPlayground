from collections import Counter


# Leetcode one-edit-distance
def one_away(word1, word2):
    if word1 == word2:
        return True
    else:
        if abs(len(word1) - len(word2)) > 1:
            return False
        else:
            A = Counter(word1) 
            B = Counter(word2)
            print(A)
            print(B)
            corr = 0
            for ch in A:
                if not B[ch]:
                    corr +=1
                else:
                    corr += abs(A[ch] - B[ch])
                if corr > 1:
                    print(corr)
                    return False
            return True

print(one_away("pale", "bake"))