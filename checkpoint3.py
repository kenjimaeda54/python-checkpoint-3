tuplaStudents = [
    {
        "name": "",
        "rm": "",
        "serie": "",
    },

],

[listStudents] = list(tuplaStudents)

listStudents.append

createTellStory = [""]
singLanguage = [""]
lightCameraAction = [""]
expressionArtistic = [""]
spelling = [""]


workShopMorning = [
    {
        "2": ["Criar e contar historias", "A língua de sinais"],
        "3": ["Criar e contar historias", "Teatro:Luz camera e ação", " A língua de sinais"],
        "4": ["Teatro: luz camera e ação", "Expressão Artística"],
        "5": ["A língua de sinais", "Soletrando", "Expressão Artística"]
    },
]


workShopAfternon = [
    {
        "2": ["O mundo da imaginação", "Criando e recriando emojis"],
        "3": ["O Corpo fala"],
        "4": ["Leitura dramática"],
        "5": ["Leitura dinâmica"],
    }
]
# [getItem] = list(map(lambda y: y["5"], workShopStudentsMorning))
# i = 0
# print(getItem)
# i = 0

# while(i <= len(getItem)):
#     print(i, "->", getItem[i])
#     i += 1
#     if(i == len(getItem)):
#         break

# list(map(lambda y: print(y, "->", i += 1), getItem))
# print(armazenaItem)
# while(i <= len(armazenaItem)):
#     print(i, "->", armazenaItem)


# workShopMorning = [
#     {
#         "2": {
#             "Criar e contar historias": createTellStory,
#             "A lingua dos sinais": singLanguage,
#         },
#         "3": {
#             "Criar e contar historias": createTellStory,
#             "Luz camera e ação": lightCameraAction,
#             "A lingua dos sinais": singLanguage,
#         },
#         "4": {
#             "Luz camera e ação": lightCameraAction,
#             "A lingua dos sinais": singLanguage,
#             "Expressão artística": expressionArtistic
#         },
#         "5": {
#             "A lingua dos sinais": singLanguage,
#             "Soletrando": spelling
#         },

#     },

# ]


# [getSerie] = list(map(lambda student: student, workShopMorning))
# print(getSerie)

# worldImagination = [""]
# creatingEmoji = [""]
# bodySpeaks = [""],
# dinamicReading = [""]

# workShopAfternon = [
#     {
#         "2": {
#             "Mundo da imaginação":  worldImagination,
#             "Criando e recriando emojis": creatingEmoji
#         },
#         "3": {
#             "Corpofala":  bodySpeaks,
#         },

#         "4": {
#             "Leitura,dramática":  dinamicReading,
#         },
#         "5": {
#             "Leitura,dinâmica": dinamicReading

#         }
#     },
# ]


# workShopMorning = [
#     {
#         "2": [createTellStory, "Linguagem de sinais"],
#         "3": ["Criar e contar historias", "Luz camera e acao", "A lingua dos sinais"],
#         "4": ["Luz camera e acao", "A lingua dos sinais", "Expressão artística"],
#         "5": ["A lingua dos sinais", "Soletrando"]
#     },

# ]


# workShopAftermon = [
#     {
#         "2": ["Mundo da imaginação", "Criando e recriando emojis"],
#         "3": ["Corpo,fala"],
#         "4": ["Leitura,dramatica"],
#         "5": ["Leitura,dinamica"]
#     },
# ]


# listNumber = [2, 4, 6]

# numbersMY = list(map(lambda x: x*2, listNumber))

# lista = ["pera"]

# listStudents.append({
#     "workshop": lista
# })

# print(listStudents)

