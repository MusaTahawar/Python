import random
uppercase = "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"
symbols = "*", "&", "%", "$", "#", "@", "+", "-", "*", ",", ":", ""
lowercase = "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"
numbers = 1, 2, 3, 4, 5, 6, 7, 8, 9
result = []
for i in range(17):
    password_generator = random.choice(
        lowercase + uppercase + numbers + symbols)
    result.append(password_generator)
    musa = result
musa = ''.join(str(x) for x in result)
print(musa)
