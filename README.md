## Cotação do Dólar Americano (USD to BRL)

Um aplicativo web simples desenvolvido em Streamlit que exibe a cotação atual do Dólar Americano (USD) para o Real Brasileiro (BRL) em tempo real. Os dados são consumidos a partir da AwesomeAPI.

Este projeto foi desenvolvido como um trabalho acadêmico para demonstrar o uso de APIs.

### Acesso à Aplicação

Você pode acessar a aplicação online através do seguinte link:

``st-cotacao-dolar.streamlit.app``

##

### Tecnologias Utilizadas:

  - Python

  - Streamlit: Framework para a construção da interface web.

  - Pandas: Biblioteca para manipulação e exibição dos dados em formato de tabela.

  - uv: Um instalador e resolvedor de pacotes Python extremamente rápido.

  - AwesomeAPI: API utilizada para obter os dados da cotação de moedas.

##
    
### Como Executar o Projeto Localmente

Para executar este projeto em sua máquina local, siga os passos abaixo.

Pré-requisitos

  - Python 3.13 ou superior
  - Git

Passos
    Clone o repositório:

``` bash
git clone https://github.com/luis-otavio-dias/st-cotacao-dolar.git
cd st-cotacao-dolar
```

Crie e ative um ambiente virtual:

``` bash
python -m venv .venv
source .venv/bin/activate
# No Windows, use: .venv\Scripts\activate
``` 
Instale as dependências com uv:

Se você não tiver o uv instalado, instale-o primeiro:

``` bash
pip install uv
``` 

Em seguida, instale as dependências do projeto:

``` bash
uv sync
``` 
Execute a aplicação Streamlit:

``` bash
streamlit run main.py
```
Após executar o comando, o aplicativo será aberto automaticamente no seu navegador padrão.

##

### Licença

Este projeto está sob a licença MIT.
