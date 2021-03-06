# Chapter 03-2
# 파이썬 문자형
# 문자형 중요!

#문자열 생성

str1 = "I am Python"
str2 = 'Python'
str3 = """Jisung"""
str4 = '''JS'''

print (len(str1), len(str2), len(str3), len(str4) ) # 길이 구하기


# 빈 문자열

str1_t1 = ''
str2_t2 = str()

print (type(str1_t1), len(str1_t1))
print (type(str2_t2), len(str2_t2))

# 이스케이프 문자 사용 : 탈출 문자

''' 참고 : Escape code 

\n 개행
\t 탭
\\ 문자
\' 문자
\" 문자
\000 널 문자
...

'''
# I'm boy

print ("I'm Boy") # 작은 따옴표 안에 쓸거면 큰 따옴표 쓰기!
print ('I\'m boy')

print ('a \t b') # 탭키
print ('a \n b') # 줄바꿈
print ('a \"\" b')

escape_str1 = "Park Jisung \"튼튼하고\" "
print(escape_str1)

escape_str2 =  'What\'s on TV?'
print(escape_str2)

# 탭, 줄바꿈
t_s1 = "Click \t Start!"
t_s2 = "New Line \n Check!"

print(t_s1)
print(t_s2)

# Row STring 역 슬래쉬 있는 그대로 나오게 > 이스케이프 안쓰려고

raw_s = r'D:\Pyhton\test' 
print(raw_s)


#멀티라인 입력
multi_str = \
'''
Stirng
Multi Line
Test
'''
# """ 도 가능

print(multi_str)


# 문자열 연산 
str_o1 = "Park"
str_o2 = "Ji"
str_o3 = "Sung"
str_o4 = "NCTDREAM"

print(str_o1 * 3)

print (str_o1 + str_o2)
print ('k' in str_o1) #str_o1에 k 포함ㅂ되어 잇니?
print ("P" not in str_o2) #in 연산자 사용 가능

# 문자열 형 변환
print(str(66), type(str(66)))
print(str(10.1))
print(str(True), type(str(True)))

# 문자열 함수 (upper, isalnum, startswith, count, endswith, isalpha...)

print("Capitalize", str_o1.capitalize())
# 시작 글자 대문자로
print("endswith?", str_o2.endswith("e"))
#끝 글자가 e로 끝나는지 물어봄/ 마지막문자 체크할때 느낌표 마침표 가능
print("reaplce", str_o4.replace("REAM", "Good"))
# rEAM을 gOOOD으로 바꾸기
print("sorted: ", sorted(str_o1))
# 정렬해서 리스트 형태로 반환
print("split: ", str_o4.split(' '))
# 공백 기준 분리 / 느낌표 기준 분리헤사 리스트 형태로 반환


# 반복 (시퀀스) _ 슬라이싱 처리 가능 
im_str = "Good Boy!"
print(dir(im_str)) #__iter__ 가 존재하면 반복 가능

#출력
for i in im_str:
    print(i)

# 슬라이싱 연습 문자형 (2-3)

str_sl = "Nice Python"

#슬라이싱 연습

print (str_sl[0:3])  # 0 1 2
print (str_sl[5:]) # [5:11]
print (str_sl [:len(str_sl)]) # str_sl [:11] #끝 부분 모를 땐 len 쓰거나 비우기 
print (str_sl [:len(str_sl)-1]) # str_sl [:10] / 임의로 슬라이싱 처리 조정 가능
print (str_sl [1:9:2]) #세번째 단위는 몇개 단위로 스킴해서 가져올지
print(str_sl [-5:])
print (str_sl [1:-2])
print(str_sl[::2]) # 처음 부터 끝까지 두 칸 간격으로 점프하기
print (str_sl[::-1]) #처음부터 끝까지 반대 방향으로


# 아스키 코드 (또는 유니코드)

a = 'z'

print (ord(a)) # 알파벳을 아스키 코드로 보여줌
print (chr(122)) # 아스키 코드를 알파벳(문자)으로 보여줌 


# 문자형 사용법
# 문자형 중요성 . 문자형 출력, 이스케이프, 멀티 라인, 문자형 연산, 문자형 형변환, 인덱싱, 문자열 함쉬, 슬라이싱