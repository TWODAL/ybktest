# 기본 모듈.
'''
   파이썬 함수 형식 ->

   def 함수이름 (인자):
       함수 코드 스위트
'''

# 리스트의 모든 요소들을 재귀적으로 출력.
def printList(a_list):
    for each_item in a_list:
        if isinstance(each_item, list):
            printList(each_item)
        else:
            print(each_item)

'''
    range() 내장 함수는 정해진 수를 나열합니다.
'''
def printNum(num):
    for i in range(num):
        print(i)
import sys
# 리스트의 모든 요소들을 level에 지정한 수 만큼 탭 들여쓰기로 재귀적으로 출력.
def printListTab(a_list,indent=False,level=0,fh=sys.stdout):
    for each_item in a_list:
        if isinstance(each_item, list):
            printListTab(each_item,indent,level+1, fh) # 들여쓰기 증가.
        else:
            if(indent):
                for l in range(level):
                    print("\t", end='',file=fh) # 라인을 바꾸지 않고 탭만 출력.
            print(each_item,file=fh)        # 탭 출력후 줄바꿈없이 바로 출력.
