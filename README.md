# Keyword Search
Script para análise das keywords da string de busca nos resultados encontrados no Scopus


# Como utilizar?
Antes de utilizar você deve realizar uma busca com sua string no Scopus e exportar os resultados. Para exportar, você deve estar na tela de resultados de busca. Estando nela, clique na opção para selecionar todos os resultados (link "Select" e a opção "Select all"). Após selecione a opção "Export" e escolha o formato CSV e selecione as colunas que deverão ser buscadas. Por exemplo, se sua busca é por título, abstract e keywords você deve selecionar as colunas "Document Title", "Abstract", "Author keywords" e "Index keywords". Exemplo de arquivo exportado:

```csv
Title,Link,Abstract,Author Keywords,Index Keywords
"Falling for fake news: Investigating the consumption of news via social media","https://www.scopus.com/inward/[..]","In the so called 'post-truth' era, characterized by a loss of public trust in various institutions,[...]","Facebook; Fake news; [..]","Human computer interaction; [..]"
"Mining significant microblogs for misinformation identification: An attention-based approach","https://www.scopus.com/inward/[..]","With the rapid growth of social media, [..]","Attention model; Misinformation identification; [...]","Dynamics; Information use; [...]"
"Informative and misinformative interactions in a school of fish","https://www.scopus.com/inward/[..]","Quantifying distributed information processing is crucial [..]","Collective animal behaviour; Collective motion; [...]","Animals; Computation theory;[..]"
```

Após exportar os resultados, você deve criar um arquivo de texto contendo **somente** as palavras chave da sua string de busca e os operadoes lógicos (AND e OR). Exemplo, para a busca `TITLE-ABS-KEY((method OR techinique) AND ("fake news" OR misinformation)) AND SUBJAREA(COMP)` crie um arquivo com o conteúdo:

	(method OR techinique) AND ("fake news" OR misinformation) 

Após isso, você pode executar o script informando o caminho do arquivo com as keyword e o arquivo com os resultados exportados.

```sh
	python main.py [-h] [--detailed] arquivoComAsKeywords arquivoExportadoDoScopus
```
***Argumentos:***
* `--detailed` (opcional) Gera resultados mais detalhados sobre as keywords, como o título de todos os artigos associados as keywords e todos as keyword encontradas para um artigo
* `arquivoComAsKeywords` Caminho do arquivo com as keywords
* `arquivoExportadoDoScopus` Caminho do arquivo com o resultado exportado. Para utilizar a opção `--detailed` a primeira coluna do CSV será lida como o título do artigo
