def generate_number(i):
    return (i * (3 + i)) * (1 if i % 2 == 0 else -1)


def calc(m):
    nums = [generate_number(i) for i in range(m)]
    print(nums)

    middleIndex = m // 2
    middle = nums[middleIndex]

    list_min = min(nums)
    list_max = max(nums)
    s = sum(nums)
    
    ret_str = f"""
Middle item: {middle}
Min item: {list_min}
Max item: {list_max}
Sum: {s}
"""
    return ret_str


if __name__ == '__main__':
    print(calc(int(input())))
