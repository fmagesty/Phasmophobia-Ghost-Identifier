# Objetivo: usar user input para identelificar o tipo de fantasma no phasmophobia de acordo com as 3 evidencias de cada tipo de fantasma.
# Tabela de referencia: https://i.imgur.com/HYd7aOG.jpg
# PROJETO CONCLUIDO COM SUCESSO DIA 5 DE NOVEMBRO 2020 - versao 1.0

# Update versao 1.1.0 dia 8 de novembro 2020: adicionadas possiveis evidencias para cada possibilidade de fantasma e adicionadas descricoes de cada fantasma apos 3 evidencias
# Update versao 1.1.1 dia 12 de novembro 2020: adicionada condicao para input incorreto (que nao corresponde a nenhuma evidencia). o programa entao ira dizer que o input esta incorreto e pede para digitar uma das evidencias descritas.
# Update versao 1.1.2 dia 13 de novembro 2020: corrigido erro ao digitar evidencia repetida dava o nome de fantasmas repetidos. exemplo: orb+book+book
# Update versao 1.1.3 dia 15 de novembro 2020: corrigido erro ao digitar evidencias que nao sao possiveis eram lidas pelo programa como correto. exemplo: box, orb, book (neste caso 'book' nao eh uma possivel evidencia junto com box e orb)
# Update versao 1.1.4 dia 8 de dezembro 2020: agora o input eh feito com pyinputplus ao inves do input regular
# Update versao 1.1.5 dia 23 de janeiro 2021: usando inputMenu ao inves de inputChoice por razao estetica
# Update versao 2.1.5 dia 25 janeiro 2021: criada GUI para o programa. Ainda rudimentar, falta polimento.

# TODO: adicionar botoes para escolher evidences no lugar de input escrito

import pyinputplus as pyip
from PySimpleGUI import PySimpleGUI as sg

Shade = ["emf", "orb", "book"]  
Phantom = ["emf", "orb", "temp"]
Jinn = ["emf", "orb", "box"]
Yurei = ["orb", "book", "temp"]
Mare = ["orb", "temp", "box"]
Demon = ["book", "temp", "box"]
Banshee = ["emf", "temp", "prints"]
Revenant = ["emf", "book", "prints"]
Oni = ["emf", "book", "box"]
Poltergeist = ["orb", "box", "prints"]
Spirit = ["book", "box", "prints"]
Wraith =  ["temp", "box", "prints"]
Ghost_Id_First_Evidence = []
Ghost_Id_Second_Evidence = []
Ghost_Id_Third_Evidence = []
Possible_Evidences_1 = []
Possible_Evidences_2 = []
Possible_Evidences_3 = []

# Layout
sg.theme('DarkBlack')
layout = [
    [sg.Text('Select first evidence:', justification='left', size=(100,1), text_color='red')],
    [sg.Input(key='input1', size=(10,1)), sg.Button('OK', key='ok1')],
    [sg.Text('Select second evidence:', justification='left', size=(100,1), text_color='red')],
    [sg.Input(key='input2', size=(10,1)), sg.Button('OK', key='ok2')],
    [sg.Text('Select third evidence:', justification='left', size=(100,1), text_color='red')],
    [sg.Input(key='input3', size=(10,1)), sg.Button('OK', key='ok3')],
    [sg.Text('Possible ghosts:', justification='left', size=(50,1), text_color='red')],
    [sg.Text('The possible ghosts appear here.', key='outputGhosts', size=(50,1))],
    [sg.Text('Possible evidences:', key='possibleEvidences', justification='left', size=(50,1), text_color='red')],
    [sg.Text('The possible evidences appear here.', key='outputEvidences', size=(100,3))],
    [sg.Button('Reset', key='-RESET-')]
]
# Janela
window = sg.Window('Ghost Identifier by fmagesty', layout)
# Ler os eventos
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break

