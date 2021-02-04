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
