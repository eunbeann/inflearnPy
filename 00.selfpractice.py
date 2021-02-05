# while 문 연습
'''while <조건문>:
    <수행할 문장1>
    <수행할 문장2>
    <수행할 문장3>
    ...'''

k = 0
while k < 20 :
    k = k+1
    print(k)

# while 예제 1) 1~100까지 짝수를 더하는 코드

i = 0
result1 = 0
while i<100 :
    i = i+1
    if i % 2 == 0 :
        result1 = result1 + i
print(result1)

#while 예제2) 구구단 4단~5단 출력

four = 0
while 