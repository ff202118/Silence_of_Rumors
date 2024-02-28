# from pulp import LpVariable, LpProblem, lpSum, value, LpInteger, LpMaximize
#
# # 创建线性规划问题
# prob = LpProblem("Equations", LpMaximize)
#
# # 创建变量
# x1 = LpVariable("x1", lowBound=0, upBound=95, cat=LpInteger)
# x2 = LpVariable("x1", lowBound=0, upBound=95, cat=LpInteger)
# x3 = LpVariable("x3", lowBound=0, upBound=95, cat=LpInteger)
# x4 = LpVariable("x4", lowBound=0, upBound=95, cat=LpInteger)
#
# # 添加目标函数
# prob += 0  # 由于是等式，目标函数为0
#
# # 添加方程
# prob += x1 + x2 + x3 + x4 + 95 + 88 == 545
# prob += x1 * 0.25 + x2 * 3 + x3 * 3.5 + x4 * 3 + 95 + 88 * 2 == 1163.250075
# prob += (0.1 * x1 - 4.5) * 0.25 + (0.1 * x2 - 4.5) * 3 + (0.1 * x3 - 4.5) * 3.5 + (0.1 * x4 - 4.5) * 3 == 43.949675
# prob += (0.1 * x1 - 4.5) + (0.1 * x2 - 4.5) + (0.1 * x3 - 4.5) + (0.1 * x4 - 4.5) == 17.8002
#
# # 求解问题
# prob.solve()
#
# # 打印结果
# print("Status:", prob.status)
# print("Solution (x1, x2, x3, x4):", value(x1), value(x2), value(x3), value(x4))

x1 = 89
x2 = 87
x3 = 95
x4 = 91

print(x1 + x2 + x3 + x4 + 95, 457)
print(x1 * 0.25 + x2 * 3 + x3 * 3.5 + x4 * 3 + 85, 987.250075)

if x3 >= 95:
    a = 5
else:
    a = 0.1 * x3 - 4.5

if x4 >= 95:
    b = 5
else:
    b = 0.1 * x4 - 4.5

print( (0.1 * x1 - 4.5) * 0.25 + (0.1 * x2 - 4.5) * 3 + a * 3.5 + b * 3, 43.949675)
print( (0.1 * x1 - 4.5) + (0.1 * x2 - 4.5) + a + b, 17.8002)