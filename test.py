# 函数
def my_abs(x):
	if not isinstance(x,(float,int)):
		raise TypeError('bad operand type')
	if x >= 0:
		return x
	else:
		return -x


print(my_abs(-11))

import math

def move(x, y, step, angle = 0):
	nx = x + step * math.cos(angle)
	ny = y - step * math.sin(angle)
	return nx, ny

x, y = move(100, 100, 60, math.pi / 6)
print(x, y)

# 解一元二次方程

import math

def quadratic(a, b, c):
	x1 = (-b + math.sqrt(b ** 2 - 4 * a * c)) / 2 / a
	x2 = (-b - math.sqrt(b ** 2 - 4 * a * c)) / 2 / a
	return x1, x2

# 测试:
print('quadratic(2, 3, 1) =', quadratic(2, 3, 1))
print('quadratic(1, 3, -4) =', quadratic(1, 3, -4))

if quadratic(2, 3, 1) != (-0.5, -1.0):
    print('测试失败')
elif quadratic(1, 3, -4) != (1.0, -4.0):
    print('测试失败')
else:
    print('测试成功')