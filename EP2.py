import random
import json
import time
import ast


meus_inspermons={"Aluno": [56, 32, 100]} #poder ataque -> poder defesa -> vida
inspermons_selvagens = {"Romero": [60, 32, 100],
                        "Hage": [56, 31, 100],
                        "Fernando": [46, 33, 100],
                        "Betao": [58, 28, 100],
                        "Ferraz": [43, 28, 100], 
                        "Daniel": [57, 36, 100]}
insperdex = {"Aluno": [56, 32, 100]}


pergunta = input("Voce deseja continuar sua ultima jornada? (essa função apenas funciona se voce tiver dormido na ultima partida) \n'sim' ou\n'nao'\n")
if pergunta == "sim":
    with open("jogo.json", "r") as arquivo:
        lista = []
        for linha in arquivo:
            lista.append(linha) 
    meus_inspermons=dict()
    inspermons_selvagens=dict()
    insperdex=dict()
    meus_inspermons=ast.literal_eval(lista[0])
    inspermons_selvagens=ast.literal_eval(lista[1])
    insperdex=ast.literal_eval(lista[2])
    

def batalha (VidaInspermon, VidaPlayer, PoderPlayer, PoderIspermon, DefesaInspermon, DefesaPlayer):
    while VidaPlayer > 0 and VidaInspermon > 0:
        VidaInspermon = VidaInspermon - (PoderPlayer - DefesaInspermon)
        if VidaInspermon <= 0:
            meus_inspermons["Aluno"][0] = meus_inspermons["Aluno"][0] + 1
            meus_inspermons["Aluno"][1] = meus_inspermons["Aluno"][1] + 1
            insperdex["Aluno"][0] = insperdex["Aluno"][0] + 1
            insperdex["Aluno"][1] = insperdex["Aluno"][1] + 1
            return "Voce venceu a batalha"
        VidaPlayer = VidaPlayer - (PoderIspermon - DefesaPlayer)
        if VidaPlayer <= 0:
            return "Voce perdeu a batalha"


def batalhaSorte(VidaInspermon, VidaPlayer, PoderPlayer, PoderIspermon, DefesaInspermon, DefesaPlayer):
    while VidaPlayer > 0 and VidaInspermon > 0:
        VidaInspermon = VidaInspermon - (PoderPlayer - DefesaInspermon)
        if VidaInspermon <= 0:
            return "Voce perdeu a batalha"
        VidaPlayer = VidaPlayer - (PoderIspermon - DefesaPlayer)
        if VidaPlayer <= 0:
            meus_inspermons["Aluno"][0] = meus_inspermons["Aluno"][0] + 1
            meus_inspermons["Aluno"][1] = meus_inspermons["Aluno"][1] + 1
            insperdex["Aluno"][0] = insperdex["Aluno"][0] + 1
            insperdex["Aluno"][1] = insperdex["Aluno"][1] + 1
            return "Voce venceu a batalha"


meus_inspermons_str = json.dumps(meus_inspermons) 
inspermons_selvagens_str = json.dumps(inspermons_selvagens)
insperdex_str = json.dumps(insperdex)
arquivo = open ("jogo.json", "w")
arquivo.write(meus_inspermons_str)
arquivo.write(inspermons_selvagens_str)
arquivo.write(insperdex_str)

