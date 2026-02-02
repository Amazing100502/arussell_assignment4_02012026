def first_non_repeating_char(s):
    if not isinstance(s, str):
        return "Error: Input must be a string."

    if s == "":
        return None

    freq = {}  # dictionary to count characters

    for char in s:
        freq[char] = freq.get(char, 0) + 1

    for char in s:
        if freq[char] == 1:
            return char

    return None
print(first_non_repeating_char("aabbcdd"))   # c
print(first_non_repeating_char("aabb"))      # None
print(first_non_repeating_char(""))          # None
print(first_non_repeating_char(123))         # Error message
print(first_non_repeating_char("swiss"))     # w
