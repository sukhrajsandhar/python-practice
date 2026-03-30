def number_pattern(n):
    result = ""
    i = 0
    if type(n) is not int:
        return "Argument must be an integer value."
    if n < 1:
        return "Argument must be an integer greater than 0."

    for i in range(1, n + 1):
        result += str(i) + " "
    else:
        return result.strip()


print(number_pattern(12))
