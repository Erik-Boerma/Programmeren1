def tel_op(x):
    if x<=0:
        return x
    x = x + tel_op(x-1)
    return x

print(tel_op(0))
print(tel_op(8))
print(tel_op(5))
print(tel_op(200))