# Bootcamp Engenharia de Dados com Python - NTT DATA

## Desafio do Módulo: Sintaxe com Python

### Projeto: Criando um Sistema Bancário com Python

#### Objetivo Geral

Desenvolver uma versão inicial de um sistema bancário que possibilite as operações essenciais de: **sacar**, **depositar** e **visualizar extrato**. O projeto será implementado para apenas **1 usuário**, evitando a necessidade de identificar o número da agência e conta bancária.

---

### Funcionalidades

#### 1. Depósito

-   Permitir o depósito de valores **positivos** na conta.
-   Todos os depósitos devem ser armazenados em uma variável e exibidos na operação de extrato.

#### 2. Saque

-   O sistema deve permitir **até 3 saques diários**.
-   Limite máximo de **R$ 500,00** por saque.
-   Caso o usuário não tenha saldo suficiente, o sistema deve exibir uma mensagem informando que não será possível realizar o saque por falta de saldo.
-   Todos os saques devem ser armazenados em uma variável e exibidos na operação de extrato.

#### 3. Extrato

-   Listar todos os depósitos e saques realizados na conta.
-   Exibir o saldo atual da conta ao final da listagem.
-   Se não houver movimentações, exibir a mensagem: **"Não foram realizadas movimentações."**
-   Os valores devem ser exibidos no formato **R$ XXX.XX**.

---
