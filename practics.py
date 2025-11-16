def generate_binary_strings(n):
    def helper(current, n, result):
        print(current)
        if len(current) == n:
            result.append(current)
            return
        helper(current + "0", n, result)
        helper(current + "1", n, result)

    result = []
    helper("", n, result)
    return result


# Example usage:
n = 3  # Length of binary strings
# binary_strings = generate_binary_strings(n)
# print(binary_strings)
print("Hellow world")
