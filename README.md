# 🧪 Automação de Testes com Python, Selenium e Pytest

Este projeto implementa uma suíte de testes automatizados utilizando **Python**, **Selenium WebDriver** e **Pytest**, seguindo o padrão de arquitetura **Page Object Model (POM)**.  
O objetivo é garantir a qualidade e a estabilidade das funcionalidades web por meio de testes automatizados de interface (UI).

---

## ⚙️ Pré-requisitos

Antes de executar o projeto, certifique-se de ter instalado:

- [Python 3.10+](https://www.python.org/downloads/)
- [Google Chrome](https://www.google.com/chrome/) (ou outro navegador suportado)
- [ChromeDriver](https://chromedriver.chromium.org/downloads) compatível com a versão do seu navegador
- Git (opcional, para clonar o repositório)

---

## 🧩 Como configurar o ambiente

### 1️⃣ Clonar o repositório

```bash
git clone https://github.com/matheusCCO/Trabalho_Automacao_Selenium.git
cd nome-do-repositorio
```

### 2️⃣ Criar e ativar o ambiente virtual

Windows

```bash
Cria: python -m venv venv
Ativa: venv\Scripts\activate
```

macOS / Linux

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3️⃣ Instalar as dependências do projeto

```bash
pip install -r requirements.txt
```

### 🏗️ Estrutura do projeto

```bash
.
├── pages/
│   ├── login_page.py                   # Classe e métodos da página de login
│   ├── home_page.py                    # Classe e métodos da página inicial
│   ├── carrinho.py                     # Classe e métodos da página de carrinho
│   ├── preenche_informacao_pedido.py   # Classe e métodos da página de informações do cliente
│   ├── valida_informacao_pedido.py     # Classe e métodos da página de informações gerais do pedido
│   └── base_page.py                    # Classe base comum a todas as páginas
│
├── tests/
│   └── test_fazer_compra.py  # Casos de teste da funcionalidade de realizar uma compra
│
│
├── requirements.txt          # Dependências do projeto
└── conftest.py               # Fixtures do Pytest (setup e teardown)

```

### 🧱 Padrão Page Object

- Cada página da aplicação é representada por uma classe Python.

- Cada elemento e ação da página é encapsulado em métodos, reduzindo duplicação de código.

- Os testes interagem apenas com os métodos das páginas, nunca diretamente com o Selenium.

### ▶️ Como executar os testes

Após ativar o ambiente virtual e instalar as dependências, execute:

### Rodar todos os testes

```bash
pytest -
```

### Rodar testes com relatório detalhado

```bash
pytest -v
```
