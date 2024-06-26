# Testes com Selenium 

### Para Executar

- Você deverá executar o servidor da aplicação no repositório https://github.com/GuedesPeter/QA-testes-django rodando o comando : 
        
        python manage.py runserver

- Após execute no código deste repositório o comando: 

        python test_selenium.py


## EXPLICAÇÃO

test_pagina_inicial


Propósito: Verificar se a página inicial carrega corretamente e contém o título esperado.
Passos:
Acessar a página inicial (http://127.0.0.1:8000/).
Verificar se o título da página contém "Lista de Livros".


test_adicao_livro

Propósito: Testar a funcionalidade de adicionar um novo livro.
Passos:
Acessar a página de adicionar livro (http://127.0.0.1:8000/adicionar/).
Preencher o formulário com os detalhes do livro.
Submeter o formulário.
Verificar se o livro adicionado aparece na página inicial.


test_atualizacao_livro


Propósito: Testar a funcionalidade de atualizar os detalhes de um livro existente.
Passos:
Acessar a página inicial.
Clicar no botão de editar para um livro existente.
Atualizar os detalhes do livro.
Submeter o formulário.
Verificar se as mudanças aparecem na página inicial.


test_atualizacao_livro


Propósito: Testar a funcionalidade de atualizar os detalhes de um livro existente.
Passos:
Acessar a página inicial.
Clicar no botão de editar para um livro existente.
Atualizar os detalhes do livro.
Submeter o formulário.
Verificar se as mudanças aparecem na página inicial.

## Como os Testes Funcionais São Executados

Setup e Teardown:

O método setUpClass inicializa o navegador antes que qualquer teste seja executado.

O método tearDownClass encerra o navegador após todos os testes terem sido executados.
Execução dos Testes:

Cada método de teste é independente e executa uma sequência específica de ações na aplicação web, verificando os resultados esperados.
O Selenium é usado para interagir com a aplicação web da mesma forma que um usuário faria, como preencher formulários, clicar em botões e navegar entre páginas.
Verificações:

Os testes usam assertions para verificar se o estado da aplicação após cada interação é o esperado (por exemplo, verificar se um livro foi adicionado ou excluído corretamente).