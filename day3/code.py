import re

def sumValidMul(filePath):
    def parseMul(expression):
        pattern = r"mul\((\d{1,3}),(\d{1,3})\)"
        matches = re.findall(pattern, expression)

        return sum(int(x) * int(y) for x, y in matches)

    with open(filePath, "r") as file:
        data = file.read()

    return parseMul(data)

print(sumValidMul(r'C:\Users\x\Desktop\AoC\day3input.txt'))
