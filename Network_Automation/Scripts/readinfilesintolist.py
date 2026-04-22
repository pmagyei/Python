with open('./newdir/configuration.txt') as f:
    content = f.read().splitlines()
    print(content)
print('#' * 50)

with open('./newdir/configuration.txt') as f:
    content = f.readlines()
    print(content)

with open('./newdir/configuration.txt') as f:
    print(f.readline(), end='')
    print(f.readline())