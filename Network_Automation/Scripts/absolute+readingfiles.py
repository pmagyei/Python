

f = open('./newdir/configuration.txt', 'r')
# content = f.read(5)
# print(content)
# f.close()
# print(f.closed)


print(f.read())
f.seek(0)

print('#' * 50)
print(f.read())