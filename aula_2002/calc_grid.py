import tkinter as tk

def somar():    
    try:
        n1 = float(entrada1.get())
        n2 = float(entrada2.get())
        
        soma = n1 + n2 
        labelResult.config(text=f"Resultado: {soma}")
    except:
        labelResult.config(text=f"Informe numeros validos!!!")
def sub(self):    
    try:
        n1 = float(entrada1.get())
        n2 = float(entrada2.get())
        
        soma = n1 - n2 
        labelResult.config(text=f"Resultado: {soma}")
    except:
        labelResult.config(text=f"Informe numeros validos!!!")

def mult(self):    
    try:
        n1 = float(entrada1.get())
        n2 = float(entrada2.get())
        
        soma = n1 * n2 
        labelResult.config(text=f"Resultado: {soma}")
    except:
        labelResult.config(text=f"Informe numeros validos!!!")
def div(self):    
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

labelNum1 = tk.Label(janela, text="Numero 1:").grid(row=0, column=0)
entrada1 = tk.Entry(janela).grid(row=0, column=1)

labelNum2 = tk.Label(janela, text="Numero 2:").grid(row=1, column=0)
entrada2 = tk.Entry(janela).grid(row=1, column=1)

labelResult = tk.Label(janela, text="Resultado: ").grid(row=2, column=2)


botao = tk.Button(janela, text="Somar", command=somar).grid(row=3, column=0)
botao = tk.Button(janela, text="Subtrair", command=sub).grid(row=3, column=1)
botao = tk.Button(janela, text="Mult", command=mult).grid(row=3, column=2)
botao = tk.Button(janela, text="Dividir", command=div).grid(row=3, column=3)





janela.mainloop()