# Evidence 1
    if event == 'ok1':
        evidence_1 = values['input1']
        
        if evidence_1 in Shade:
            Ghost_Id_First_Evidence.append("Shade")
            for i in Shade:
                Possible_Evidences_1.append(i)

        if evidence_1 in Phantom:       
            Ghost_Id_First_Evidence.append("Phantom")
            for i in Phantom:
                Possible_Evidences_1.append(i)

        if evidence_1 in Jinn:
            Ghost_Id_First_Evidence.append("Jinn")
            for i in Jinn:
                Possible_Evidences_1.append(i)

        if evidence_1 in Yurei:
            Ghost_Id_First_Evidence.append("Yurei")
            for i in Yurei:
                Possible_Evidences_1.append(i)

        if evidence_1 in Mare:
            Ghost_Id_First_Evidence.append("Mare")
            for i in Mare:
                Possible_Evidences_1.append(i)

        if evidence_1 in Demon:
            Ghost_Id_First_Evidence.append("Demon")
            for i in Demon:
                Possible_Evidences_1.append(i)

        if evidence_1 in Banshee:
            Ghost_Id_First_Evidence.append("Banshee")
            for i in Banshee:
                Possible_Evidences_1.append(i)

        if evidence_1 in Revenant:
            Ghost_Id_First_Evidence.append("Revenant")
            for i in Revenant:
                Possible_Evidences_1.append(i)

        if evidence_1 in Oni:
            Ghost_Id_First_Evidence.append("Oni")
            for i in Oni:
                Possible_Evidences_1.append(i)

        if evidence_1 in Poltergeist:
            Ghost_Id_First_Evidence.append("Poltergeist")
            for i in Poltergeist:
                Possible_Evidences_1.append(i)

        if evidence_1 in Spirit:
            Ghost_Id_First_Evidence.append("Spirit")
            for i in Spirit:
                Possible_Evidences_1.append(i)

        if evidence_1 in Wraith:
            Ghost_Id_First_Evidence.append("Wraith")
            for i in Wraith:
                Possible_Evidences_1.append(i)

        Possible_Evidences_1 = set(list(Possible_Evidences_1))

        if evidence_1 == "emf":
            Possible_Evidences_1.remove("emf")

        if evidence_1 == "orb":
            Possible_Evidences_1.remove("orb")

        if evidence_1 == "book":
            Possible_Evidences_1.remove("book")

        if evidence_1 == "temp":
            Possible_Evidences_1.remove("temp")

        if evidence_1 == "box":
            Possible_Evidences_1.remove("box")

        if evidence_1 == "prints":
            Possible_Evidences_1.remove("prints")

    # Output evidences and ghost
    window['outputGhosts'].update(Ghost_Id_First_Evidence)
    window['outputEvidences'].update(Possible_Evidences_1)
    
    # Transform possible evidences back to a list so it can be reset and entered again
    Possible_Evidences_1 = list(Possible_Evidences_1)

# Evidence 2
    if event == 'ok2':
        evidence_2 = values['input2']
        
        if evidence_1 in Shade and evidence_2 in Shade and "Shade" not in Ghost_Id_Second_Evidence:
            Ghost_Id_Second_Evidence.append("Shade")
            for i in Shade:
                Possible_Evidences_2.append(i)

        if evidence_1 in Phantom and evidence_2 in Phantom and "Phantom" not in Ghost_Id_Second_Evidence:
            Ghost_Id_Second_Evidence.append("Phantom")
            for i in Phantom:
                Possible_Evidences_2.append(i)

        if evidence_1 in Jinn and evidence_2 in Jinn and "Jinn" not in Ghost_Id_Second_Evidence:
            Ghost_Id_Second_Evidence.append("Jinn")
            for i in Jinn:
                Possible_Evidences_2.append(i)

        if evidence_1 in Yurei and evidence_2 in Yurei and "Yurei" not in Ghost_Id_Second_Evidence:
            Ghost_Id_Second_Evidence.append("Yurei")
            for i in Yurei:
                Possible_Evidences_2.append(i)

        if evidence_1 in Mare and evidence_2 in Mare and "Mare" not in Ghost_Id_Second_Evidence:
            Ghost_Id_Second_Evidence.append("Mare")
            for i in Mare:
                Possible_Evidences_2.append(i)

        if evidence_1 in Demon and evidence_2 in Demon and "Demon" not in Ghost_Id_Second_Evidence:
            Ghost_Id_Second_Evidence.append("Demon")
            for i in Demon:
                Possible_Evidences_2.append(i)

        if evidence_1 in Banshee and evidence_2 in Banshee and "Banshee" not in Ghost_Id_Second_Evidence:
            Ghost_Id_Second_Evidence.append("Banshee")
            for i in Banshee:
                Possible_Evidences_2.append(i)

        if evidence_1 in Revenant and evidence_2 in Revenant and "Revenant" not in Ghost_Id_Second_Evidence:
            Ghost_Id_Second_Evidence.append("Revenant")
            for i in Revenant:
                Possible_Evidences_2.append(i)

        if evidence_1 in Oni and evidence_2 in Oni and "Oni" not in Ghost_Id_Second_Evidence:
            Ghost_Id_Second_Evidence.append("Oni")
            for i in Oni:
                Possible_Evidences_2.append(i)

        if evidence_1 in Poltergeist and evidence_2 in Poltergeist and "Poltergeist" not in Ghost_Id_Second_Evidence:
            Ghost_Id_Second_Evidence.append("Poltergeist")
            for i in Poltergeist:
                Possible_Evidences_2.append(i)

        if evidence_1 in Spirit and evidence_2 in Spirit and "Spirit" not in Ghost_Id_Second_Evidence:
            Ghost_Id_Second_Evidence.append("Spirit")
            for i in Spirit:
                Possible_Evidences_2.append(i)

        if evidence_1 in Wraith and evidence_2 in Wraith and "Wraith" not in Ghost_Id_Second_Evidence:
            Ghost_Id_Second_Evidence.append("Wraith")
            for i in Wraith:
                Possible_Evidences_2.append(i)

        Possible_Evidences_2 = set(list(Possible_Evidences_2))

        if evidence_1 == "emf" or evidence_2 == "emf":
            Possible_Evidences_2.remove("emf")

        if evidence_1 =="orb" or evidence_2 == "orb":
            Possible_Evidences_2.remove("orb")

        if evidence_1 == "book" or evidence_2 == "book":
            Possible_Evidences_2.remove("book")

        if evidence_1 == "temp" or evidence_2 == "temp":
            Possible_Evidences_2.remove("temp")

        if evidence_1 == "box" or evidence_2 == "box":
            Possible_Evidences_2.remove("box")

        if evidence_1 == "prints" or evidence_2 == "prints":
            Possible_Evidences_2.remove("prints")

    # Output evidences and ghost
        window['outputGhosts'].update(Ghost_Id_Second_Evidence)
        window['outputEvidences'].update(Possible_Evidences_2)

        # Transform possible evidences back to a list so it can be reset and entered again
        Possible_Evidences_2 = list(Possible_Evidences_2)

