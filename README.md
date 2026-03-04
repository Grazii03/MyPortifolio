# Meu Portfólio

Este é o meu portfólio interativo, desenvolvido com a utilização de tecnologias modernas para exibir minhas habilidades, experiências e projetos.

## Objetivo

A API do Meu Portfólio fornece várias funcionalidades relacionadas ao gerenciamento de conteúdo do portfólio interativo. As principais funcionalidades incluem a exibição de informações sobre a pessoa (como educação e áreas de atuação), projetos, habilidades, experiência e contatos.

## Funcionalidades

- **GET /api/skills**: Retorna uma lista de habilidades para exibição no portfólio. O campo `hard` contém habilidades técnicas e o campo `soft` contém habilidades interpessoais.
- **GET /api/about**: Retorna informações sobre a pessoa, como nome, bio e áreas de atuação.
- **POST /api/contact**: Recebe mensagens de contato diretamente do portfólio. O usuário fornece nome, e-mail e mensagem, que são registrados na API.

## Tecnologias Utilizadas

### Backend
- **Flask**: Framework para construção da API REST.
- **psycopg2-binary**: Biblioteca para conectar a API ao banco de dados PostgreSQL.
- **Gunicorn**: Servidor WSGI para executar a aplicação Flask em produção.

### Frontend
- **HTML5 e CSS3**: Estrutura e estilização da página.
- **JavaScript (Fetch API)**: Para carregar dinamicamente as informações das habilidades da API.
- **Fontes**: Uso de fontes personalizadas do Google Fonts, como "Lora", "Anton", "Inter", etc.

## Como Rodar o Projeto

### Requisitos
- Python 3.x
- pip (gerenciador de pacotes Python)

### Instalando Dependências

1. Clone o repositório:
   ```bash
   git clone https://github.com/Grazii03/MyPortfolio.git