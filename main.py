import math

def calc_equation(a, b=0, c=0):
    if a == 0:
        print("Não é uma equação de segundo grau.")
        return
    
    if b == 0 and c == 0:
        print("A equação é 0 = 0, que é uma identidade.")
        return
    elif b == 0:
        if c != 0:
            x = math.sqrt(-c / a)
            results = [x, -x]
            print(f"S = {sorted(results)}")
        else:
            print("A equação é 0 = 0, que é uma identidade.")
    elif c == 0:
        x1 = 0
        x2 = -b / a
        results = [x1, x2]
        print(f"S = {sorted(results)}")
    else:
        delta = b ** 2 - 4 * a * c
        
        if delta > 0:
            x1 = (-b - math.sqrt(delta)) / (2 * a)
            x2 = (-b + math.sqrt(delta)) / (2 * a)
            results = sorted([x1, x2])
            print(f"S = {results}")
        elif delta == 0:
            x = -b / (2 * a)
            print(f"S = [{x}]")
        else:
            print("A equação não tem raízes reais.")
            
print("Teste 1: Completa")
calc_equation(2, -5, 3)
