n: int = 0;
res: int = 1;

n = int(input("Insira um número inteiro: "));

for i in range(n, 1, -1):
  res = res * i;

print("Valor do fatorial:", res);