# 📦 Compila o projeto e prepara para o deploy
sam build

# 🚀 Realiza o primeiro deploy com guia interativo
# Isso salvará configurações para futuros deploys
sam deploy --guided

# 🔁 Após o primeiro deploy, use isso para futuras atualizações
sam deploy --stack-name nome-da-sua-stack

# 🗑️ Deleta a stack e todos os recursos criados (Lambda, DynamoDB, etc.)
aws cloudformation delete-stack --stack-name nome-da-sua-stack

# 🔍 Verifica o status da stack (útil após deletar ou para debugging)
aws cloudformation describe-stacks --stack-name nome-da-sua-stack

# Lista todas as stacks:
aws cloudformation list-stacks --stack-status-filter CREATE_COMPLETE UPDATE_COMPLETE
