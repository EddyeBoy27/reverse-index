# Desafio Python

## 1 - Contexto 

Aqui na **Projeto22** "conhecimento" é a palavra-chave, disponibilizamos para nossos colaboradores um acervo contendo milhares de documentos dos mais diversos assuntos, a fim de contribuir na busca interminável pelo saber. 

Queremos aumentar ainda mais a nossa disponibilidade de títulos, mas ultimamente notamos que muitos dos nossos colaboradores relatam a enorme dificuldade de encontrar um documento de um determinado assunto, frente ao enorme acervo que disponibilizamos.<br/> 
Na esperança de uma solução fácil que permita a pesquisa de informações através de palavras-chave em nossos documentos, consultamos um de nossos maiores especialistas em Engenharia de Software ...**Tobias "The Guy"!** 

Tobias, com o objetivo de resolver o problema da forma mais simples e eficiente, decidiu utilizar uma representação vetorial para nossos documentos.<br/>
Mecanismos de pesquisa utilizam diversos tipos de representações de documentos, uma delas é a representação vetorial. Esta representação permite o uso direto de ferramentas matemáticas como distância, similaridade e redução de dimensão. 

Só que surgiu um pequeno problema, devido ao enorme backlog de demandas, Tobias está com falta de disponibilidade para atuar na solução do nosso problema **:(** <br/>
Aí que você entra, jovem entusiasta do saber, pedimos sua ajuda para implementar este grande desafio, para que a busca incessante pelo saber não acabe!

Nosso desafio não se resume a ferramentas matemáticas, mas sim sobre a construção de um índice reverso que acelere os cálculos. Muitas vezes os cálculos necessários são baseados em produto escalar que acabam consumindo muita memória e CPU do computador, tendo um índice reverso simplifica em muito os cálculos.

Nós precisamos que você escreva uma implementação eficiente de um índice reverso, que indexe uma quantidade grande de documentos.

----
# Solução

Para a solução do desafio, decidi criar um dicionário, utilizando cada palavra única de cada documento como <b>key</b>. Como <b>value</b>, inseri uma lista de dois index, o index [0] é o <b>wordId</b> e o index [1] é uma lista contendo os documentos que contém aquela palavra.

Espero que gostem da minha solução para o desafio, e estou aberto para esclarecimentos e desenvolvimento do algoritmo.

LinkedIn: [Aqui](https://www.linkedin.com/in/felipe-alima/)

Email: lipe_lim@hotmail.com
