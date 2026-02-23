import tkinter as tk

def somar():    
    try:
        n1 = float(entrada1.get())
        n2 = float(entrada2.get())
        
        soma = n1 + n2 
        labelResult.config(text=f"Resultado: {soma}")
    except:
        labelResult.config(text=f"Informe numeros validos!!!")
def sub():    
    try:
        n1 = float(entrada1.get())
        n2 = float(entrada2.get())
        
        soma = n1 - n2 
        labelResult.config(text=f"Resultado: {soma}")
    except:
        labelResult.config(text=f"Informe numeros validos!!!")

def mult():    
    try:
        n1 = float(entrada1.get())
        n2 = float(entrada2.get())
        
        soma = n1 * n2 
        labelResult.config(text=f"Resultado: {soma}")
    except:
        labelResult.config(text=f"Informe numeros validos!!!")
def div():    
    try:
        n1 = float(entrada1.get())
        n2 = float(entrada2.get())
        
        soma = n1 / n2 
        labelResult.config(text=f"Resultado: {soma}")
    except:
        labelResult.config(text=f"Informe numeros validos!!!")

#criando Janela
janela = tk.Tk()
janela.title("Calculadora")
janela.geometry("300x300")

labelNum1 = tk.Label(janela, text="Numero 1:")
labelNum1.pack()
entrada1 = tk.Entry(janela)
entrada1.pack()

labelNum2 = tk.Label(janela, text="Numero 2:")
labelNum2.pack()
entrada2 = tk.Entry(janela)
entrada2.pack()

labelResult = tk.Label(janela, text="Resultado: ")
labelResult.pack()

botao = tk.Button(janela, text="Somar", command=somar)
botao.pack()
botao = tk.Button(janela, text="Subtrair", command=sub)
botao.pack()
botao = tk.Button(janela, text="Mult", command=mult)
botao.pack()
botao = tk.Button(janela, text="Dividir", command=div)
botao.pack()




janela.mainloop()