import re

input_path = "livros/ninguem_precisa_saber/MANUSCRITO_NINGUEM_PRECISA_SABER.md"
output_path = "livros/ninguem_precisa_saber/MANUSCRITO_PUBLICAVEL.md"

with open(input_path, 'r') as f:
    lines = f.readlines()

with open(output_path, 'w') as f:
    for line in lines:
        # Remove padrões como "### 1. Abertura concreta", "### 2. Contexto humano", etc.
        if re.match(r'^### \d+\. ', line):
            continue
        # Remove linhas que sejam apenas números (caso tenham ficado sozinhas)
        if re.match(r'^\d+\.', line):
            continue
        f.write(line)
