'''
    여러 줄
    주석.
'''

#파이썬이 제공하는 내장함수 목록
print("\n***** 파이썬이 제공하는 내장함수 목록출력 *****\n")
print(dir(__builtins__))

#내장함수 도움말 출력
#print(help(input))

import sys;
print("\n***** 파이썬 모듈 경로 출력 *****\n")

#v파이썬 모듈 경로 출력
print(sys.path)

import os;
print("\n***** 현재 작업 디렉터리 출력 *****\n")
print(os.getcwd())

print("\n***** 작업 디렉터리 이동 *****\n")
os.chdir('./tdfile') #작업 디렉터리 이동
print(os.getcwd())

os.chdir('../') #작업 디렉터리 이동
print(os.getcwd())
