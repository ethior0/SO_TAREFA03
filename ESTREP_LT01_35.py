x: int = 0;
y: int = 0;
maior: int = 0;
menor: int = 0;
res: int = 0;

x = int(input("Insira o 1o valor: "));
y = int(input("Insira o 2o valor: "));

if x > y:
  maior = x;
  menor = y;
else:
  maior = y;
  menor = x;

for i in range(menor+1, maior):
  if i % 2 != 0:
    res += i;

print("Soma dos números ímpares:", res);