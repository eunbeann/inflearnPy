#리스트와 매우 유사
# 튜플 사용 법 : 선언, 특징, 슬라이싱, 함수, 팩킹언팩킹

#Chapter 03-4
#파이썬 튜플
#리스트와 비교 중요
# 튜플 자료형 (순서o, 중복o, 수정 x, 삭제x) #불변


#선언

a=() #소광호
b=(1,)
#원소가 하나 일 때는 ,로 끝나야지 튜플로 인식
c = ( 11, 12, 13, 14)
d = (100, 1000, 'Ace', 'Base', 'Captine')
e = (100, 1000, ('Ace', 'Base', 'Captine')) #튜플 안 튜플 가능

# 인덱싱 
print ('>>>>>')
print ('d - ', d[1])
print ('d - ', d[0] + d[1] +d[1])
print ('d - ', e[-1])
print ('d - ', e[-1][1])
print ('d - ', list(e[-1][1])) #리스트로 형 변환

# 수정X

#d[0] = 1500 #에러 발생 함

# 슬라이싱

print ('>>>>')
print('d=', d[0:3])
print('d=', d[2:])
print('e=', e[2][1:3])

#튜플 연산
print(">>>>>")
print('c+d', c + d) 
print('c*3', c * 3) 

#튜플 함수

a = (5, 2,3,1,4)
print('a -', a)
print('a - ', a.index(3))
print('a - ', a.count(2))

# 팩킹 & 언팩킹 (Packing and Unpacking)

# 팩킹
t = ('foo', 'bar', 'baz', 'qux') 

#묶어둔거라 인덱싱 가능함 / 튜플을 선언하는 거와 마찬가지
print (t)
print (t[0])
print (t[-1])

#언팩킹1 , 튜플을 풀어서 각각 할당해주는 것
(x1, x2,x3,x4) = t #괄호 없어도 언패킹 되긴하는디 관습상 괄호 ㄱㄱ
print(type(x1), type(x2), type(x3), type(x4))
print (x1, x2, x3, x4)

# 팩킹 & 언팩킹
t2 = (1, 2, 3)
t3 = 4, #괄호 생략가능해서 얘도 튜플
x1, x2, x3 = t2 #언팩킹
x4, x5, x6 = 4, 5, 6 #언패킹

print(t2)
print(t3)
print(x1, x2, x3)
print(x4, x5, x6)


# 튜플 사용 법
# 튜플 선언, 튜플 특징, 튜플 슬라이싱, 튜플 함수, 팩킹, 언팩킹



