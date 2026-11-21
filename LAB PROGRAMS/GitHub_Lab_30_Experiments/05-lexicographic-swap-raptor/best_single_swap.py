def best_swap(s):
    best = s
    chars = list(s)
    for i in range(len(chars)):
        for j in range(i + 1, len(chars)):
            chars[i], chars[j] = chars[j], chars[i]
            candidate = ''.join(chars)
            if candidate < best:
                best = candidate
            chars[i], chars[j] = chars[j], chars[i]
    return best

s = input("Enter string: ")
print("Smallest after at most one swap:", best_swap(s))
