from turtle import *
infinity = float('inf')
color('black')
begin_fill()
x = 10
c = 1
while c > 0:
    x = x + 7  # 7 is cool here
    speed(infinity)
    forward(10)
    left(x)
    if abs(pos()) < 1:
        x = x + 21  # 21 is cool here
end_fill()
done()
