import tkinter as tk 

numero = 0

def lerNome():   
    global numero
    numero += 1
    labelResult.config(text=f"{numero}") # escrevendo label
    inputNome.delete(0, tk.END) #escrevendo no inputText
    inputNome.insert(0, numero)


janela = tk.Tk() #criação da janela principal
janela.title("Minha Janela principal")  #titulo da janela
janela.geometry("600x400") #dimensões da tela

labelNome = tk.Label(janela, text="Contador")
labelNome.pack()

inputNome = tk.Entry(janela)
inputNome.pack()

labelResult = tk.Label(janela, text="Resultado")
labelResult.pack()

botao = tk.Button(janela, text="Ler", command=lerNome )
botao.pack()

janela.mainloop() #looping que mantem a janela aberta
