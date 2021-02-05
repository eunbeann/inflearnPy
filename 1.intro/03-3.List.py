# 배열, 리스트 리스트를 잘 써야 데이터 가져올 때 사요 가능
# 데이터 분석에 있어서는 필수적임.

#Chapter03-3
#파이썬 리스트
# 자료구조에서 중요함
### 리스트 자료형 (순서ㅇ, 중복ㅇ, 수정ㅇ, 삭제ㅇ)

# 선언
a = [] #빈 리스트 대괄호로 선언
#print(type(a))
b = list () #d이렇게도 선언 가능
c = [70, 75, 80, 85]
d = [1000, 10000, 'Ace', 'Base', 'Captine'] #서로 다른 자료형 선언 가능
e = [1000, 10000, ['Ace', 'Base', 'Captine']] # 리스트 안에 리스트 가능
f = [21.42, 'foobar', 3, 4, False, 3.14159]

#인덱싱
print('>>>>')
print('d-', type (d),d) # 타입이랑 리스트 보여주가
print('d-', d[1]) # 인덱스
print('d-', d[0]+d[1]+d[1]) # 인트형 저절로 계산해줌
print('d-', d[-1])
print('e-', e[-1][1]) #리스트 안에 있는 리스트 중 1번 인덱스
# 첫 리스트 접근 먼저 필요
print('e-', list(e[-1][1])) # 리스트 형변환해서 문자열은 시퀀스 하니까


#슬라이싱
print('>>>>')

print('d=', d[0:3])
print('d=', d[2:])
print('e=', (e[-1][1:3])) #e의 -1의 1~3까지 #리스트 슬라이싱함녀 리스트나deha

#리스트 연산의 결과는 리스트
print ('>>>>')
print ('c+d', c+d) #리스트 더하기 리스트는 리스트
print ('c*3', c*3) 
print ("'Test' + c[0]", 'Test' + str(c[0]))

# 값 비교 (리스트 3-5)

print (c == c[:3] + c[3:])
print(c)
print(c[:3] + c[3:])
print("")

# Identity (id)
temp =c 
print (temp, c)

print (id(temp))
print (id(c)) # 둘다 같은 Id를 갖고 있음! 둘 중 하나수정하면 둘 다 수정 됨~


#### 리스트 수정, 삭제
print('>>>>>')
c [0] = 4
print ('c -', c) #수정
c[1:2] = ['a', 'b', 'c'] #1부터 2는 2-1이니까  첫번쨰 인덱싱 번호인 75에 리스ㅡ가 들어감! 
print ('c-', c)
c[1] = ['a', 'b', 'c']
print ('c-', c)
c[1:2] = [['a', 'b', 'c']] # 이경우에는 리스트 자체가 들어감! 괄호 두 개 일 경우 
print ('c-', c)
# 슬러아상 범위 지정시 원소로 들어가고 숫자 지정하면 리스트가 중첩되어 들어감 
c[1:3] = [] # 1,2를 비워버림 / 삭제하기
print ('c-', c)
del c[2] #삭제
print ('c-', c)
print()

#리스트 함수

a=[5, 4, 1, 2, 3]
print ('a-', a)

a.append(10) #리스트 마지막에 데이터 삽입
print ('a-', a)

a.sort #오름차순 정렬
print ('a-', a)

a.reverse() #데이터를 역순으로 위치 구조 변경
print ('a-', a)
print ('a-', a.index(3), a[3]) # 인덱스로 가져올 때 두 가지 방법 가능

a.insert(2, 7) #두 번째 위치에 7을 삽입할래 나머지는 뒤로 밀림
#insert(위치, 추가할 값)

a.reverse()
print ('a-', a)

#del a[6]
#print ('a-', a)

a.remove(10) #제거할 인수 적으면 제거 됨
print ('a-', a)
print ('a-', a.pop()) # 기존 리스트에서 마지막 인덱스 원소를 꺼내고 나머지 리스트로 원소 재구성
print ('a-', a)
print ('a-', a.pop())
print ('a-', a) # 이거 스택! 마지막에 들어온 애가 가장 먼저 나감
#라스트인 퍼스트아웃 (LiFo) (FiFo은 큐)
print ('a-', a.count(4)) #4의 개수 몇 개 인지 알려줌
# 내가 찾는 값이 몇 개나 중복되어 있는지

ex = [8, 9]
a.extend(ex)
print ('a-', a) #두 개를 뒤에 붙이기 extend
print( )

#삭제 : romove(원소), pop(마지막), del (인덱스 번호)

# 반복문 활용
while a :
    data = a.pop()
    print(data) #빌 때 까지 반복 # 이거 다시 꼭 보기 이해 잘 안가니까


#### 리스트 사용 법
# 리스트 선언, 리스트 특징, 리스트 인덱싱, 리스트 슬라이싱, 리스트 함수, 리스트 사제










