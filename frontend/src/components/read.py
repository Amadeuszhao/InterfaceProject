file_name = 'UI_Content.md'
new_file = None
with open(file_name,'rb') as f:
    new_file =str(f.read())

with open('result.txt','w') as f:
    f.write(new_file)