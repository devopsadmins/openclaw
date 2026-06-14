import re

with open('DISTORCAO.MD', 'r', encoding='utf-8') as f:
    lines = f.readlines()

new_lines = []
for line in lines:
    # Substitui "- " no início da linha por "— " (travessão)
    if line.startswith("- "):
        # Substitui o hífen inicial
        line = "— " + line[2:]
        
        # Também podemos substituir " - " no meio da linha (usado para incisos de diálogo)
        line = line.replace(" - ", " — ")
    
    new_lines.append(line)

with open('DISTORCAO.MD', 'w', encoding='utf-8') as f:
    f.writelines(new_lines)

print("Substituição concluída.")