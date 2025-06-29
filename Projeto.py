
import tkinter as tk
from tkinter import messagebox
from ttkbootstrap import Style
from ttkbootstrap.widgets import Combobox, Checkbutton, Button, Label

# definição de constantes
TIPOS_BEBIDA = ["Refrigerante", "Suco"]
TODOS_SABORES = ["Coca", "Guaraná", "Suco de Uva", "Suco de Laranja"]
TODOS_TAMANHOS = [300, 500, 700]
TIPOS_ORDEM = ["Para Viagem", "Comer Aqui"]

# desenvolvimento
def EnviarOrdemAoABS(tipoDeBebida, saborDaBebida, tamanhoDaBebida, tipoDaOrdem, comGelo):
    SABORES_VALIDOS = {
        "Refrigerante": ["Coca", "Guaraná"],
        "Suco": ["Suco de Uva", "Suco de Laranja"]
    }
    TAMANHOS_VALIDOS = {
        "Refrigerante": [300, 500, 700],
        "Suco": [300, 500]
    }

    if saborDaBebida not in SABORES_VALIDOS.get(tipoDeBebida, []):
        return "Ops! Parece que tem algo de errado com seu pedido." "\nVerifique o sabor"

    if int(tamanhoDaBebida) not in TAMANHOS_VALIDOS.get(tipoDeBebida, []):
        return "Ops! Parece que tem algo de errado com seu pedido." "\nO tamanho máximo para suco é de 500ml"

    copo = "Copo de Papel" if tipoDeBebida == "Refrigerante" else "Copo de Plástico"

    #validação, é preciso uma confirmação a partir do cliente se deseja gelo ou não
    gelo_str = f"{6 if tipoDeBebida == 'Refrigerante' else 12} pedras de gelo" if comGelo == True else "sem gelo"
    

    tampa = "tampa sem furo" if tipoDaOrdem == "Para Viagem" else "Tampa com Furo"
    return f"A bebida selecionada foi servida em: {copo} de {tamanhoDaBebida}ml, {tampa} e {gelo_str}."

# Função para processar botão
def ValidacaoFormulario():
    tipoDeBebida = tipo_var.get()
    saborDaBebida = sabor_var.get()
    tamanhoDaBebida = tamanho_var.get()
    tipoDaOrdem = ordem_var.get()
    comGelo = gelo_var.get()

    if not tipoDeBebida or not saborDaBebida or not tamanhoDaBebida or not tipoDaOrdem:
        messagebox.showwarning("Erro", "Não está se esquecendo de nada? Preencha todos os campos")
        return

    resultado = EnviarOrdemAoABS(tipoDeBebida, saborDaBebida, int(tamanhoDaBebida), tipoDaOrdem, comGelo)
    messagebox.showinfo("Resultado", resultado)

# Tema formulário
style = Style(theme='flatly') 

# Tela principal
root = style.master
root.title("ABS - Sistema de Bebidas")
root.geometry("420x360")
root.configure(bg='#f8f9fa')

# Labels e comboboxes
Label(root, text="Tipo de Bebida:", bootstyle="journal").pack(pady=5)
tipo_var = tk.StringVar()
tipo_cb = Combobox(root, textvariable=tipo_var, values=TIPOS_BEBIDA, bootstyle="info", width=30, state="readonly")
tipo_cb.pack()

Label(root, text="Sabor:", bootstyle="journal").pack(pady=5)
sabor_var = tk.StringVar()
sabor_cb = Combobox(root, textvariable=sabor_var, values=TODOS_SABORES, bootstyle="info", width=30, state="readonly")
sabor_cb.pack()

Label(root, text="Tamanho (ml):", bootstyle="journal").pack(pady=5)
tamanho_var = tk.StringVar()
tamanho_cb = Combobox(root, textvariable=tamanho_var, values=TODOS_TAMANHOS, bootstyle="info", width=30, state="readonly")
tamanho_cb.pack()

Label(root, text="Tipo de Ordem:", bootstyle="journal").pack(pady=5)
ordem_var = tk.StringVar()
ordem_cb = Combobox(root, textvariable=ordem_var, values=TIPOS_ORDEM, bootstyle="info", width=30, state="readonly")
ordem_cb.pack()

gelo_var = tk.BooleanVar(value=True)
Checkbutton(root, text="Adicionar Gelo", variable=gelo_var, bootstyle="round-toggle").pack(pady=30)

# Botão Enviar
Button(root, text="Enviar Pedido", command=ValidacaoFormulario, bootstyle="journal", width=20).pack(pady=5)

root.mainloop()