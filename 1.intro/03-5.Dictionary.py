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
print('f-', f.get('Name'))