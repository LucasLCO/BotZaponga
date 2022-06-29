import pyautogui
import time

mensagens = list()
sim = True

def BotZap(modo):
    if modo == 'M':
        while sim:
            mensagens.append(str(input("Digite a mensagem: ")).strip())
            resp = str(input("Deseja adicionar mais alguma mensagem? [S/N]").strip().upper())
            if resp not in 'NSsn':
                print("Erro... Digite novamente")
            elif resp in 'N':
                sim = False
            else:
                sim = True
        time.sleep(20)
        while True:
            for texto in mensagens:
                pyautogui.typewrite(texto)
                pyautogui.press("enter")
    elif modo == 'F':
        time.sleep(20)
        while True:
            pyautogui.click()
