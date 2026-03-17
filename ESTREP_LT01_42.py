res: float = 0;
j: int = 1;

for i in range(1, 51):
  res += i / j;
  j += 2;

print(f"Resultado: {res:.3f}");