import tkinter as tk

def calcular(op):    
    try:
        
        n1 = float(entrada1.get())
        n2 = float(entrada2.get())
        
        resultado = 0.0
        if op == "+":
            resultado = n1 + n2
        if op == "-":
            resultado = n1 - n2
        if op == "*":
            resultado = n1 * n2
        if op == "/":
            resultado = n1 / n2

        labelResult.config(text=f"Resultado: {resultado}")
    except:
        labelResult.config(text=f"Informe numeros validos!!!")


#criando Janela
janela = tk.Tk()
janela.title("Calculadora")
janela.geometry("400x300")

labelNum1 = tk.Label(janela, text="Numero 1:").grid(row=0, column=0, padx=10, pady=5, sticky="w" )
entrada1 = tk.Entry(janela)
entrada1.grid(row=0, column=1, padx=10, pady=5)

labelNum2 = tk.Label(janela, text="Numero 2:").grid(row=1, column=0, padx=10, pady=5, sticky="w")
entrada2 = tk.Entry(janela)
entrada2.grid(row=1, column=1, padx=10, pady=5)

botao = tk.Button(janela, text="Somar", command=lambda:calcular("+"))
botao.grid(row=2, column=0, padx=10, pady=5)
botao1 = tk.Button(janela, text="Subtrair", command=lambda:calcular("-"))
botao1.grid(row=2, column=1, padx=10, pady=5)
botao2 = tk.Button(janela, text="Mult", command=lambda:calcular("*"))
botao2.grid(row=2, column=2, padx=10, pady=5)
botao3 = tk.Button(janela, text="Dividir", command=lambda:calcular("/"))
botao3.grid(row=2, column=3, padx=10, pady=5)

labelResult = tk.Label(janela, text="Resultado: ")
labelResult.grid(row=3, column=3)


janela.mainloop()