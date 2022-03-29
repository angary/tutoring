def generateNumber(i):
    return (i * (3 + i)) * (1 if i % 2 == 0 else -1)


def calc(m):
    retStr = ""

    nums = []
    for i in range(m):
        nums.append(generateNumber(i))

    middleIndex = int(m/2 - 0.5)
    middle = nums[middleIndex]

    retStr += "Middle item: "
    retStr += str(middle)
    retStr += "\n"

    min = 99999999
    max = -99999999

    for i in range(m):
        if nums[i] < min:
            min = nums[i]
        if nums[i] > max:
            max = nums[i]

    retStr += "Min item: "
    retStr += str(min)
    retStr += "\n"
    retStr += "Max item: "
    retStr += str(max)
    retStr += "\n"

    s = 0
    for i in range(m):
        s += nums[i]

    retStr += "Sum: "
    retStr += str(s)
    retStr += "\n"
    return retStr


if __name__ == '__main__':
    m = input()
    m = int(m)
    x = calc(m)
    print(x)
