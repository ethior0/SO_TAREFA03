x: int = 0;
y: int = 0;
maior: int = 0;
menor: int = 0;
cc: int = 0;

x = int(input("Insira o 1o valor: "));
y = int(input("Insira o 2o valor: "));

if x > y:
  maior = x;
  menor = y;
else:
  maior = y;
  menor = x;

if menor < 0:
  print("Inválido!");
else:
  for i in range(menor, maior):
    cc = 0; # contador para quantidade de divisores
    for j in range(2, (i // 2) + 1):
      if i % j == 0:
        cc += 1;
    
    if cc == 0 and i > 1: # núm 1 não é primo
      print(i);