def save_file(lines):
    file_name = '计划' + str(count) + '.txt'
    project_file = open(file_name,'w')
    project_file.writelines(lines)
    project_file.close()

def split_file(file_name):
    f= open(file_name)

    global count
    lines = []
    count = 1

    for each_line in f:
        if each_line[:6] != '======':
            lines.append(each_line)
        else:
            save_file(lines)

            lines = []
            count +=1
            
    save_file(lines)

    f.close()
        
split_file('C:\\Users\\WXYZ\\Desktop\\桌面文档.txt')

