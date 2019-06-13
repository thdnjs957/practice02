# 문제1. 파이썬 경로명 s = '/usr/local/bin/python' 에서 각각의 디렉토리 경로명을 분리하여 출력하세요.
#‘usr’, ‘local’, ‘bin’, ‘python’
# ‘/usr/local/‘bin’, ‘python’
s = '/usr/local/bin/python'

a = s[1:].split('/')
result = ','.join(a)
print(result)

b = s.rsplit('/', 1) # 오른쪽에서 한개
result = ','.join(b)
print(result)



