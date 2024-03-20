#3 絕對值:簡單來說，絕對值就是去掉數字的正負號，將其轉換為非負值。

X = -5

y= abs(X)

print('abs=' + str(y))

#4 商數與餘數

a, b = divmod(10, 7)

print('divmod商數=' + str(a))
print('divmod餘數=' + str(b))


#5 max & min 取最大值或最小值

c = max(1,2,3,4,5)
print('max=' + str(c))
d = min(1,2,3,4,5)
print('max=' + str(d))


#6 次方

e = 2**5

print('2的5次方=' + str(e))
f = pow(2,5)

print('2的5次方=' + str(f))

#7 四捨五入

g = round(3.14159)

print('g的四捨五入 =' + str(g))

h = round(3.14159, 3)

print('h的四捨五入取小數點三位 =' + str(h))

# 無條件進入
import math

i = math.ceil(3.14159)
print('i的無條件進入 =' + str(i))


# 最大公因數

j = math.gcd(12, 8)
print("最大公因數為" + str(j))

# 數學常數

r = 10 
k = math.pi * r * r
print("半徑10的面績為" + str(k))
