import re

string = "dfdf('':46%%^)"

# 使用正则表达式提取数字
numbers = re.findall(r'(\d+)', string)

# 转换为整数类型
numbers = [int(number) for number in numbers]

# 访问第一个数字
number = numbers[0]
print(number)
