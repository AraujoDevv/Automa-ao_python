import pandas as pd
import tkinter as tk
from tkinter import messagebox, ttk
from tkinter import font as tkfont


def formatar_valor(valor):
    return f"R$ {valor:,.2f}"


def buscar_dados():
    nome_busca = entrada_nome.get()
    resultado = df[df.iloc[:, 0] == nome_busca]

    if not resultado.empty:
        valor_correspondente = resultado.iloc[0, 1]
        valor_formatado = formatar_valor(valor_correspondente)
        messagebox.showinfo("Resultado", f"Nome: {nome_busca}\nValor: {valor_formatado}")
    else:
        messagebox.showinfo("Aviso", f"Nome {nome_busca} não foi encontrado na planilha.")


arquivo = 'vendas_aleatorio.xlsx'
df = pd.read_excel(arquivo)


janela = tk.Tk()
janela.title("Consulta de Vendas")
janela.configure(bg='#E8F5E9')  

font_padrao = tkfont.Font(family="Arial", size=12)
font_botao = tkfont.Font(family="Arial", size=12, weight="bold")


rotulo = tk.Label(janela, text="Digite o nome que deseja buscar:", bg='#E8F5E9', font=font_padrao)
rotulo.pack(pady=10)

entrada_nome = tk.Entry(janela, font=font_padrao, bd=0, relief='flat')
entrada_nome.pack(pady=5, padx=10)


botao_buscar = tk.Button(janela, text="Buscar", command=buscar_dados, font=font_botao, bg='#66BB6A', fg='white', relief='flat', borderwidth=2)
botao_buscar.pack(pady=10, padx=10)


def create_rounded_rectangle(canvas, x1, y1, x2, y2, radius=10, **kwargs):
    """Cria um retângulo com cantos arredondados no canvas."""
    points = [x1 + radius, y1,
              x2 - radius, y1,
              x2, y1,
              x2, y2 - radius,
              x2, y2,
              x1 + radius, y2,
              x1, y2,
              x1, y1 + radius]
    canvas.create_polygon(points, **kwargs, smooth=True)


canvas = tk.Canvas(janela, width=botao_buscar.winfo_reqwidth(), height=botao_buscar.winfo_reqheight(), bg='#66BB6A', bd=0, highlightthickness=0)
canvas.pack(pady=10, padx=10)
create_rounded_rectangle(canvas, 0, 0, canvas.winfo_reqwidth(), canvas.winfo_reqheight(), radius=10, fill='#66BB6A')


janela.mainloop()
