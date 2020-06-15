def string_letter_count(s):
    counter = {}
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
