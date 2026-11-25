# GramFix — Corretor Gramatical com LLM

## 1. Sobre o projeto

O GramFix é uma aplicação desenvolvida em Python que utiliza um Modelo de Linguagem de Grande Escala (LLM) para identificar e corrigir erros gramaticais, ortográficos e de pontuação em textos escritos em português.

A aplicação recebe um texto fornecido pelo usuário, envia uma solicitação a um modelo de linguagem por meio da API da Groq e apresenta uma versão corrigida, acompanhada de explicações sobre as principais alterações realizadas.

## 2. Problema escolhido

Erros gramaticais, ortográficos e de pontuação são comuns na produção de textos, especialmente em contextos acadêmicos, profissionais e cotidianos.

Muitas pessoas têm dificuldade para identificar esses erros ou compreender as regras gramaticais envolvidas nas correções.

O GramFix busca oferecer uma ferramenta simples que auxilie na revisão textual e contribua para o aprendizado da língua portuguesa, explicando as alterações realizadas em vez de apenas apresentar o texto corrigido.

## 3. Público-alvo

A aplicação é direcionada principalmente a:

- Estudantes que desejam revisar trabalhos e atividades acadêmicas.
- Pessoas que produzem textos e precisam verificar sua escrita.
- Usuários que desejam compreender melhor seus erros gramaticais.
- Qualquer pessoa interessada em melhorar sua escrita em português.

## 4. Justificativa para utilização de um LLM

A utilização de um Modelo de Linguagem de Grande Escala é adequada ao problema porque a correção textual exige interpretação do contexto, compreensão da estrutura das frases e identificação de diferentes tipos de erros linguísticos.

Diferentemente de uma solução baseada exclusivamente em regras fixas ou expressões regulares, um LLM consegue analisar o contexto de uma frase e considerar aspectos como concordância verbal, concordância nominal, pontuação e ortografia.

Além disso, o modelo consegue gerar explicações em linguagem natural sobre as correções realizadas, tornando a ferramenta também um recurso de apoio ao aprendizado.

Neste projeto, o modelo é acessado por meio da API da Groq, utilizando o modelo `openai/gpt-oss-120b`.

## 5. Funcionamento da solução

O funcionamento do GramFix ocorre nas seguintes etapas:

1. O usuário informa um texto pelo terminal.
2. A aplicação verifica se a entrada é válida.
3. O texto é enviado à API da Groq juntamente com instruções específicas para revisão gramatical.
4. O LLM analisa o conteúdo e retorna o texto corrigido e as explicações das principais alterações.
5. A aplicação recebe e processa a resposta.
6. O resultado é apresentado ao usuário no terminal.

### Fluxo simplificado

```text
Usuário
   |
   v
Entrada textual
   |
   v
Validação da entrada
   |
   v
Aplicação Python
   |
   v
Groq API
   |
   v
LLM (GPT-OSS 120B)
   |
   v
Resposta processada
   |
   v
Resultado no terminal
```

### Tecnologias utilizadas

- **Python 3:** linguagem utilizada no desenvolvimento.
- **Groq API:** serviço utilizado para acessar o modelo de linguagem.
- **Groq Python SDK:** biblioteca responsável pela comunicação com a API.
- **python-dotenv:** carregamento das variáveis de ambiente.
- **Pytest:** execução dos testes automatizados.
- **Git e GitHub:** controle de versão e hospedagem do código-fonte.

## 6. Limites do projeto

O GramFix possui um escopo intencionalmente reduzido, com foco na integração entre Python e um único modelo de linguagem.

As seguintes limitações fazem parte da proposta:

- A aplicação trabalha exclusivamente com entrada e saída textual.
- O sistema é direcionado à correção de textos em português.
- Não existe armazenamento ou histórico das correções realizadas.
- Não há interface gráfica, sendo toda a interação realizada pelo terminal.
- A aplicação depende de conexão com a internet para acessar a API da Groq.
- É necessário possuir uma chave válida da API.
- O resultado depende da interpretação e da qualidade das respostas geradas pelo modelo.

## 7. Instalação

### Pré-requisitos

- Python 3.10 ou superior.
- Git.
- Conexão com a internet.
- Uma chave de acesso à Groq API.

### 7.1. Clonar o repositório

```bash
git clone https://github.com/lupercioneto/P0-DIO.git
cd P0-DIO
```

### 7.2. Criar o ambiente virtual

```bash
python -m venv venv
```

Ativação no Windows (PowerShell):

```powershell
.\venv\Scripts\Activate.ps1
```

### 7.3. Instalar as dependências

```bash
pip install -r requirements.txt
```

## 8. Configuração do acesso ao LLM

O GramFix utiliza a API da Groq para realizar as solicitações ao modelo de linguagem.

### 8.1. Obter uma chave de API

