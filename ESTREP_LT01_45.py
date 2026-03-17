res: float = 0;

for i in range(1, 16):
  if i % 2 == 0:
    res -= i / (i * i);
  else:
    res += i / (i * i);

print("Resultado da sequência:", res);