# 1
"""answer = 0
for i in range(1, 1000000):
    answer += i

print(answer)"""


answer = 0
for i in range(1, 500):
    if i % 2 != 0: # Om det blir en rest som inte är noll = inte delbart med 2
        answer += i

print(answer)

