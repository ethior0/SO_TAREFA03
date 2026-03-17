base: float = 0;
valor: float = 0;
expoente: int = 0;

base = float(input("Insira o valor da base: "));
expoente = int(input("Insira o valor do expoente: "));

valor = base;

for i in range(expoente-1):
  valor *= base;

print(f"{base} ^ {expoente} = {valor}");