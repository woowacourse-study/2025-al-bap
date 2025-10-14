# =============================================================
# 1. 수 자료형
# =============================================================

# 정수형
integer_value = 42

# 실수형
floating_value = 3.14

# 지수표현
one_billion = 1e9  # 1000000000.0

# 반올림
sum_value = 0.3 + 0.6
rounded_sum_to_4 = round(sum_value, 4)  # 0.9

# 나누기
division_result = 7 / 3

# 나머지
remainder_result = 7 % 3

# 몫
floor_division_result = 7 // 3

# 거듭제곱
power_result = 7 ** 3



# =============================================================
# 2. 리스트
# =============================================================

# 리스트 초기화
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# 빈 리스트 생성
empty_list = []
empty_list_alt = list()

# 인덱싱
fifth_value = numbers[4]      # 5
last_value = numbers[-1]      # 9

# 슬라이싱
slice_2_to_4 = numbers[1:4]   # [2,3,4]

# 리스트 컴프리헨션
odds_under_20 = [i for i in range(20) if i % 2 == 1]
squares_1_to_9 = [i * i for i in range(1, 10)]

# 2차원 리스트
rows, cols = 3, 4
matrix = [[0] * cols for _ in range(rows)]



# =============================================================
# 3. 리스트 메서드
# =============================================================

# append()
work_list = [1, 4, 3]
work_list.append(2)              # [1,4,3,2]

# sort()
work_list.sort()                 # [1,2,3,4]

# reverse()
work_list.reverse()              # [4,3,2,1]

# insert()
work_list.insert(2, 3)           # [4,3,3,2,1]

# count()
count_of_three = work_list.count(3)

# remove()
work_list.remove(4)              # 첫 4 하나 삭제

# 특정 값 삭제 (remove_set)
source_values = [1, 2, 3, 4, 5, 5, 5]
remove_set = {3, 5}
filtered_values = [v for v in source_values if v not in remove_set]  # [1,2,4]



# =============================================================
# 4. 문자열
# =============================================================

# 문자열 초기화
hello = "Hello"
world = "World"

# 문자열 더하기
hello_world = hello + " " + world

# 문자열 곱하기
hello_triple = hello * 3

# 문자열 슬라이싱
letters = "ABCDEF"
slice_cd = letters[2:4]  # "CD"



# =============================================================
# 5. 튜플
# =============================================================

# 튜플 생성
immutable_tuple = (1, 2, 3, 4)

# 튜플 인덱싱
third_in_tuple = immutable_tuple[2]  # 3



# =============================================================
# 6. 사전
# =============================================================

# 사전 생성
k2e = {}
k2e["사과"] = "Apple"
k2e["바나나"] = "Banana"
k2e["코코넛"] = "Coconut"

# 키 존재 여부 확인
has_apple = "사과" in k2e

# keys()
only_keys = k2e.keys()

# values()
only_values = k2e.values()



# =============================================================
# 7. 집합
# =============================================================

# 집합 생성
set_a = {1, 2, 3, 4, 5}
set_b = {3, 4, 5, 6, 7}

# 합집합
union_ab = set_a | set_b

# 교집합
intersect_ab = set_a & set_b

# 차집합
diff_ab = set_a - set_b

# add()
mutable_set = {1, 2, 3}
mutable_set.add(4)

# update()
mutable_set.update([5, 6])

# remove()
mutable_set.remove(3)



# =============================================================
# 8. 조건문
# =============================================================

# if
score = 85
if_result = None
if score >= 80:
    if_result = "Success"
elif score >= 60:
    if_result = "Retry"
else:
    if_result = "Fail"

# elif
# (위 블록에 이미 포함되어 있음)

# else
# (위 블록에 이미 포함되어 있음)

# 조건부 표현식
cond_expr_result = "Success" if score >= 80 else "Fail"

# 3항 연산자
and_or_result = (score >= 80 and "Success") or "Fail"



# =============================================================
# 9. 반복문
# =============================================================

# while
total_while = 0
i = 1
while i <= 9:
    total_while += i
    i += 1

# for
total_for = 0
for j in range(1, 10):
    total_for += j

# continue
passed_indices = []
scores = [90, 85, 77, 65, 97]
cheating = {2, 4}
for idx in range(5):
    if (idx + 1) in cheating:
        continue
    if scores[idx] >= 80:
        passed_indices.append(idx + 1)

# break
first_under_70 = None
for s in scores:
    if s < 70:
        first_under_70 = s
        break

# 중첩 for문
gugudan = []
for a in range(2, 10):
    for b in range(1, 10):
        gugudan.append(f"{a} X {b} = {a*b}")
    gugudan.append("")  # 줄바꿈 용



# =============================================================
# 10. 함수 / global / 람다
# =============================================================

# 함수 정의
def add_numbers(left: int, right: int) -> int:
    return left + right

# 함수 호출
sum_direct = add_numbers(3, 7)
sum_by_keyword = add_numbers(left=3, right=7)

# global 변수
global_counter = 0
def increase_global_counter() -> None:
    global global_counter
    global_counter += 1

for _ in range(10):
    increase_global_counter()

# 람다 표현식
lambda_sum = (lambda a, b: a + b)(3, 7)



# =============================================================
# 11. 주요 라이브러리
# =============================================================

# itertools
from itertools import permutations, combinations, product, combinations_with_replacement
iter_data = ["a", "b", "c"]
perm_len3 = list(permutations(iter_data, 3))
comb_len2 = list(combinations(iter_data, 2))
prod_rep2 = list(product(iter_data, repeat=2))
comb_wr_len2 = list(combinations_with_replacement(iter_data, 2))

# heapq
import heapq

def heapsort_min(iterable):
    h = []
    for v in iterable:
        heapq.heappush(h, v)
    result = []
    for _ in range(len(h)):
        result.append(heapq.heappop(h))
    return result

def heapsort_max(iterable):
    h = []
    for v in iterable:
        heapq.heappush(h, -v)
    result = []
    for _ in range(len(h)):
        result.append(-heapq.heappop(h))
    return result

# bisect
from bisect import bisect_left, bisect_right
sorted_list = [1, 2, 4, 4, 8]
idx_left_4 = bisect_left(sorted_list, 4)   # 2
idx_right_4 = bisect_right(sorted_list, 4) # 4

def count_by_range(a, left_value, right_value):
    right_idx = bisect_right(a, right_value)
    left_idx = bisect_left(a, left_value)
    return right_idx - left_idx

# collections
from collections import deque, Counter
dq = deque([2, 3, 4])
dq.appendleft(1)
dq.append(5)
dq.pop()
dq.popleft()
dq_as_list = list(dq)  # [2,3,4]

counter = Counter(["red", "blue", "green", "blue", "blue"])
count_blue = counter["blue"]
counter_as_dict = dict(counter)

# math
import math
five_fact = math.factorial(5)
sqrt_seven = math.sqrt(7)
gcd_21_14 = math.gcd(21, 14)
pi_value = math.pi
e_value = math.e
