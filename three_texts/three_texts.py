file_list = ['1.txt', '2.txt','3.txt' ]
new_file_list = ['new_1.txt', 'new_2.txt','new_3.txt' ]
intermediate_list = []

step = 0
while step < len(file_list):
    with open(file_list[step],encoding='UTF-8') as f:
        content = f.readlines()
        list_lengt = len(content)
    with open(file_list[step],encoding='UTF-8') as f:
        content_text = f.read()

    with open(new_file_list[step], 'w') as f:
        f.write(f'{file_list[step]}\n')
        f.write(f'{list_lengt}\n')
        f.write(f'{content_text}\n')
    step +=1

for number in new_file_list:
     with open(number) as f:
         new_content = f.read()
         intermediate_list.append(new_content)


sort_list = sorted(intermediate_list, key=len)
##print(sort_list)


with open('final_file.txt', 'a') as f:
    for part in sort_list:
        f.write(f'{part}')