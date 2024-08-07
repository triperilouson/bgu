with open('output.txt', 'w', encoding='utf-8') as file:
    file.write("(9))(")
def is_balanced(s):
    stack = []
    brackets = {')': '(', ']': '[', '}': '{', '>': '<'}

    for char in s:
        if char in brackets.values():
            stack.append(char)
        elif char in brackets.keys():
            if stack == [] or brackets[char] != stack.pop():
                return False
    return stack == []


def check_balanced_in_file(input_file, output_file):
    results = []

    with open(input_file, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    for line in lines:
        line = line.strip()
        if is_balanced(line):
            results.append("true")
        else:
            results.append("false")

    with open(output_file, 'w', encoding='utf-8') as file:
        file.write("\n".join(results))

input_file = 'output.txt'
output_file = 'output.txt'
try:
    check_balanced_in_file(input_file, output_file)
except Exception as e:
    print(f'{e}')
def two():

    def evclid_reverse(a=1, b=0):
        if b == 0:
            return a
        else:
            a, b = b, a % b
            return evclid_reverse(a,b)
    while True:
        try:
            a = int(input('a'))
            b = int(input('b'))
        except Exception as e:
            print(f"{e}")
    evclid_reverse(a, b)
#two()