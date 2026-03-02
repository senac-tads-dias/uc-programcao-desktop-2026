import tkinter as tk

def limpar():
    inputDisplay.delete(0, tk.END)

def calcular():    
    try:
        print("Calcular")
        resultado  = eval(inputDisplay.get())
        limpar()
        inputDisplay.insert(0, str(resultado))       
    except:
        print("Erro")
        limpar()
        inputDisplay.insert(0, "ERROR")
        
def adicionar(valor):
    print("Adicionar caracter")
    inputDisplay.insert(tk.END, valor)


#criando Janela
janela = tk.Tk()
janela.title("Calculadora")
janela.geometry("200x280")

inputDisplay = tk.Entry(janela, font=("Arial", 20), bd=5, width=12, justify="right")
inputDisplay.grid(row=0, column=0, columnspan=4, padx=3, pady=3)

botoes = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('1', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('=', 4, 2), ('+', 4, 3),
]

#Criar os botões com base na lista de tuplas
for(texto, linha, coluna ) in botoes:
    if texto == '=':
        tk.Button(janela, text=texto, width=5, height=2, command=calcular).grid(row=linha, 
                                                                                column=coluna, padx=2, pady=2)
    else:
        tk.Button(janela, text=texto, width=5, height=2, command= lambda t=texto : adicionar(t)).grid(row=linha, 
                                                                                column=coluna, padx=2, pady=2)

#Botão para limpar
botaoLimpar = tk.Button(janela, text="C", width=22, height=2, bg = "blue", fg= "white", command=limpar)
botaoLimpar.grid(row=5, column=0, columnspan=4, padx=2, pady=2)

janela.mainloop()