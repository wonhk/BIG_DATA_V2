# 황금알을 낳는 거위 프로그램
from goose import goldegg, money_eat

print('길을 가다가 거위를 만났습니다.')
print('먹이를 주면 안잡아 먹지~')
print('어떻게 할 것 인가?')
print('1. 먹이를 준다 2. 그냥 간다')
user = 1
egg = 0
# 만약에 1번 먹이를 주면 거위가 황금알을 낳는다
if user == 1:
    egg = goldegg()

# 돈을 주면 돈을 3배로 뻥튀기 해준다
mymoney = 3000
# print(f'내 돈은 {mymoney}원이 있다')
mymoney = money_eat()
# 내가 가진 돈도 보여주고 황금알도 확인 할 수 있게 해보자
print(f'황금알: {egg}, 내 돈: {mymoney}')