laco=1
while laco:
    time.sleep(1)
    pergunta_inicial=input("Voce deseja: \n'passear';\n'ver inspermons';\n'ver insperdex';\n'dormir'? ")
    if pergunta_inicial=="ver insperdex":
        print(insperdex)
    elif pergunta_inicial=="ver inspermons":
        print(meus_inspermons)
    elif pergunta_inicial=="dormir":
          print ("Até logo!")
          break
    elif pergunta_inicial=="passear":
        inspermon = str(random.choice(list(inspermons_selvagens.items())))
        inspermon = inspermon.replace("('Romero', [60, 32, 100])", "Romero")
        inspermon = inspermon.replace("('Hage', [56, 31, 100])", "Hage")
        inspermon = inspermon.replace("('Fernando', [46, 33, 100])", "Fernando")
        inspermon = inspermon.replace("('Betao', [58, 28, 100])", "Betao")
        inspermon = inspermon.replace("('Ferraz', [43, 28, 100])", "Ferraz")
        inspermon = inspermon.replace("('Daniel', [57, 36, 100])", "Daniel")
        insperdex [inspermon] = inspermons_selvagens [inspermon]
        time.sleep(1)
        print("Um {} selvagem acabou de aparecer!".format(inspermon))
        while True:
            time.sleep(1)
            luta=input("Voce deseja:\n'batalhar',\n'fugir'\ntentar 'capturar'? ")
            if luta == "batalhar":
                time.sleep(1)
                aleatorio5 = random.randint (0,9)
                if aleatorio5 > 1:
                    inspermon_utilizado=input("Dentre os inspermons a baixo:\n"+str(meus_inspermons)+"\nqual voce deseja utilizar? ")
                    if inspermon_utilizado=="Aluno" or "Hage" or "Betao" or "Fernando" or "Romero" or "Daniel" or "Ferraz":
                        print("Se prepare para a batalha!")
                        time.sleep(1)
                        print("O duelo esta ocorrendo!")
                        time.sleep(1)
                        print(batalha (100, 100, meus_inspermons[inspermon_utilizado][0], inspermons_selvagens[inspermon][0], inspermons_selvagens[inspermon][1], meus_inspermons[inspermon_utilizado][1]))
                        break
                if aleatorio5 <= 1:
                    inspermon_utilizado=input("Dentre os inspermons a baixo:\n"+str(meus_inspermons)+"\nqual voce deseja utilizar? ")
                    if inspermon_utilizado=="Aluno" or "Hage" or "Betao" or "Fernando" or "Romero" or "Daniel" or "Ferraz":
                        print("Se prepare para a batalha!")
                        time.sleep(1)
                        print("O duelo esta ocorrendo!")
                        time.sleep(1)
                        print(batalhaSorte (100, 100, meus_inspermons[inspermon_utilizado][0], inspermons_selvagens[inspermon][0], inspermons_selvagens[inspermon][1], meus_inspermons[inspermon_utilizado][1]))
                        break
            elif luta == "fugir":
                aleatorio=random.randint(0, 9)
                if aleatorio >5:
                    time.sleep(1)
                    print("Sua fuga foi um fracasso!\nVoce tera de batalhar!")
                    time.sleep(1)
                    aleatorio5 = random.randint (0,9)
                    if aleatorio5 > 1:
                        inspermon_utilizado=input("Dentre os inspermons a baixo:\n"+str(meus_inspermons)+"\nqual voce deseja utilizar? ")
                        if inspermon_utilizado=="Aluno" or "Hage" or "Betao" or "Fernando" or "Romero" or "Daniel" or "Ferraz":
                            print("Se prepare para a batalha!")
                            time.sleep(1)
                            print("O duelo esta ocorrendo!")
                            time.sleep(1)
                            print(batalha (100, 100, meus_inspermons[inspermon_utilizado][0], inspermons_selvagens[inspermon][0], inspermons_selvagens[inspermon][1], meus_inspermons[inspermon_utilizado][1]))
                            break
                    if aleatorio5 <= 1:
                        inspermon_utilizado=input("Dentre os inspermons a baixo:\n"+str(meus_inspermons)+"\nqual voce deseja utilizar? ")
                        if inspermon_utilizado=="Aluno" or "Hage" or "Betao" or "Fernando" or "Romero" or "Daniel" or "Ferraz":
                            print("Se prepare para a batalha!")
                            time.sleep(1)
                            print("O duelo esta ocorrendo!")
                            time.sleep(1)
                            print(batalhaSorte (100, 100, meus_inspermons[inspermon_utilizado][0], inspermons_selvagens[inspermon][0], inspermons_selvagens[inspermon][1], meus_inspermons[inspermon_utilizado][1]))
                            break
                    else:
                        print("Esse inspermon não é existente na sua lista (lembre da letra maiuscula)")
                if aleatorio <=5:
                    time.sleep(1)
                    print("Sua fuga foi um sucesso! A batalha terminou em empate.")
                    break
            elif luta == "capturar":
                time.sleep(1)
                inspermon_utilizado=input("Dentre os inspermons a baixo:\n"+str(meus_inspermons)+"\nqual voce deseja utilizar para a captura? ")
                aleatorio2=random.randint(0, 9)
                if meus_inspermons[inspermon_utilizado][0] > inspermons_selvagens[inspermon][0]:
                    if aleatorio2 <= 6:
                        time.sleep(1)
                        print("Voce capturou o inspermon selvagem!") 
                        meus_inspermons[inspermon] = inspermons_selvagens[inspermon]
                        break
                    if aleatorio2 > 6:
                        time.sleep(1)
                        print("Voce nao conseguiu captura-lo e o " + inspermon + " selvagem conseguiu fugir")
                        break
                if meus_inspermons[inspermon_utilizado][0] <= inspermons_selvagens[inspermon][0]:
                    if aleatorio2 >= 7:
                        time.sleep(1)
                        print("Voce capturou o inspermon selvagem!") 
                        meus_inspermons[inspermon] = inspermons_selvagens[inspermon]
                        break
                    if aleatorio2 < 7:
                        time.sleep(1)
                        print("Voce nao conseguiu captura-lo e o " + inspermon + " selvagem conseguiu fugir")
                        break
            else:
                print("Essa opção não existe, escolha entre 'batalhar', 'fugir' ou 'capturar")
    else:
         print("Essa opção nao existe, escolha entre: passear, dormir, ver inspermons ou ver insperdex")


with open ("jogo.json", "w") as arquivo:
    arquivo.write(str(meus_inspermons))
    arquivo.write(str("\n"))
    arquivo.write(str(inspermons_selvagens))
    arquivo.write(str("\n"))
    arquivo.write(str(insperdex))
    #arquivo.write(str("\n"))
    #arquivo.write(str("brunoartc")
