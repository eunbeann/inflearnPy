#Chapter 03-5
# 파이썬 딕셔너리
# 범용적으로 가장 많이 사용(JSON)
# 딕셔너리 자료형 (순서x, 키 중복 x, 수정 ㅇ, 삭제 ㅇ)

# 선언 
a = {'name': 'Park', 'phone':'01000000000', 'birth':'020205'} #int str 모두 key 가능
b = {0: 'Hello Python'}
c = {'arr':[1,2,3,4]}
d = {
    'Name': 'Jisung',
    'City' : 'N',
    'Age' : '20',
    'Grade' : 'S',
    'Status': True
}
#FM
e = dict([
    ('Name', 'Jisung'),
    ('City', 'N'),
    ('Age', '20'),
    ('Grade', 'S'),
    ('Status', True)
])


f = dict (
    Name = 'Jisung',
    City = 'N',
    Age = 20,
    Grade = 'A',
    Status = True
)

#a = [f1,f2,f3] #리스트로 효율적으로 전체 학생 관리 가능
print('a =', type(a), a)
print('b =', type(b), b)
print('c =', type(c), c)
print('d =', type(d), d)
print('e =', type(e), e)
print('f =', type(f), f)

#출력
print('a-', a['name']) # 키가 존재 X 에러 발생
print('a-', a.get('name')) # 키가 존재 X None 처리
print('b-', b.get(0))
print('f-', f.get('City'))
print('f-', f.get('Age'))

# 딕셔너리 추가, 속성 값으로 접근해서 넣기
a['address'] = 'seoul'
print ('a-', a)
#원래 있는 값 추가하면 수정됨
a['rank'] = [1,2,3]
print ('a-', a)

#딕셔너리 길이

print('a =', len(a))
print('a =', len(b))
print('a =', len(c))
print('a =', len(d))

# dict_keys, dict_values, dict_items : 반복문 (__iter__)에서 사용 가능

#z키만 가져와
print ('a-', a.keys())
print ('b-', b.keys())
print ('c-', c.keys())
print ('d-', d.keys())
print ('a-', list(a.keys()))
print ('a-', list(b.keys()))

print()

#속성만 가져와
print ('a-', a.values())
print ('b-', b.values())
print ('c-', c.values())
print ('a-', list(a.values()))
print ('b-', list(b.values()))

print()

#키, 밸류 동시 출력
print('a-,', a.items())
print('b-,', b.items())
print('c-,', c.items())
print('a-,', list(a.items()))
print('b-,', list(b.items()))


print()
#pop 가능

print('a - ', a.pop('name'))
print('a-', a)

print('c - ', c.pop('arr'))
print('c - ', c)

print()

print('f-', f.popitem()) #아무거나 하나 임의로 꺼내 옴
print('f -', f) #해당 값 없어짐 #추첨기 만들때 사용 하면 돼 원본 데이터 삭제

print ()

#in 연산자, 키 포험 여부 조회

print('a-', 'birth' in a)
print('a-', 'City' in d)

# 쉊ㅇ

a ['test'] = 'test_dict'

print('a-', a)

a['address'] = 'dj'
print('a-', a)

#문법적으로 확실한 수정
a.update (birth='000323')
print('a-', a)
temp = {'address': 'Busan'}

a.update(temp)
print('a-', a)


'''
딕셔너리 사용 법
 - 딕셔너리 선언
 - 딕셔너리 특징
 - 딕셔너리 수정
 - 딕셔너리 함수
- 딕셔너리 중요성
'''