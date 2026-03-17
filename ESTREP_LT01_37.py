a: int = 0;
b: int = 1;
c: int = 0;
n: int = 0;

n = int(input("Insira um número: "));

if n > 0:
  print(a);
if n > 1:
  print(b);
if n > 2:
  for i in range(2, n):
    c = a + b;
    a = b;
    b = c;
    print(c);