1. Acesse o [Groq Console](https://console.groq.com/).
2. Crie uma conta ou faça login.
3. Acesse a seção de API Keys.
4. Gere uma nova chave de acesso.

### 8.2. Configurar a variável de ambiente

Copie o arquivo de exemplo para `.env` na raiz do projeto:

No PowerShell:

```powershell
Copy-Item .env.example .env
```

No Linux/macOS:

```bash
cp .env.example .env
```

Edite `.env` e informe sua chave:

```env
GROQ_API_KEY=sua_chave_aqui
```

O arquivo `.env` é utilizado para armazenar a chave de acesso de maneira separada do código-fonte.

**Importante:** não compartilhe sua chave de API nem a envie ao GitHub.

### 8.3. Modelo utilizado

O modelo configurado na aplicação é:

```text
openai/gpt-oss-120b
```

A comunicação é realizada por meio do Groq Python SDK.

## 9. Execução da aplicação

Após configurar o ambiente e a chave da API, execute o seguinte comando na raiz do projeto:

```bash
python -m src.main
```

A aplicação solicitará um texto pelo terminal e apresentará o resultado da correção.

## 10. Exemplos de entrada e saída

### Exemplo 1 — Erro de concordância verbal

**Entrada:**

```text
Os alunos foi para escola ontem.
```

**Saída esperada:**

```text
TEXTO CORRIGIDO:

Os alunos foram para a escola ontem.

CORREÇÕES REALIZADAS:

1. Concordância verbal:
O sujeito "Os alunos" está no plural.
Portanto, o verbo deve concordar:
"foi" -> "foram".

2. Artigo definido:
Inserção do artigo "a" antes de "escola":
"para escola" -> "para a escola".
```

### Exemplo 2 — Erros ortográficos

**Entrada:**

```text
Eu nao conssegui terminar o trabalho.
```

**Saída esperada:**

```text
TEXTO CORRIGIDO:

Eu não consegui terminar o trabalho.

CORREÇÕES REALIZADAS:

1. Acentuação:
"nao" -> "não".

2. Ortografia:
"conssegui" -> "consegui".
```

*Observação: os exemplos são ilustrativos. Como a resposta é gerada por um LLM, a redação e a organização das explicações podem variar entre as solicitações.*

## 11. Testes

O projeto utiliza Pytest para verificar o comportamento das principais funcionalidades e o tratamento de erros.

Os testes automatizados incluem:

- Rejeição de textos vazios.
- Credencial ausente ou em branco.
- Credencial inválida, simulada sem expor o segredo.
- Resposta de sucesso simulada.
- Falha de comunicação e timeout.
- Modelo indisponível e erro temporário do serviço.
- Respostas vazias ou em formato inesperado.

### 11.1. Executar os testes

Na raiz do projeto, execute:

```bash
pytest -v
```

### 11.2. Testes simulados

Os testes automatizados utilizam mocks para simular as respostas e falhas da API da Groq. Isso inclui credenciais ausentes e inválidas, sem enviar chaves reais nem fazer chamadas externas.

Esses testes não verificam a disponibilidade real da Groq e não consomem créditos. Para reproduzir falhas de autenticação com a API real, use uma chave inválida apenas em ambiente local e nunca a inclua em commits ou compartilhe o valor.

### 11.3. Execução real

Para verificar a comunicação real com o modelo:

1. Configure uma chave válida no arquivo `.env`.
2. Execute `python -m src.main`.
3. Envie um texto e confira a resposta apresentada no terminal.

Essa execução acessa a Groq, depende de internet e está sujeita a limites e custos definidos pelo serviço. Os testes simulados e a execução real são verificações diferentes: os mocks não comprovam que o serviço esteja disponível. Se for utilizada infraestrutura institucional, a recuperação do serviço permanece sob responsabilidade da equipe técnica.

## 12. Limitações conhecidas

Apesar de utilizar um modelo de linguagem avançado, o GramFix não garante que todas as correções estejam linguisticamente corretas.

Entre as limitações conhecidas estão:

- Possibilidade de correções inadequadas dependendo do contexto.
- Possibilidade de o modelo modificar trechos que já estavam corretos.
- Variação na qualidade e no nível de detalhamento das explicações.
- Dependência da disponibilidade e dos limites de utilização da Groq API.
- Ausência de validação gramatical independente para conferir todas as sugestões do modelo.

Portanto, o resultado deve ser considerado uma sugestão de revisão, e não uma garantia de correção absoluta.

## 13. Estrutura do projeto

```text
P0-DIO/
│
├── src/
│   ├── __init__.py
│   ├── config.py
│   ├── corretor.py
│   ├── main.py
│
├── tests/
│   ├── __init__.py
│   └── test_corretor.py
│
├── .env.example
├── .gitignore
├── requirements.txt
└── README.md
```

## 14. Autor

Projeto desenvolvido como atividade acadêmica com o objetivo de explorar a integração de aplicações Python com Modelos de Linguagem de Grande Escala (LLMs).