#Chapter 02-2
# 파이썬 완전 기초
# 파이썬 변수

# 기본 선언

n = 700 #n에 700을 할당

print (n)
print (type(n)) #타입 알려주기

# 동시 선언 가능

x = y= z = 700

print ( x,y,z)

#선언 
var = 75

#재선언

var = "change Value"

#출력

print(var)
print(type(var))

#Object reference 
# 뱐수 값 할당 상태
# 1. 타입에 맞는 오브젝트 생성
# 2. 값 생성
# 3. 콘솔 출력

# 예 1)
print(300)
print(int(300)) 

#예 2)
 
n = 777

print (n, type(n))

m = n

# m -> 777 <- n

print(m, n)
print (type(m), type(n))
print ()

m = 400


print(m, n)
print (type(m), type(n))
print ()


#id(identity 확인) (2-2 vkdlTKs)

m = 800
n = 600

print (id(m))
print (id(n))
print (id(m) == id(n))


# 같은 오브젝트 참조

m = 800
n = 800

print (id(m))
print (id(n))
print (id(m) == id(n))
print ()

# 재사용, 같은 값 사용하면 파이썬은 내부에서 하나만 만들어짐!

# 다양한 변수 선언
# Camel Case : numberOfColegeGraduates -> Method #추천!!
# Pascal Case : NumverOfCollegeGraduates -> Class
# Snake Case : number_of_college_graduates

studentGrade = 3

#허용하는 변수 선언 법

age =1 
Age = 1
aGe =1 
AGE = 1
a_g_e = 1
_age = 3
age_ = 2
_AGE_ = 8

#특수문자, 숫자로 시작하는 변수 안됨 

# 예약어는 변수명으로 불가능

# for, as , class 와 같은 것

'''
False def if raise
None del import return
True elif in try
and else is while
as except lambda with
assert finally nonlocal yield
break for not
class from or
continue global pass
'''
