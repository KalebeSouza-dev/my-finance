import tkinter as tk 
import customtkinter as ctk

class CalculatorAPP:
    def __init__(self, root):
        self.root = root 

        # window
        root.title("Calculadora de Juros") 
        root.geometry("300x230")
        root.resizable(False, False)

        # valor inicial
        # taxa anual
        # aporte mensal
        # tempo
    
    def calculo(self, valor_inicial, aporte_mensal, juros_anual, periodo) -> dict:
        juros_mensal = (1 + (juros_anual / 100)) ** (1 / 12) - 1
        juros_por_periodo = (1 + juros_mensal) ** periodo

        valorMontante = valor_inicial * juros_por_periodo
        valorAporte = (aporte_mensal / juros_mensal) * (juros_por_periodo - 1)

        valor_final = valorMontante + valorAporte
        valor_juros = valor_final - (valor_inicial + periodo * aporte_mensal)
        valor_investido = valor_final - valor_juros

        print(f"{'  Valor Final:':<20} {'R$ ':>5}{valor_final:>10.2f}")
        print(f"{'  Valor Juros:':<20} {'R$ ':>5}{valor_juros:>10.2f}")
        print(f"{'  Valor Investido:':<20} {'R$ ':>5}{valor_investido:>10.2f}")

        return {"valor_final": valor_final, "valor_juros": valor_juros, "valor_investido": valor_investido}