# def scrabble_score(st):
#     print(sum(scrabble_score.get(c, 0) for c in st.upper()))
    

# scrabble_score("Street")


# nth power rules them all
# def modified_sum(a, n):
#     xyz = (sum(i**n for i in a)-sum(j for j in a))
#     print(xyz)


# modified_sum([1, 2, 3], 3)



# 


def string_letter_count(s):
    counter = {}
    # alphabets = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L",
    #              "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "z"]
    alphabets = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t",
                 "u", "v", "w", "x", "y", "z"]
    lowering = s.lower()
    listing = tuple(lowering)
    sorting = sorted(lowering)
    for al in alphabets:
        for key in sorting:
            if key in counter:
                if key != al:
                    pass
                else:
                    counter[key] += 1
            else:
                if key != al:
                    pass
                else:
                    counter[key] = 1

    if not counter:
        return ""

    for x, y in counter.items():
        result = "".join(f"{y}{x}" for x, y in counter.items())
        return result
        return



string_letter_count("./4592#{}()")
