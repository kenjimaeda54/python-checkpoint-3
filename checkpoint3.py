
tuplaStudents = [
    {
        "name": "",
        "rm": "",
        "serie": "",
        "workshop": [""]
    },

],


[listStudents] = list(tuplaStudents)

listStudents.append

createTellStory = [""]
singLanguage = [""]
lightCameraAction = [""]
expressionArtistic = [""]
spelling = [""]
worldImagination = [""]
createEmoji = [""]
bodySpeak = [""]
readDramatic = [""]
readDinamic = [""]


workShopMorning = [
    {
        "2": ["Criar e contar historias", "A língua de sinais"],
        "3": ["Criar e contar historias", "Teatro:Luz camera e ação", "A língua de sinais"],
        "4": ["Teatro:Luz camera e ação", "Expressão Artística"],
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


def initial(selected):
    if(selected == 5):
        print("\n")
        selected = int(input(
            "Digite 2 para fazer inscricoes\n"
            "Digite 3 para listar as inscricoes\n"
            "Digite 4 para sair do programa\n"))
    if(selected == 0):
        print("\n")
        selected = int(input(
            "Digite de 1 para cadastrar alunos\n"
            "Digite 2 para fazer inscricoes\n"
            "Digite 3 para listar as inscricoes\n"
            "Digite 4 para sair do programa\n"))
        if(selected == 1):
            def registerStudents(choose):
                if(choose == 1):
                    studentsRm = int(input("\nDigite o RM do aluno: "))
                    if(studentsRm == 0):
                        return initial(5)
                    elif(studentsRm != 0):
                        studentsName = str(input("Digite o nome do aluno: "))
                        studentsSerie = int(input(
                            "Por favor coloque  a serie que o aluno esta cursando:\n"
                            "Digite 2 para segunda serie\n"
                            "Digite 3 para terceira serie \n"
                            "Digite 4 para quarta serie\n"
                            "Digite 5 para quinta serie\n"))
                        if studentsSerie == 2 or studentsSerie == 3 or studentsSerie == 4 or studentsSerie == 5:
                            resultsRm = list(
                                filter(lambda students: students["rm"] == str(studentsRm), listStudents))
                            if(resultsRm):
                                print(
                                    "\nPor favor verifique suas credenciais rm igual")
                                registerStudents(1)
                            else:
                                listStudents.append({
                                    "name": studentsName,
                                    "rm": str(studentsRm),
                                    "serie": studentsSerie,
                                    "workshop": []
                                }),

                                registerStudents(1)
                        else:
                            print("\nDigitou opção invalida repita operação")
                            registerStudents(1)
            registerStudents(1)
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
                    print("--> Segue abaixo as oficinais no periodo da manha")
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
                print("\n --> Segue abaixo as oficinais no periodo do verpertino")
                if(i == len(getWorkShopAftermon)):
                    print(i, "-->", getWorkShopAftermon[i])
                    return getChoseUser(getSerieStudent, getWorkShopAftermon, getWorkShopMorning, requestRm)
                else:
                    while(i <= len(getWorkShopAftermon)):
                        print(i, "-->", getWorkShopAftermon[i])
                        i += 1
                        if(i == len(getWorkShopAftermon)):
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
                    if(selectedWorkshop >= len(workShopMorning)):
                        print(
                            "Opção invalida Selecione numero de acordo com os valores na esquerda da oficina")
                        getChoseUser(series, workShopAfternon,
                                     workShopMorning, requestRm)
                    else:
                        workshop = workShopMorning[selectedWorkshop]

                        def getListOfRm(x):
                            if(x["rm"] == requestRm):
                                checkWorkshop = list(filter(lambda x: x ==
                                                            workshop, x["workshop"]))
                                if(checkWorkshop):
                                    print(
                                        "Nao foi possível registrar,voce ja possui essa oficina no cadastro")
                                    initial(5)
                                else:
                                    x.setdefault(
                                        "workshop", []).append(workshop)
                                    quantity = len(x["workshop"])
                                    print("Cadastro feito sucesso!")
                                    print("Voce possui no total", quantity, quantity >=
                                          2 and "inscrições" or "inscrição")
                                    initial(5)
                        isAddWorkshop(workshop) and list(
                            filter(getListOfRm, listStudents)) or print("Esta oficina atingiu o limite de registros")
                        initial(5)
                elif(selectedPeriod == 1):
                    selectedWorkshop = int(input(
                        "Agora digite o numero que esta ao lado esquerdo da oficina que voce deseja cadastrar: "))
                    if(selectedWorkshop >= len(workShopAfternon)):
                        print(
                            "Opção invalida Selecione numero de acordo com os valores na esquerda da oficina")
                        getChoseUser(series, workShopAfternon,
                                     workShopMorning, requestRm)
                    else:
                        workshop = workShopAfternon[selectedWorkshop]
                    # listWorkshop = ("workshop", workshop)

                        def getListOfRm(x):
                            if(x["rm"] == requestRm):
                                checkWorkshop = list(filter(lambda x: x ==
                                                            workshop, x["workshop"]))
                                if(checkWorkshop):
                                    print(
                                        "Nao foi possível registrar,voce ja possui essa oficina no cadastro")
                                    initial(5)
                                else:
                                    x.setdefault(
                                        "workshop", []).append(workshop)
                                    quantity = len(x["workshop"])
                                    print("Cadastro feito sucesso!")
                                    print("Voce possui no total", quantity, quantity >=
                                          2 and "inscrições" or "inscrição")
                                    initial(5)
                        isAddWorkshop(workshop) and list(
                            filter(getListOfRm, listStudents)) or print("Esta oficina atingiu o limite de registros")
                    initial(5)
            list(map(getSerieStudent, listStudents))
        else:
            print(
                "\nALuno não cadastrado.Por favor procurar a coordenação do Fundamental 1 ")
            initial(5)

    if(selected == 3):
        selectedOption = int(
            input("Selecione 1 para listar por aluno ou 2 por lista de oficina:"))
        if(selectedOption == 1):
            print("***** Alunos inscritos – Ordem: Alfabética (nome) *****")

            def byOderName(students):
                if(students["name"]):
                    print("\nRm:", students["rm"], "--", students["name"],
                          "--", students["serie"], "৹.serie",)
                    if(len(students["workshop"]) > 0):
                        print("Oficina")
                        i = 1
                        for x in range(len(students["workshop"])):
                            formatedWorkshop(students["workshop"][x])
                            i += 1
                        if(i == len(students["workshop"])):
                            initial(5)
                    else:
                        return

            newList = sorted(listStudents, key=lambda student: student["name"])
            list(map(byOderName, newList))
            initial(5)
        elif(selectedOption == 2):
            print("***** Alunos inscritos – Ordem: Alfabética (Oficinas) *****")

            def byOrderWorkshop(students):
                if(len(students["workshop"]) > 0):
                    i = 1
                    for x in range(len(students["workshop"])):
                        print("\nOficinas")
                        formatedWorkshop(students["workshop"][x])
                        print("RM", students["rm"], "---",
                              students["name"], "---", students["serie"])
                        i += 1
                    if(i == len(students["workshop"])):
                        initial(5)
                else:
                    return
            newList = sorted(
                listStudents, key=lambda student: student["workshop"])
            list(map(byOrderWorkshop, newList))

        else:
            print("Por favor repita a operação,colocou valor invaldo")
            initial(3)

    else:
        print("Esse comando não existe!")


def formatedWorkshop(workShop):
    if(workShop == "Criar e contar historias"):
        return print(workShop, ",segunda-feira, matutino")
    if(workShop == "A língua de sinais"):
        return print(workShop, ",quarta-feira,matutino")
    if(workShop == "Teatro:Luz camera e ação"):
        return print(workShop, ",terça-feria,matutino")
    if(workShop == "Expressão Artística"):
        return print(workShop, ",quinta-feira,matutino")
    if(workShop == "Soletrando"):
        return print(workShop, ",sexta-feira, matutino")
    if(workShop == "O mundo da imaginação"):
        return print(workShop, ",quarta-feira, vespertino")
    if(workShop == "Criando e recriando emojis"):
        return print(workShop, ",sexta-feira,vespertino")
    if(workShop == "O Corpo fala"):
        return print(workShop, ",terça-feira,vespertino")
    if(workShop == "Leitura dramática"):
        return print(workShop, ",segunda-feira,vespertino")
    if(workShop == "Leitura dinâmica"):
        return print(workShop, ",quinta-feira,vespertino")


def isAddWorkshop(workshopSelected):
    if(workshopSelected == "Criar e contar historias"):
        if(len(createTellStory) == 10):
            return False
        else:
            createTellStory.append(workshopSelected)
            return True
    if(workshopSelected == "A língua de sinais"):
        if(len(singLanguage) == 10):
            return False
        else:
            singLanguage.append(workshopSelected)
            return True
    if(workshopSelected == "Teatro:Luz camera e ação"):
        if(len(lightCameraAction) == 10):
            return False
        else:
            lightCameraAction.append(workshopSelected)
            return True
    if(workshopSelected == "Expressão Artística"):
        if(len(expressionArtistic) == 10):
            return False
        else:
            expressionArtistic.append(workshopSelected)
            return True
    if(workshopSelected == "Soletrando"):
        if(len(spelling) == 10):
            return False
        else:
            spelling.append(workshopSelected)
            return True
    if(workshopSelected == "O mundo da imaginação"):
        if(len(worldImagination) == 10):
            return False
        else:
            worldImagination.append(workshopSelected)
            return True
    if(workshopSelected == "Criando e recriando emojis"):
        if(len(createEmoji) == 10):
            return False
        else:
            createEmoji.append(workshopSelected)
            return True
    if(workshopSelected == "O Corpo fala"):
        if(len(bodySpeak) == 10):
            return False
        else:
            bodySpeak.append(workshopSelected)
            return True
    if(workshopSelected == "Leitura dramática"):
        if(len(readDramatic) == 10):
            return False
        else:
            readDramatic.append(workshopSelected)
            return True
    if(workshopSelected == "Leitura dinâmica"):
        if(len(readDinamic) == 10):
            return False
        else:
            readDinamic.append(workshopSelected)
            return True


print("Ola seja bem vindo")
initial(0)
