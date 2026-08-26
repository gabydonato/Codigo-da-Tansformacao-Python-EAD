# 🍧 Sistema de Vendas - Açaiteria & Barbearia

Um sistema interativo desenvolvido em Python para gerenciamento de vendas, controle de estoque, cadastro de clientes e acompanhamento financeiro, projetado com foco em usabilidade e organização de negócios.

---

## 📌 Sumário
- [Visão Geral do Projeto](#-visão-geral-do-projeto)
- [Histórias de Usuário (User Stories)](#-histórias-de-usuário-user-stories)
- [Funcionalidades Principais](#-funcionalidades-principais)
- [Tecnologias e Estruturas Utilizadas](#-tecnologias-e-estruturas-utilizadas)
- [Como Executar o Projeto](#-como-executar-o-projeto)
- [Estrutura do Menu CLI](#-estrutura-do-menu-cli)

---

## 🎯 Visão Geral do Projeto

O **Sistema de Vendas** foi desenvolvido para auxiliar na gestão de produtos, clientes e operações de vendas. A aplicação permite cadastrar produtos, controlar o estoque, registrar vendas, atualizar preços, aplicar descontos e acompanhar o faturamento obtido de forma rápida e intuitiva.

O sistema conta com suporte a execuções via **Terminal (CLI)** e integração com **Interface Gráfica (Tkinter)**, realizando validações de dados, controle automático de estoque e atualizações em tempo real.

---

## 👥 Histórias de Usuário (User Stories)

Para cobrir as necessidades de todas as partes interessadas no desenvolvimento do sistema, foram mapeadas as seguintes perspectivas:

* **PO (Product Owner / Dono do Negócio):**
  > *“Como dono do negócio, quero um sistema de vendas para minha açaiteria/barbearia, para que eu possa controlar as vendas e os produtos.”*

* **QA (Cliente / Qualidade):**
  > *“Como cliente, quero um sistema de vendas eficiente, para que eu possa comprar meus produtos favoritos de forma rápida e fácil.”*

* **Tech (Arquitetura & Código):**
  > *“Como programador, quero um sistema de vendas bem estruturado, para que eu possa desenvolver um software eficiente e funcional para o negócio.”*

* **Dev (Desenvolvimento):**
  > *“Como desenvolvedor, quero implementar as funcionalidades necessárias para atender às necessidades do negócio e dos clientes.”*

* **UX (Designer de Experiência):**
  > *“Como designer de UX, quero uma interface intuitiva e agradável, garantindo uma experiência de compra satisfatória para o usuário.”*

* **IA / Data (Analista de Dados):**
  > *“Como analista de dados, quero coletar e analisar dados de vendas para identificar padrões de consumo e otimizar estratégias de marketing e estoque.”*

---

## 🚀 Funcionalidades Principais

- 📦 **Cadastro de Produtos:** Registro com código, nome, marca, preço de custo, validade, lote, estoque mínimo e descrição.
- 📋 **Listagem e Consulta:** Exibição detalhada de produtos e busca rápida pelo nome ou código.
- 🛍️ **Realização de Vendas:** Baixa automática no estoque ao efetuar uma venda.
- 📈 **Gestão de Estoque:** Alertas de estoque mínimo e reposição de itens.
- 💰 **Controle Financeiro:** Consulta do faturamento total obtido e aplicação de descontos.
- 👤 **Gestão de Clientes:** Cadastro e associação de clientes às vendas.
- 🎨 **Interface Gráfica Intuítiva:** Mensagens de confirmação, alerta e erro para navegação fluida.

---

## 🛠️ Tecnologias e Estruturas Utilizadas

### Linguagem
- **Python 3.x**

### Interface Gráfica (GUI)
- **Tkinter**: Utilizado para a criação da interface do sistema.
  - `Tk()`: Janela principal da aplicação.
  - `Label`, `Entry`, `Button`, `Frame`, `LabelFrame`: Componentes visuais.
  - `Text`: Exibição legível da lista de produtos e vendas.
  - `messagebox`: Notificações visuais de erro, alerta e sucesso.
  - `ttk.Style`: Customização e estilização visual dos elementos.

### Estrutura de Programação
- **Laços de Repetição:** Loop `while True` para menus interativos CLI.
- **Estruturas Condicionais:** `if`, `elif` e `else` para tratamento de opções do usuário.
- **Tratamento de Exceções:** Blocos `try/except` garantindo a estabilidade contra entradas inválidas.
- **Manipulação de Dados:** Organização de produtos via variáveis estruturadas (Listas/Dicionários).

---

## 🖥️ Estrutura do Menu CLI

Ao executar o script via terminal, o menu interativo oferece as seguintes opções:

```text
--------------------------------------------------------------------------------
1 - Cadastrar produto
2 - Listar produtos
3 - Realizar venda
4 - Listar vendas
5 - Analisar dados de vendas
6 - Criar interface de usuário
7 - Implementar funcionalidades
8 - Otimizar estratégias de marketing
9 - Cadastrar cliente
0 - Sair
--------------------------------------------------------------------------------