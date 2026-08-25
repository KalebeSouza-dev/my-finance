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
