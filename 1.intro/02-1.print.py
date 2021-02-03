#Chapter 02-1
#파이썬 완전 기초
#Print 사용법

print("Python Start!")
print('Python Start!')
print('''Python Start!''')
print("""Python Start!""")

print()

#separator 옵션

print('P', 'Y', 'T', 'H','O','N')

print('P', 'Y', 'T', 'H','O','N', sep='') #공백으로 분리되어있삼
print('P', 'Y', 'T', 'H','O','N', sep=',') #컴마로 분리되어 있삼
print('P', 'Y', 'T', 'H','O','N', sep="_")
print ('010', '7777', '8888', sep='-')#각 인수 파라미터로 

print()

#end 옵션 

print('welcome to', end=' ') #end옵션에 들어간 문자로 다음 프린트문에 이어줌
print('IT News', end=' ')
print('Web Site')

# file 옵션

import sys

print('Learn Python', file=sys.stdout) #현재 이 내용을 외부에 쓸거야
#sys.stdout은 콘솔에 보여주는 거 
print()

# 개중요! format 사용 (d(정수:3), s(문자열:'python'), f(실수'3.14')) 이건 기초

print('%s %s' % ('one', 'two')) #두 개를 대체할 수 있어 이건 정석
print('{} {}'.format('one', 'two')) #이건 매핑해줌 포맷함수가 알아처 처리해줌
print ('{1} {0}'.format('one','two')) #이건 순서 지정해서!
#복습해서 외워주세용


# %s

print('%10s' % ('nice'))
print('{:>10}' .format('nice')) #앞 칸 비우고 글자 채우기

print('%-10s' % ('nice')) 
print('{:10}' .format('nice')) #뒷 칸 비우고 글자 채우기

print('{:@>10}' .format('nice')) #빈자리 @자리에 들어가는 문자로 채우기
print('{:^10}' .format('nice')) #중앙정렬

print('%.5s' %('pythonstudy')) #다섯글자만 절삭 #점 없으면 다 들어옴!
print('{:10.5}'.format('pythonstudy')) #공간 열갠데 다섯개만 보이게!


# %d

print ('%d %d' % (1,2))
print ('{} {}' .format (1,2))

print('%4d' % (42))
print ('{:4d}'.format(42))

print()

# %f

print ('%f' %(3.1546153245621))
print ('%1.5f' %(3.1546153245621)) #%1.5 #%정수부,소수부
print ('{:f}'.format (3.1546153245621))

print ('%06.2f' % (3.141592653589793)) 
print ('{:06.2f}' .format (3.141592653589793)) 





