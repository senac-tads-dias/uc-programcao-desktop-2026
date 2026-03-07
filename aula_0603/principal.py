import tkinter as tk

def abrir_janela_novo_usuario():
    janela_usuario = tk.Toplevel()
    janela_usuario.title("Novo Usuario")
    janela_usuario.geometry("300x200")

    tk.Label(janela_usuario, text="Nome:").grid(row=0,column=0, padx=5, pady=5)
    input_nome = tk.Entry(janela_usuario, width=35)
    input_nome.grid(row=0, column=1, padx=10, pady=5)

    tk.Label(janela_usuario, text="Email:").grid(row=1,column=0, padx=5, pady=5)
    input_email = tk.Entry(janela_usuario, width=35)
    input_email.grid(row=1, column=1, padx=10, pady=5)

    def salvar_usuario():
        nome = input_nome.get()
        email = input_email.get()
        lista_usuario.insert(tk.END, f"{nome}  -  {email}")
        janela_usuario.destroy()

    btn_salvar = tk.Button(janela_usuario, text="Salvar", command=salvar_usuario)
    btn_salvar.grid(row=2, column=1, padx=10, sticky="e")


janela = tk.Tk()
janela.title("Cadastro de Usuario")
janela.geometry("405x300")

menu_principal = tk.Menu(janela)
janela.config(menu=menu_principal)

menu_arquivo = tk.Menu(menu_principal, tearoff=0)
menu_principal.add_cascade(label="Arquivo", menu=menu_arquivo)
menu_arquivo.add_command(label="Sair", command=janela.quit)
menu_arquivo.add_command(label="Sair 2", command=janela.quit)

menu_usuario = tk.Menu(menu_principal, tearoff=0)
menu_principal.add_cascade(label="Usuario", menu=menu_usuario)
menu_usuario.add_command(label="Cadastrar", command=abrir_janela_novo_usuario)
menu_usuario.add_command(label="Alterar", command=janela.quit)

btn_cad = tk.Button(janela, text="Novo Cadastro", command=abrir_janela_novo_usuario)
btn_cad.grid(row=0, column=0, padx=10, pady= 10, sticky="e")

lista_usuario = tk.Listbox(janela, width=63)
lista_usuario.grid(row=1, column=0, padx=10, pady=10)


janela.mainloop()

