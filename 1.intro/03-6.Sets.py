#Chapter 03-6
# 집합(Set) 특징
# 집합(Set) 자료형 (순서x, 중복x) 추가삭제는 가능

#선언
a = set()
b = set([1,2,3,4,4,4])
c = set([1,4,5,6])
d = set([1,2, 'ham', 'zzi', 'sung'])
e = {'foo', 'bar', 'baz'} #키 없으면 얘도 set
f = {42, 'foo', (1,2,3), 3.14159}
 # 중복 데이터 출력 안돼, in 연산자 가능~

print('a-', type(a), a)
print('b-', type(b), b)
print('c-', type(c), c)
print('d-', type(d), d)
print('e-', type(e), e)
print('f-', type(f), f)

#튜플 변환 (set > tuple)
t  = tuple(b)
print('t - ', type(t), t)
# 튜플로 바꿨으니까 슬라이싱 가능
print ('t-', t[0], t[1:3])


#리스트 변환 (set > list)
l=list(c)
l2 = list(e)

print ( 'l-', l)
print ( 'l2-', l2)

# 길이
print(len(a))
print(len(b))
print(len(c))
print(len(d))
print(len(e))
print(len(f))


# 집합 자료형 활용
s1 = set ([1,2,3,4,5,6])
s2 = set ([4,5,6,7,8,9])

  #교집합
print('s1 & s2: ', s1 & s2)
print('s1 & s2: ', s1.intersection(s2))

    #합집합
print('s1 | s2 : ', s1 | s2)
print('s1 | s2 : ', s1.union(s2))


    #차집합
print('s1 - s2 : ', s1 - s2)
print('s1 - s2 : ', s1.difference(s2))

    #중복 원소 확인

print('s1 & s2 : ', s1.isdisjoint(s2))
#결과가 False면 교집합 OO

# 부분 집합 확인
print ('부분집합확인 subset : ', s1.issubset(s2))
print ('부분집합확인  superset : ', s1.issuperset(s2))

# 추가 & 제거
s1 = set([1,2,3,4])

s1.add(5)
print('s1 -', s1)

s1.remove(2) # 이 때 존재하지 않는 값 삭제 시 에러 발생할 수 있음
print('s1 -', s1)

#지우고자하는 값이 있는지 체크 먼저하기
s1.discard(3)
print('s1 - ', s1) #여기는 예외 발생 X 에러 발생하지 않음

s1.clear()
print(s1) #전부 지움, 리스트도 clear로 삭제 가능

'''
집합 선언
집합 특징
집합 추가
집합 관련 함수
'''

