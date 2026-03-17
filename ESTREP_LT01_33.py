n: int = 0;
i: int = 1;
res: float = 0;

n = int(input("Insira um número: "));

while i <= n:
  res += 1 / i;
  i += 1;

print(f"Valor final aproximado: {res:.3f}");