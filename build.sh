#!/bin/bash

echo "Iniciando build do TypeScript..."

cd "./handlers/user"

# Compila o projeto com tsc (baseado no tsconfig.json)
pnpm build

if [ $? -eq 0 ]; then
  echo "Build concluído com sucesso!"
else
  echo "Erro na build do TypeScript."
  exit 1
fi
