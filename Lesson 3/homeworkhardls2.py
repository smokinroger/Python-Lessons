equation = 'y = -12x + 11111140.2121'
equation = equation.replace(" ", "")
x = 2.5
a = equation.split("=")[1].split("x")[0]
y = float(a)*x+float(equation.split("+")[1])

print(a)
print(equation.split("+")[1])
print(y)

