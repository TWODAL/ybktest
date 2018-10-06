print("\n***** c_file_write.py *****\n")
man = []
other = []

try:
    data = open('sketch.txt')

    for each_line in data:
        try:
            (role, line_spoken) = each_line.split(':', 1)
            line_spoken = line_spoken.strip()
            if role == 'Man':
                man.append(line_spoken)
            elif role == 'Other Man':
                other.append(line_spoken)
        except ValueError:
            pass

    data.close()
except IOError as err:
    print('The datafile is missing!' + str(err))

try:
    # w는 쓰기 모드로 파일 열기, 기존파일이 있으면 삭제됨.
    man_file = open('man_data.txt', 'w')
    other_file = open('other_data.txt', 'w')

    print(man, file=man_file) # 데이터를 파일로 출력.
    print(other, file=other_file)
except IOError as err:
    print('File error.' + str(err))
finally:
    # 작업을 끝낸후에는 반드시 파일을 닫아야 캐시에 남아 있던 데이터도 실제 파일에 써집니다.
     man_file.close()
     other_file.close()

import basic
try:
    # with 문을 사용하면 파이썬 인터프리터가 파일을 자동으로 닫아 줍니다.
    with open('man_data2.txt', 'w') as man_file, open('other_data2.txt', 'w') as other_file:
        basic.printListTab(man,False, 0, man_file)
        print('\n')
        basic.printListTab(other,fh=other_file)
except IOError as err:
    print('File error: ' + str(err))

try:
    man_file = open('man_data2.txt')
    other_file = open('other_data2.txt')

    basic.printListTab(man) # 데이터를 파일로 출력.
    print('\n')
    basic.printListTab(other)
except IOError as err:
    print('File error.' + str(err))
finally:
    # 작업을 끝낸후에는 반드시 파일을 닫아야 캐시에 남아 있던 데이터도 실제 파일에 써집니다.
     man_file.close()
     other_file.close()

import pickle
try:
    # with 문을 사용하면 파이썬 인터프리터가 파일을 자동으로 닫아 줍니다.
    with open('man_data.pickle', 'wb') as man_file, open('other_data.pickle', 'wb') as other_file:
        pickle.dump(man,man_file)
        print('\n')
        pickle.dump(other,other_file)
except IOError as err:
    print('File error: ' + str(err))

print("\n***** pickle 데이터 출력 *****\n")
try:
    # with 문을 사용하면 파이썬 인터프리터가 파일을 자동으로 닫아 줍니다.
    with open('man_data.pickle', 'rb') as man_file, open('other_data.pickle', 'rb') as other_file:
        man = pickle.load(man_file)
        other = pickle.load(other_file)

        print(man)
        print('\n')
        print(other)
except IOError as err:
    print('File error: ' + str(err))
