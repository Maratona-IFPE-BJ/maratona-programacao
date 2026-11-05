# Guia de Contribuição — Projeto Maratona

Bem-vindo(a) ao repositório do **Projeto Maratona**!

Este repositório tem como objetivo reunir soluções de problemas de programação competitiva desenvolvidas pelos integrantes do projeto, promovendo o compartilhamento de conhecimento, a colaboração e o aperfeiçoamento das habilidades de programação.

Todas as contribuições são bem-vindas, desde que sigam as orientações descritas neste documento.

## 1. Como contribuir

As contribuições devem ser realizadas por meio de **Fork e Pull Request**.

O procedimento é:

1. Acesse o repositório oficial do projeto.
2. Clique em **Fork** para criar uma cópia do repositório em sua conta GitHub.
3. Clone seu Fork para o computador.
4. Crie ou adicione os arquivos com suas soluções.
5. Faça commit das alterações.
6. Envie as alterações para seu Fork utilizando `git push`.
7. Acesse seu Fork no GitHub e abra um **Pull Request** direcionado ao repositório original.

As contribuições serão analisadas antes de serem incorporadas ao repositório oficial.

## 2. Organização dos arquivos

As soluções devem ser organizadas por plataforma e identificador do problema.

Exemplo:

```text
maratona-programacao/
├── beecrowd/
│   ├── 1001/
│   │   ├── lucas_sampaio.py
│   │   └── maria_silva.cpp
│   └── 1002/
│       └── joao_santos.py
│
├── codeforces/
│   └── 1000A/
│       └── lucas_sampaio.cpp
│
└── atcoder/
```

Cada problema deve possuir uma pasta própria, identificada pelo seu código ou número na plataforma.

## 3. Identificação das soluções

Os arquivos devem seguir o padrão:

`nome_sobrenome.extensão`

Exemplos:

- `lucas_sampaio.py`
- `maria_silva.cpp`
- `joao_santos.java`

Quando houver mais de uma solução do mesmo integrante para o mesmo problema, utilize uma identificação complementar, como `lucas_sampaio_v2.py`.

## 4. Requisitos das soluções

As soluções submetidas devem atender aos seguintes critérios:

- Resolver corretamente o problema proposto.
- Respeitar o formato de entrada e saída especificado no enunciado.
- Ser compatíveis com a linguagem e a versão utilizadas pela plataforma.
- Apresentar código organizado e legível.
- Evitar arquivos desnecessários, executáveis ou temporários.
- Ter sido testadas antes da submissão.

As soluções devem ter recebido veredito **Accepted (AC)** na plataforma correspondente.

## 5. Padrão dos commits

Utilize mensagens de commit curtas e descritivas.

Exemplos:

```text
Adiciona solução do problema 1001 em Python
Adiciona solução do problema 1002 em C++
Corrige solução do problema 1001
```

## 6. Pull Requests

Ao abrir um Pull Request, informe:

- Plataforma de origem do problema.
- Código ou identificador da questão.
- Nome do problema.
- Linguagem utilizada.
- Nome do integrante responsável pela solução.
- Link do problema original.

Antes de enviar, verifique se os arquivos estão na pasta correta e se não existem alterações que não estejam relacionadas à contribuição.

## 7. Revisão das contribuições

Os Pull Requests serão avaliados pelos responsáveis pelo Projeto Maratona IFPE/BJ.

Durante a revisão, poderão ser solicitados ajustes relacionados à organização, legibilidade, correção ou qualidade das soluções.

Uma contribuição somente será incorporada ao repositório oficial após sua aprovação.

## 8. Considerações finais

O repositório é um espaço coletivo de aprendizagem e colaboração. Incentivamos os integrantes a consultar as soluções existentes, estudar diferentes abordagens e compartilhar conhecimentos.

**Bons estudos e bons códigos!**

Equipe do Projeto Maratona — IFPE/BJ.