# Evidence 3
    if event == 'ok3':
        evidence_3 = values['input3']

        if evidence_1 in Shade and evidence_2 in Shade and evidence_3 in Shade and "Shade" not in Ghost_Id_Third_Evidence:
            Ghost_Id_Third_Evidence.append("Shade")

        if evidence_1 in Phantom and evidence_2 in Phantom and evidence_3 in Phantom and "Phantom" not in Ghost_Id_Third_Evidence:
            Ghost_Id_Third_Evidence.append("Phantom")

        if evidence_1 in Jinn and evidence_2 in Jinn and evidence_3 in Jinn and "Jinn" not in Ghost_Id_Third_Evidence:
            Ghost_Id_Third_Evidence.append("Jinn")

        if evidence_1 in Yurei and evidence_2 in Yurei and evidence_3 in Yurei and "Yurei" not in Ghost_Id_Third_Evidence:
            Ghost_Id_Third_Evidence.append("Yurei")

        if evidence_1 in Mare and evidence_2 in Mare and evidence_3 in Mare and "Mare" not in Ghost_Id_Third_Evidence:
            Ghost_Id_Third_Evidence.append("Mare")

        if evidence_1 in Demon and evidence_2 in Demon and evidence_3 in Demon and "Demon" not in Ghost_Id_Third_Evidence:
            Ghost_Id_Third_Evidence.append("Demon")

        if evidence_1 in Banshee and evidence_2 in Banshee and evidence_3 in Banshee and "Banshee" not in Ghost_Id_Third_Evidence:
            Ghost_Id_Third_Evidence.append("Banshee")

        if evidence_1 in Revenant and evidence_2 in Revenant and evidence_3 in Revenant and "Revenant" not in Ghost_Id_Third_Evidence:
            Ghost_Id_Third_Evidence.append("Revenant")

        if evidence_1 in Oni and evidence_2 in Oni and evidence_3 in Oni and "Oni" not in Ghost_Id_Third_Evidence:
            Ghost_Id_Third_Evidence.append("Oni")

        if evidence_1 in Poltergeist and evidence_2 in Poltergeist and evidence_3 in Poltergeist and "Poltergeist" not in Ghost_Id_Third_Evidence:
            Ghost_Id_Third_Evidence.append("Poltergeist")

        if evidence_1 in Spirit and evidence_2 in Spirit and evidence_3 in Spirit and "Spirit" not in Ghost_Id_Third_Evidence:
            Ghost_Id_Third_Evidence.append("Spirit")

        if evidence_1 in Wraith and evidence_2 in Wraith and evidence_3 in Wraith and "Wraith" not in Ghost_Id_Third_Evidence:
            Ghost_Id_Third_Evidence.append("Wraith")

    # Output evidences and ghost
        window['outputGhosts'].update(Ghost_Id_Third_Evidence[0])
        window['possibleEvidences'].update('Ghost description:')
        
        # Transform possible evidences back to a list so it can be reset and entered again
        Possible_Evidences_3 = list(Possible_Evidences_3)

