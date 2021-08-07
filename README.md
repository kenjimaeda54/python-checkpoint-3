# python-checkpoint-3

# Python

Checkpoint 3 , cadastros de alunos e suas respectivas oficinas

# Colégio Nova Esperança - Evento literário

Checkpoint 3.

## Tabelas de conteúdos

- Visão geral
  - <a href='#Desafio' > Desafio </a>
  - <a href='#Construção' > Construção </a>
  - <a href='#o-que-eu-aprendi' > Aprendizado </a>
  - <a href='#Feature' > Feature </a>

## Visão Geral

## Desafio

- Cadastrar alunos,com suas respectivas series,Rm e nome
- Cadastrar as oficinas escolhidas pelos alunos

## Construção

![VSCode](https://img.shields.io/badge/-VSCode-0085D1?style=flat-square&logo=visual-studio-code&logoColor=white)
![Git](https://img.shields.io/badge/-Git-F05032?style=flat-square&logo=git&logoColor=white)
![python](https://img.shields.io/badge/-reactnative-212121?style=flat-square&logo=python&logoColor=white)
!

## O que eu aprendemos

Utilizar controles de fluxo(if,else),controles de lop(funções recursivas,for),utilização de funções para filtrar,mapear,sorted, listas...

Utilizamos recurso de recursividade disponível no python,para fazer o laço na aplicação

```python
 def initial(selected)
   if(selected == 1)
    ....


 initial(0)
```

Utilizamos recursos de listas para facilitar na construção da relação entre dependências,
usuário e suas oficinas.
Então de forma dinâmica os valores eram inseridos nos seus respectivos campos.
Usamos o recurso de append para inserir os valores.

```typeScript
tuplaStudents = [
    {
        "name": "",
        "rm": "",
        "serie": "",
        "workshop": [""]
    },

],


  listStudents.append({
                       "name": studentsName,
                        "rm": str(studentsRm),
                        "serie": studentsSerie,
                        "workshop": []
                      }),
```

Usamos bastante do aproveite de uso de funções,para evitar quebras de estouro em memorias, pelos
laços na aplicação.
Exemplo em getChoseUser esta função e sempre chamada e executada dentro do nosso while,
quando nosso lop atingir a quantidade igual ao comprimento da nossa lista,vai inferir,
os valores na função e vamos aproveitar isto para usar em outro espaço do código, para realizar
a logica de filtragem do aluno. Selecionado pela oficina, rm e serie.

```python
  while(i <= len(getWorkShopAfternoon)):
                        print(i, "-->", getWorkShopAfternoon[i])
                        i += 1
                        if(i == len(getWorkShopAfternoon)):
                            return getChoseUser(getSerieStudent, getWorkShopAfternoon, getWorkShopMorning, requestRm)



 def getChoseUser(series, workShopAfternoon, workShopMorning, requestRm):

   .....

```

Reaproveitamos funções para formatar as tabelas de acordo com nosso caso de uso, com uma única função aproveitamos em dois momentos do código,imprimindo para o usuário de forma amigável os valores desejados</br>

```python

 if(len(students["workshop"]) > 0):
                        print("Oficina")
                        i = 1
                        for x in range(len(students["workshop"])):
                            formatWorkshop(students["workshop"][x])
                            i += 1
                        if(i == len(students["workshop"])):
                            initial(5)

#----------------------------------------

 for x in range(len(students["workshop"])):
                        print("\n")
                        formatWorkshop(students["workshop"][x])
                        print("RM", students["rm"], "---",
                              students["name"], "---", students["serie"])
                        i += 1
                    if(i == len(students["workshop"])):
                        initial(5)


#----------------------------------
def formatWorkshop(workShop):
    if(workShop == "Criar e contar historias"):
        return print(workShop, ",segunda-feira, matutino")
    if(workShop == "A língua de sinais"):
        return print(workShop, ",quarta-feira,matutino")
    if(workShop == "Teatro:Luz camera e ação"):
        return print(workShop, ",terça-feria,matutino")
    if(workShop == "Expressão Artística"):
        return print(workShop, ",quinta-feira,matutino")

    .....

```

Com função sorted, nos ordenamos em ordem alfabética nossas listas.</br>
Nós usamos uma função anonima(lambda) e também passamos o parâmetro que desejávamos formatar,
no caso pelo nome do usuário(student["name"]).
Aproveitamos bastante dos recursos do paradigma funcional disponível no Python,usamos bastante as feature filter,map nos códigos. Alguns momentos usando função anonima(lambda) e outras definindo nossas próprias funções.

```python
     newList = sorted(listStudents, key=lambda student: student["name"])
#------------------------------

    newList = sorted(listStudents, key=lambda student: student["name"])

#------------------------------

    def getListOfRm(x):
                      if(x["rm"] == requestRm):
                         checkWorkshop = list(filter(lambda x: x ==
                                                            workshop, x["workshop"]))
                         if(checkWorkshop):
                           print("Nao foi possível registrar,voce ja possui essa oficina no cadastro")
                           initial(5)
              ......


    filter(getListOfRm, listStudents)) or print("Esta oficina atingiu o limite de registros")

```

Usamos a função setdefault(), para adicionar em um campo especifico valores que desejamos.
Essa função,primeiro definimos uma chave,no caso o nome era "workshop". Caso esta chave nao exista ela sera criada. Apos isto definimos oque desejamos fazer com essa chave,nosso caso uso era para adicionar uma lista com os nomes da oficina.

```python
 x.setdefault("workshop", []).append(workshop)
 quantity = len(x["workshop"])
 print("Cadastro feito sucesso!")
 print("Voce possui no total", quantity, quantity >= 2 and "inscrições" or "inscrição")
```

# Feature

- Funções
- Listas
- Recursividade
