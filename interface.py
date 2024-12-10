from tkinter import * #importação da interface

class Aplication: #criação de uma classe que no momento não há informação
    def __init__(self, master=None): 
        self.fontepadrao = ("Codec Pro", 15)
        self.primeiroContainer = Frame(master)
        self.primeiroContainer["pady"] = 50
        self.primeiroContainer["padx"] = 110
        self.primeiroContainer["bg"] = "orange"
        self.primeiroContainer.pack()

        self.segundoContainer = Frame(master)
        self.segundoContainer["pady"] = 50
        self.segundoContainer["padx"] = 100
        self.segundoContainer.pack()

        self.terceiroContainer = Frame(master)
        self.terceiroContainer["pady"] = 25
        self.terceiroContainer["padx"] = 50
        self.terceiroContainer.pack()

        self.quartoContainer = Frame(master)
        self.quartoContainer["pady"] = 25
        self.quartoContainer["padx"] = 50
        self.quartoContainer.pack()

        self.quintoContainer = Frame(master)
        self.quintoContainer["pady"] = 2
        self.quintoContainer["padx"] = 10
        self.quintoContainer.pack()

        self.titulo = Label(self.primeiroContainer, text="CALCULADORA DE VEICULAÇÃO")
        self.titulo ["bg"] = "orange"
        self.titulo ["font"] = ("Type Machine", 37, "bold", "italic")
        self.titulo.pack()
        
        self.segundos = Label(self.segundoContainer, text="Adicione os segundos do Spot: ", font=self.fontepadrao)
        self.segundos.pack()

        self.entradasegundos = Entry(self.segundoContainer)
        self.entradasegundos ["width"] = 45
        self.entradasegundos["font"] = self.fontepadrao
        self.entradasegundos["bg"] = "#FFFFE0"
        self.entradasegundos.pack()

        self.quantidade = Label(self.terceiroContainer, text="Quantidade de Veiculações: ", font=self.fontepadrao)
        self.quantidade.pack()
    
        self.entradaquantidade = Entry(self.terceiroContainer)
        self.entradaquantidade["width"] = 45
        self.entradaquantidade["font"] = self.fontepadrao
        self.entradaquantidade["bg"] = "#FFFFE0"
        self.entradaquantidade.pack()

        self.resultado = Button(self.quartoContainer)
        self.resultado["text"] =  "Calcular"
        self.resultado["font"] = self.fontepadrao
        self.resultado["fg"] = "white"
        self.resultado["bg"] = "orange"
        self.resultado["pady"] = 10
        self.resultado["height"] = 1
        self.resultado["width"] = 35
        self.resultado["command"] = self.Valores
        self.resultado.pack()

        self.label_resultado_segundos = Label(self.quintoContainer, text="")
        self.label_resultado_segundos["font"] = ("Codec Pro", 20, "bold")
        self.label_resultado_segundos["pady"] = 1
        self.label_resultado_segundos["fg"] = "red"
        self.label_resultado_segundos.pack()

        self.label_resultado = Label(self.quintoContainer, text="")
        self.label_resultado["font"] = ("Codec Pro", 20, "bold")
        self.label_resultado["pady"] = 1
        self.label_resultado["fg"] = "red"
        self.label_resultado.pack()

    def Calculadora(self):
        segundos = int(self.entradasegundos.get())
        vezes= int(self.entradaquantidade.get())
        total = segundos * vezes
        totalemminutos = total // 60
        segundos_restantes = segundos % 60
        
        self.label_resultado_segundos["text"] = f"{total} segundos"
        self.label_resultado["text"]= f"{totalemminutos}:{segundos_restantes} minutos"

    def Valores(self):
        if self.entradasegundos.get() or self.entradaquantidade.get():
            self.resultado["command"] = self.Calculadora
        else:
            self.label_resultado_segundos["text"]= "Dados incorretos"


janela = Tk()
janela.title("Calculadora de Veiculações")
janela.geometry("1920x1080")

Aplication(janela) #chama a interface
janela.mainloop() #abrir