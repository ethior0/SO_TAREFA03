ana: float = 1.10;
maria: float = 1.50;
anos: int = 0;

while ana <= maria:
  ana += 0.03;
  maria += 0.02;
  anos += 1;

print(f"Levará {anos} anos.");