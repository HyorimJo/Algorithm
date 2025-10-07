# 길이순 -> 알파벳순, 중복 제거
n = int(input())

words = []
for i in range(n):
    words.append(input())

words = list(set(words)) #중복제거
words = sorted(words, key = lambda x : (len(x),x)) #lambda를 쓰면 한 번에 할 수 있구나
print(*words, sep='\n') 