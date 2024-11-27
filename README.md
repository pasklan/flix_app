# Flix App

O Flix App é uma aplicação web desenvolvida com Django e Streamlit, que permite aos usuários pesquisar, visualizar informações e assistir trailers de filmes.

## Funcionalidades

### Página Inicial
- Exibe uma lista de filmes em destaque, com opções de filtro por gênero e ordenação.
- Permite que os usuários visualizem detalhes do filme, como sinopse, elenco, diretor e trailer.
- Inclui a opção de adicionar o filme aos favoritos do usuário.

### Página de Pesquisa
- Permite que os usuários pesquisem filmes pelo título.
- Exibe os resultados da pesquisa de forma paginada, com opções de filtro e ordenação.
- Ao clicar em um filme, o usuário é redirecionado para a página de detalhes do filme.

### Página de Detalhes do Filme
- Apresenta informações detalhadas sobre o filme, como sinopse, elenco, diretor, classificação etária, duração e trailer.
- Permite que os usuários adicionem o filme aos seus favoritos.
- Exibe recomendações de filmes relacionados.

### Página de Favoritos
- Mostra a lista de filmes adicionados aos favoritos pelo usuário.
- Permite que o usuário remova um filme da sua lista de favoritos.
- Inclui opções de filtro e ordenação da lista de favoritos.

### Autenticação de Usuário
- Permite que os usuários se cadastrem e façam login na aplicação.
- Apenas usuários autenticados podem adicionar filmes aos seus favoritos.
- Exibe o nome do usuário logado no cabeçalho da aplicação.

### Administração do Sistema
- Inclui uma área administrativa para gerenciamento de filmes, gêneros e usuários.
- Apenas usuários com permissão de administrador têm acesso à área administrativa.
- Permite que os administradores adicionem, editem e excluam informações sobre filmes e gêneros.

### Interface do Usuário com Streamlit
- O projeto utiliza o framework Streamlit para criar uma interface gráfica interativa para os usuários.
- A interface Streamlit permite uma experiência de usuário mais intuitiva e visualmente atraente.
- Os usuários podem interagir com a aplicação, pesquisar filmes, visualizar detalhes e favoritos diretamente pela interface Streamlit.

## Tecnologias Utilizadas
- Django: framework web Python para desenvolvimento do backend.
- Django REST Framework: para a criação da API de filmes.
- Streamlit: framework Python para a criação da interface gráfica do usuário.
- SQLite: banco de dados utilizado para armazenar as informações.
- HTML, CSS e JavaScript: para a construção da interface web.
- Bootstrap: framework CSS para estilização da aplicação.

## Como Executar o Projeto
1. Clone o repositório do projeto.
2. Crie e ative um ambiente virtual.
3. Instale as dependências do projeto.
4. Realize as migrações do banco de dados.
5. Inicie o servidor de desenvolvimento do Django e o servidor do Streamlit.
6. Acesse a aplicação em seu navegador.

Desenvolvido por Renato Pasklan
