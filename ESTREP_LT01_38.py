maior: int = 0;
menor: int = 0;
num: int = 0;

for i in range(100):
  num = int(input(f"Insira um número ({i+1}º): "));
  if num < menor:
    menor = num;
  if num > maior:
    maior = num;

print("Menor e maior:", menor, maior)