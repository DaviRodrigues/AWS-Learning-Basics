# 🛠️ Zero-Prod: Projeto Serverless na AWS com Lambda, API Gateway e DynamoDB

Este é um projeto desenvolvido com foco em **aprendizado de arquitetura serverless na AWS**, utilizando serviços como Lambda, DynamoDB, API Gateway, CloudWatch e CloudFormation por meio do AWS SAM (Serverless Application Model).

---

## 🚀 Tecnologias & Serviços Utilizados

- **AWS Lambda** — Execução de funções sem necessidade de servidores
- **Amazon API Gateway** — Criação de endpoints REST para expor as funções Lambda
- **Amazon DynamoDB** — Banco de dados NoSQL escalável e rápido
- **Amazon CloudWatch** — Monitoramento e logs das execuções das funções
- **AWS CloudFormation (via SAM)** — Infraestrutura como código (IaC)
- **TypeScript + Node.js** — Para a função de criação de usuários
- **Python 3.12** — Para a função de criação de produtos
- **pnpm** — Gerenciador de pacotes rápido e leve
- **SAM CLI** — Para empacotar, fazer build e deploy da aplicação

---

## 📁 Estrutura do Projeto

```bash
handlers/
├── user/                 # Função Lambda (Node.js + TypeScript)
│   └── dist/             # Arquivos compilados
├── product/              # Função Lambda (Python)
template.yml              # Template do SAM com todos os recursos
build.sh                  # Script de build alternativo para TypeScript
```

## 📦 Instalação e Deploy

- **Pré-requisitos: AWS CLI, SAM CLI, Node.js, pnpm, Python 3.12+**

### 1. Instalar dependências

```bash
pnpm install
```

### 2. Compilar a função TypeScript

```bash
pnpm dev
# ou
./build.s
```

### 3. Build e deploy com SAM

```bash
# Primeira vez (irá pedir configurações guiadas e salvar localmente)
sam deploy --guided

# Próximas vezes (usando o mesmo nome de stack configurado)
sam deploy --stack-name zero-prod
```

## 🧪 Testes

### Teste de criação de produto:

```bash
curl -X POST https://<api-url>/products \
  -H "Content-Type: application/json" \
  -d '{
        "name": "Teclado Mecânico RGB",
        "price": 349.90,
        "category": "Periféricos",
        "stock": 25
      }'
```

### Teste de criação de usuário:

```bash
curl -X POST https://<api-url>/users \
  -H "Content-Type: application/json" \
  -d '{
        "name": "João da Silva",
        "email": "joao@email.com",
        "age": 30,
        "location": "Brasil"
      }'
```

## 🧹 Como remover tudo e evitar custos

- **Para deletar todos os recursos criados pela stack:**

```bash
aws cloudformation delete-stack --stack-name nome_da_stack
```

## 📸 Imagens do Projeto (exemplos)

### ✅ Lambda Deploy com sucesso

### 📬 Request recebida com sucesso

### 📊 CloudWatch funcionando e registrando logs

### 💾 Dados armazenados no DynamoDB