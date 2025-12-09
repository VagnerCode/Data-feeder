# 📊 Data Feeder (Automação de Planilhas)

![Python](https://img.shields.io/badge/Python-3.10%2B-blue)
![License](https://img.shields.io/badge/License-MIT-green)
![Status](https://img.shields.io/badge/Status-Active-success)

> **Automatize o lançamento de dados de volume e tráfego (GB) em múltiplas abas do Google Sheets através de uma interface gráfica intuitiva.**

---

## 🚀 Sobre o Projeto

O **Data Feeder** foi desenvolvido para eliminar o trabalho manual e repetitivo de alimentar relatórios mensais de clientes. Ao invés de abrir o navegador, navegar por múltiplas abas e localizar células manualmente, o sistema oferece uma interface desktop ágil onde o operador insere os dados e o software cuida da sincronização com a nuvem.

![Interface do Software](assets/screenshot.png)

### 🎯 Principais Funcionalidades

- **Identificação Inteligente:** Localiza automaticamente a aba do cliente e a coluna correspondente à data informada (ex: `13.11`).
- **Interface Gráfica (GUI):** Desenvolvida em `Tkinter` com tema escuro (Dark Mode) para conforto visual.
- **Log em Tempo Real:** Feedback visual imediato sobre o sucesso ou falha das operações.
- **Navegação Rápida:** Botão "Pular Cliente" para alternar rapidamente entre empresas sem usar o mouse.
- **Segurança:** Autenticação via OAuth 2.0 do Google, garantindo que as credenciais sensíveis não fiquem expostas no código.

---

## 🛠 Tecnologias Utilizadas

- **Linguagem:** [Python](https://www.python.org/)
- **Interface Gráfica:** [Tkinter](https://docs.python.org/3/library/tkinter.html)
- **Bibliotecas de Integração:** [gspread](https://docs.gspread.org/), [Google Client Library](https://github.com/googleapis/google-api-python-client)
- **APIs do Google:** Google Sheets API, Google Drive API
- **Gerenciamento de Ambiente:** [python-dotenv](https://pypi.org/project/python-dotenv/)
---

## ⚙️ Pré-requisitos e Configuração

Para executar este projeto localmente, você precisará configurar o acesso à API do Google.

### 1. Configuração no Google Cloud Platform

1.  Acesse o [Google Cloud Console](https://console.cloud.google.com/).
2.  Crie um novo projeto.
3.  Ative as seguintes APIs:
    - **Google Drive API**
    - **Google Sheets API**
4.  Vá em "Credenciais", crie uma credencial do tipo **OAuth Client ID** (Desktop App).
5.  Baixe o arquivo JSON, renomeie para `credentials.json` e coloque na raiz do projeto.

### 2. Variáveis de Ambiente

Crie um arquivo chamado `.env` na raiz do projeto para armazenar o ID da planilha de forma segura:

```env
PLANILHA_ID=insira_aqui_o_id_da_sua_planilha_google
```

## 📦 Instalação e Execução

Clone o repositório e instale as dependências:

```bash
# 1. Clone o repositório
git clone [https://github.com/VagnerCode/Data-feeder.git](https://github.com/VagnerCode/Data-feeder.git)

# 2. Entre na pasta
cd Data-feeder

# 3. Instale as dependências
pip install -r requirements.txt

# 4. Execute a aplicação
python app.py
Na primeira execução, uma janela do navegador será aberta solicitando permissão para acessar o Google Drive/Sheets. Após aceitar, um arquivo token.json será gerado automaticamente.
```

📂 Estrutura do Projeto
/

├── app.py # Código principal da aplicação

├── requirements.txt # Lista de dependências

├── .env # Variáveis de ambiente (NÃO COMMITE ESTE ARQUIVO)

├── .gitignore # Arquivos ignorados pelo Git

├── credentials.json # Credencial do Google (NÃO COMMITE ESTE ARQUIVO)

└── README.md # Documentação do projeto

🛡 Segurança

Este projeto segue boas práticas de segurança:

As credenciais (credentials.json, token.json) e configurações de ambiente (.env) nunca devem ser enviadas para o repositório (GitHub).

Certifique-se de que seu arquivo .gitignore contenha essas exceções.

🤝 Contribuição
Contribuições são bem-vindas! Sinta-se à vontade para abrir issues ou enviar pull requests.

📝 Licença
Este projeto está sob a licença MIT. Veja o arquivo LICENSE para mais detalhes.

<p align="center"> <sub>Desenvolvido por <b>Vagner Carvalho</b></sub> </p>
