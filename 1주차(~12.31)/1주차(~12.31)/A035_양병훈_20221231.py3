num = int(input())

equation = []
for i in range(num):
  temp = input().split()
  equation.append(temp)

for i in range(num):
  sums = 0
  for j in range(len(equation[i])):
    if j==0:
      sums = float(equation[i][j])
    if equation[i][j] == "@":
      sums *= 3.00
    elif equation[i][j] =="%":
      sums += 5.00
    elif equation[i][j] == "#":
      sums -= 7
  sums = round(sums, 2)
  print("{:.2f}".format(sums))