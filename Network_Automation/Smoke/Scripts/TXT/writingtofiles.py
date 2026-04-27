# with open('myfile.txt', 'w') as f:  #'w' write mode
#     f.write('Just a line')
#     #f.write('Just a line')

with open('newdir/myfile.txt', 'a') as f:
    f.write('appending line\n')


with open('newdir/myfile.txt', 'r+') as f:
    f.write('line added with r+\n')