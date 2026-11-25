# GramFix

## Instalação

Pré-requisitos: Python 3.10 ou superior, Git e acesso à internet.

Clone o repositório e entre na pasta do projeto:

```bash
git clone https://github.com/lupercioneto/P0-DIO.git
cd P0-DIO
```

Crie e ative um ambiente virtual.

Windows (PowerShell):

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

Linux/macOS:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

Instale as dependências:

```bash
python -m pip install -r requirements.txt
```

## Configuração

O projeto acessa o modelo `openai/gpt-oss-120b` pela API da Groq e requer uma chave de API. Gere uma chave no [Groq Console](https://console.groq.com/).

Copie `.env.example` para `.env` a pasta raiz do projeto.

Windows (PowerShell):

```powershell
Copy-Item .env.example .env
```

Linux/macOS:

```bash
cp .env.example .env
```

Edite `.env` e informe sua chave:

```env
GROQ_API_KEY=sua_chave_aqui
```

Não compartilhe nem faça commit do arquivo `.env` ou da chave de API. O arquivo `.env` está excluído pelo Git.

## Execução

Com o ambiente virtual ativado e a chave configurada, execute o seguinte comando na pasta raiz do projeto:

```bash
python -m src.main
```

Digite o texto a revisar quando solicitado. A aplicação exibirá a correção no terminal. Em caso de credencial ausente ou inválida, problema de conexão ou indisponibilidade da API, será apresentada uma mensagem explicativa.