# Prints which ghost it is and a description of it

        if "Shade" in Ghost_Id_Third_Evidence:
            window['outputEvidences'].update("A shade is known to be a shy ghost. There is evidence that a shade will stop all paranormal activity if there are multiple people nearby.\nUnique strenghts: Beign shy means the ghost will be harder to find.\nWeaknesses: the ghost will not enter hunting mode if there is multiple people nearby.")

        if "Phantom" in Ghost_Id_Third_Evidence:
            window['outputEvidences'].update("A phantom is a ghost that can possess the living, most commonly summoned by a Ouija Board. It also induces fear into those around it.\nUnique strenghts: looking at a phantom will considerably drop your sanity.\nWeaknesses: taking a photo of the phantom will make it temporarily disappear.")

        if "Jinn" in Ghost_Id_Third_Evidence:
            window['outputEvidences'].update("A jinn is a territorial ghost that will attack when threatened. It has also been known to be able to travel at significant speed.\nUnique strenghts: a jinn will travel at a faster speed if its victim is far away.\nWeaknesses: turning off the locations power source will prevent the jinn from using its ability.")

        if "Yurei" in Ghost_Id_Third_Evidence:
            window['outputEvidences'].update("A yurei is a ghost that has returned to the physical world, usually for the purpose of revenge or hatred.\nUnique strenghts: yurei's have been known to have a stronger effect on people sanity.\nWeaknesses: smudging the yurei's room will cause it to not wander around the location for a long time.")

        if "Mare" in Ghost_Id_Third_Evidence:
            window['outputEvidences'].update("A mare is the source of all nightmares, making it most powerful in the dark.\nUnique strenghts: a mare will have an increased chance to attack in the dark.\nWeaknesses: turning the lights on around the mare will lower its chance to attack.")

        if "Demon" in Ghost_Id_Third_Evidence:
            window['outputEvidences'].update("A demon is one of the worst ghosts you can encounter. It has been known to attack without a reason.\nUnique strenghts: demons will attack more often than any other ghost.\nWeaknesses: asking a demon successful questions on the ouija board won't lower the users sanity.")

        if "Banshee" in Ghost_Id_Third_Evidence:
            window['outputEvidences'].update("A banshee is a natural hunter and will attack anything. It has been known to stalk its prey one at a time until making its kill.\nUnique strenghts: a banshee will only target one person at a time.\nWeaknesses: banshees fear the crucifix and will be less aggressive when near one.")

        if "Revenant" in Ghost_Id_Third_Evidence:
            window['outputEvidences'].update("A revenant is a slow but violent ghost that will attack indiscriminately. It has been rumored to travel at a significantly high speed when hunting.\nUnique strenghts: a revenant will travel at a significantly faster speed when hunting a victim.\nWeaknesses: hiding from the revenant will cause it to move very slowly.")

        if "Oni" in Ghost_Id_Third_Evidence:
            window['outputEvidences'].update("Oni's are a cousin to the demon and possess extreme strenght. There have been rumours that they become more active around their prey.\nUnique strenghts: Oni's are more active when people are nearby and have been seen moving objects at great speed.\nWeaknesses: beign more active will make the oni easier to find and identify.")

        if "Poltergeist" in Ghost_Id_Third_Evidence:
            window['outputEvidences'].update("One of the most famous ghosts, a Poltergeist, also known as a noisy ghost can manipulate objects around it to spread fear into its victims.\nUnique strenghts: a Poltergeist can throw huge amounts of objects at once.\nWeaknesses: a Poltergeist is almost ineffective in an empty room.")

        if "Spirit" in Ghost_Id_Third_Evidence:
            window['outputEvidences'].update("A spirit is the most common ghost you will come across however it is still very powerful and dangerous. They are usually discovered at one of their hunting grounds after an unexplained death.\nUnique strenghts: nothing.\nWeaknesses: using smudge sticks on a spirit will stop it attacking for a long period of time.")

        if "Wraith" in Ghost_Id_Third_Evidence:
            window['outputEvidences'].update("A wraith is one of the most dangerous ghosts you will find. It is also the only known ghost that has the ability to flight and has sometimes been known to travel trough walls.\nUnique strenghts: wraiths almost never touch the ground, meaning it can't be tracked by footsteps.\nWeaknesses: wraiths have a toxic reaction to salt.")

    if event == '-RESET-':
        window['input1'].update('')
        window['input2'].update('')
        window['input3'].update('')
        window['outputGhosts'].update('The possible ghosts appear here.')
        window['outputEvidences'].update('The possible evidences appear here.')
        window['possibleEvidences'].update('Possible evidences:')
        Ghost_Id_First_Evidence = []
        Ghost_Id_Second_Evidence = []
        Ghost_Id_Third_Evidence = []
        Possible_Evidences_1 = []
        Possible_Evidences_2 = []
        Possible_Evidences_3 = []

window.close()