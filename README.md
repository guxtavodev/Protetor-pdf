# Projeto Flask de Upload de PDF com Marca d'Água

Este é um projeto simples desenvolvido em Flask que permite aos usuários realizar o upload de arquivos PDF, adicionar uma marca d'água (texto). A marca d'água é adicionada ao PDF utilizando a biblioteca PyPDF2.

## Funcionalidades

- **Upload de arquivos PDF**: Os usuários podem selecionar um arquivo PDF localmente para ser processado.
- **Adição de marca d'água**: Um campo de texto permite inserir o texto desejado para a marca d'água, que será sobreposta ao PDF.
- **Animação de confetes**: Ao enviar o formulário com sucesso, uma animação de confetes é exibida para proporcionar uma experiência visual divertida.

## Tecnologias Utilizadas

- **Python 3**: Linguagem de programação utilizada para o backend.
- **Flask**: Framework web utilizado para criar a aplicação web.
- **HTML**: Linguagem de marcação utilizada para estruturar a página web.
- **CSS (com Tailwind CSS)**: Framework CSS utilizado para estilização.
- **JavaScript (particles.js)**: Biblioteca JavaScript utilizada para criar a animação de confetes.
- **PyPDF2**: Biblioteca Python utilizada para manipulação de arquivos PDF.

## Como Executar

1. **Clone o Repositório**:

   ```bash
   git clone https://github.com/guxtavodev/Projeto-pdf.git
   ```

2. **Instale as Dependências**:

   ```bash
   pip install Flask PyPDF2
   ```

3. **Execute a Aplicação**:

   ```bash
   python app.py
   ```

4. **Acesse a Aplicação**:

   Abra o navegador e vá para `http://localhost:5000` para visualizar a aplicação.

## Como Funciona

- **Upload de PDF**: Selecione um arquivo PDF usando o botão de upload.
- **Adição de Marca d'Água**: Digite o texto desejado para a marca d'água.
- **Envio e Processamento**: Ao enviar o formulário, você verá uma animação de confetes enquanto o PDF é processado.
- **Download do PDF Modificado**: Após o processamento, o usuário pode baixar o PDF com a marca d'água adicionada.

## Estrutura do Projeto

- `app.py`: Arquivo principal do Flask que define as rotas e o processamento do upload.
- `templates/index.html`: Template HTML para a página de upload e processamento.
- `static/style.css`: Arquivo CSS para estilização adicional (opcional).

## Contribuições

Contribuições são bem-vindas! Sinta-se à vontade para enviar pull requests para melhorias, correções de bugs ou novas funcionalidades.

## Licença

Este projeto é licenciado sob a [Licença MIT](https://opensource.org/licenses/MIT).
