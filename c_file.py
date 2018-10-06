print("\n***** c_file.py *****\n")
try:
    data = open('sketch.txt') # 파일을 엽니다.
	#print(type(data))
    for each_line in data:
        try:
            (role, line_spoken) = each_line.split(':',1)
            print(role, end='')
            print(' said ', end='')
            print(line_spoken, end='')
        except ValueError:
            pass

    data.close()
except IOError:
    print('The datafile is missing!') # 파일을 닫습니다.
