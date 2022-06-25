import pyautogui
import time

mensagens = list()
sim = True
while sim:
    mensagens.append(str(input("Digite a mensagem: ")).strip())
    resp = str(input("Deseja adicionar mais alguma mensagem? [S/N]").strip().upper())
    if resp not in 'NSsn':
        print("Erro... Digite novamente")
    elif resp in 'N':
        sim = False
    else:
        sim = True


def BotZap(mensagem):
    time.sleep(20)
    while True:
        for texto in mensagem:
            pyautogui.typewrite(texto)
            pyautogui.press("enter")


BotZap(mensagens)
