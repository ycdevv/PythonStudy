# 달력 만들기
for i in range(24):
    for j in range(60):
        for k in range(60):
            print(f'{i:0>2} : {j:0>2} : {k:0>2}')

# test
# 01 02 03 04 05
# 06 ...
# 11 ...
# 16 17 18 19 20

for i in range(1, 21):
    print(f'{i:0>2}', end='')
    if i % 5 != 0:
        print(f'', end=', ')
    if i % 5 == 0:
        print()

# 01 02 03 04 05
# 10 ...
# 11 ...
# 20 19 18 17 16

row, col = map(int, input().split())
for i in range(row):
    if i % 2 == 0:
        for j in range(col):
            print(f'{i * col + 1 + j:0>2}', end=' ')
    else:
        for k in range(col - 1, -1, -1):
            print(f'{i * col + 1 + k:0>2}', end=' ')
    print()

# 섭씨 화씨 구하기
cTemp = float(input())
fTemp = cTemp * 1.8 + 32

print(f"섭씨: {cTemp}, 화씨: {fTemp}")

# 넓이 부피 구하기
PI = 3.141592
r = float(input())

ballVol = (r ** 3) * 4 / 3 * PI
ballArea = (r ** 2) * 4 * PI

print(f"구의 부피: {ballVol:.1f}, 구의 겉넓이: {ballArea:.1f}")