def initial(selected):
    if(selected == 0):
        print(listStudents)
        print("\n")
        selected = int(input(
            "Digite de 1 para cadastrar alunos\n"
            "Digite 2 para fazer inscricoes\n"
            "Digite 3 para listar as inscricoes\n"
            "Digite 4 para sair do programa\n"))
    if(selected == 1):
        studentsRm = str(input("\nDigite o RM do aluno: "))
        studentsName = str(input("Digite o nome do aluno: "))
        studentsSerie = int(input(
            "Por favor coloque  a serie que o aluno esta cursando:\n"
            "Digite 2 para segunda serie\n"
            "Digite 3 para terceira serie \n"
            "Digite 4 para quarta serie\n"
            "Digite 5 para quinta serie\n"))
        if studentsSerie == 2 or studentsSerie == 3 or studentsSerie == 4 or studentsSerie == 5:
            resultsRm = list(
                filter(lambda students: students["rm"] == studentsRm, listStudents))
            if(resultsRm):
                print("\nPor favor verifique suas credenciais rm igual")
                initial(0)
            else:
                listStudents.append({
                    "name": studentsName,
                    "rm": studentsRm,
                    "serie": studentsSerie,
                    "workshop": []
                }),

                initial(0)
        else:
            print("\nDigitou opção invalida repita operação")
            initial(0)
    if(selected == 2):
        requestRm = str(input("\nPor favor digite o RM do aluno:"))
        checkRmStudents = list(
            filter(lambda student: student["rm"] == requestRm, listStudents))
        if(checkRmStudents):
            def getSerieStudent(students):
                if(students["rm"] == requestRm):
                    getSerieStudent = str(students["serie"])
                    [getWorkShopMorning] = list(
                        map(lambda students: students[getSerieStudent], workShopMorning))
                    print("0 --> Segue abaixo as oficinais no periodo da manha")
                    i = 0
                    if(i == len(getWorkShopMorning)):
                        print(i, "-->", getWorkShopMorning[i])
                        printAftermon(getSerieStudent,
                                      getWorkShopMorning, requestRm)
                    else:
                        while(i <= len(getWorkShopMorning)):
                            print(i, "-->", getWorkShopMorning[i])
                            i += 1
                            if(i == len(getWorkShopMorning)):
                                return printAftermon(getSerieStudent, getWorkShopMorning, requestRm)

            def printAftermon(getSerieStudent, getWorkShopMorning, requestRm):
                i = 0
                [getWorkShopAftermon] = list(
                    map(lambda students: students[getSerieStudent], workShopAfternon))
                print("\n 1--> Segue abaixo as oficinais no periodo do verpertino")
                if(i == len(getWorkShopAftermon)):
                    print(i, "-->", getWorkShopAftermon[i])
                    return getChoseUser(getSerieStudent, getWorkShopAftermon, getWorkShopMorning, requestRm)
                else:
                    while(i <= len(getWorkShopAftermon)):
                        print(i, "-->", getWorkShopAftermon[i])
                        i += 1
                        if(i <= len(getWorkShopAftermon)):
                            return getChoseUser(getSerieStudent, getWorkShopAftermon, getWorkShopMorning, requestRm)

            def getChoseUser(series, workShopAfternon, workShopMorning, requestRm):
                selectedPeriod = int(input(
                    "\nPor favor selecione 0 para oficina do periodo manha ou 1 para vespertino: "))
                print(selectedPeriod)
                if(selectedPeriod != 0 and selectedPeriod != 1):
                    print("Opção invalida")
                    getChoseUser(series, workShopAfternon,
                                 workShopMorning, requestRm)
                elif(selectedPeriod == 0):
                    selectedWorkshop = int(input(
                        "Agora digite o numero que esta ao lado esquerdo da oficina que voce deseja cadastrar: "))
                    if(selectedWorkshop > len(workShopMorning)):
                        print(
                            "Opção invalida Selecione numero de acordo com os valores na esquerda da oficina")
                        getChoseUser(series, workShopAfternon,
                                     workShopMorning, requestRm)
                    else:
                        workshop = workShopMorning[selectedWorkshop]
                        # listWorkshop = ("workshop", workshop)

                        def getListOfRm(x):
                            if(x["rm"] == requestRm):
                                if(len(x["workshop"]) == 2):
                                    print(
                                        "Aluno ja atingiu a quantidade maxima permitida")
                                    initial(0)
                                else:
                                    x.setdefault(
                                        "workshop", []).append(workshop)

                        list(filter(getListOfRm, listStudents))
                        print("Cadastro com sucesso!")
                        initial(0)
                elif(selectedPeriod == 1):
                    selectedWorkshop = int(input(
                        "Agora digite o numero que esta ao lado esquerdo da oficina que voce deseja cadastrar: "))
                    if(selectedWorkshop > len(workShopMorning)):
                        print(
                            "Opção invalida Selecione numero de acordo com os valores na esquerda da oficina")
                        getChoseUser(series, workShopAfternon,
                                     workShopMorning, requestRm)
                    else:
                        workshop = workShopAfternon[selectedWorkshop]
                    # listWorkshop = ("workshop", workshop)

                        def getListOfRm(x):
                            if(x["rm"] == requestRm):
                                if(len(x["workshop"]) == 2):
                                    print(
                                        "Aluno ja atingiu a quantidade maxima permitida")
                                    initial(0)
                                else:
                                    x.setdefault(
                                        "workshop", []).append(workshop)

                    list(filter(getListOfRm, listStudents))
                    print("Cadastro com sucesso!")
                    initial(0)
            list(map(getSerieStudent, listStudents))
        # getWorkshop = list(
        #     map(lambda students: students == requestRm, workShopMorning))
        # print("Oficinas disponíveis no peridodo da manha", getWorkshop)
        else:
            print(
                "\nALuno não cadastrado.Por favor procurar a coordenação do Fundamental 1 ")
            initial(0)

    # if(selected == 3):
    #     print("Numero 3 foi chamado")
    #     initial(0)

    else:
        print("Esse comando não existe!")


print("Ola seja bem vindo")
initial(0)
