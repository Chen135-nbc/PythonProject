# - 使用bin()将十进制转为二进制
result1 = bin(25)

# - 使用oct()将十进制转为八进制
result2 = oct(540)

# - 使用hex()将十进制转为十六进制
result3 = hex(463)

print(result1)
print(result2)
print(result3)

# - 使用int()将指定进制的数，转为十进制数字
value1 = int('0b110011',2)
value2 = int('0o10342',8)
value3 = int('0x1cf6',16)
print(value1,value2,value3)

