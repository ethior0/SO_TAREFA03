n: int = 0;
i: int = 1;
fat: int = 1;
res: float = 1;

n = int(input("Insira o número: "));

while i <= n:
  fat = fat * i;
  res += 1 / fat;
  i += 1;

print(f"Valor final aproximado: {res:.3f}");