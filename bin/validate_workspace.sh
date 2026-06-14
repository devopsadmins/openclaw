#!/bin/bash
# bin/validate_workspace.sh
# Validador de integridade do ambiente do Editor E.O.Lima

echo "--- Iniciando Validação de Integridade ---"

# Verificar arquivos essenciais
ESSENTIALS=("USER.md" "MEMORY.md" "SOUL.md" "IDENTITY.md" "AGENTS.md")
for file in "${ESSENTIALS[@]}"; do
    if [ ! -f "$file" ]; then
        echo "ERRO: Arquivo essencial $file não encontrado na raiz!"
        exit 1
    fi
done

# Verificar formato do USER.md (check básico por campos críticos)
if ! grep -q "Elisangela Lima" USER.md || ! grep -q "Stephanie Lima" USER.md; then
    echo "ERRO: USER.md parece corrompido ou sem os contatos obrigatórios."
    exit 1
fi

echo "Integridade do ambiente: OK"
exit 0
