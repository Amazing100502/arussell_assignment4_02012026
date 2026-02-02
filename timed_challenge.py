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

"""
Reflection (Timed Challenge – 30 Minutes)

For this timed challenge, I chose to use a dictionary as my primary data structure. 
The problem required identifying the first non-repeating character in a string, 
and a dictionary allowed me to count character frequencies in O(n) time while 
still being able to check order efficiently. This structure was ideal because it 
balances speed and clarity, and it avoids unnecessary nested loops that would slow 
down the solution.

The 30-minute time limit definitely shaped my decision-making. Instead of exploring 
multiple possible approaches, I focused on the most reliable and familiar method. 
I prioritized writing a solution that was simple, readable, and guaranteed to work 
within the time constraint. The time pressure also pushed me to avoid overthinking 
edge cases until after the main logic was complete.

There were a few trade-offs I had to accept. I didn’t spend time optimizing memory 
usage or experimenting with alternative structures like OrderedDict or queues. 
I also chose not to implement additional validation beyond basic type checking 
because I needed to ensure the core algorithm was correct first. Overall, the 
challenge reinforced the importance of balancing correctness, efficiency, and 
speed """ 
