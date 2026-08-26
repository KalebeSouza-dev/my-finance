import tkinter as tk 
import customtkinter as ctk

class CalculatorAPP:
    def __init__(self, root):
        self.root = root 

        # window
        root.title("Calculadora de Juros") 
        root.geometry("300x320")
        root.resizable(False, False)

        # inputs
        self.entry_valor_inicial = ctk.CTkEntry(root, placeholder_text="Valor Inicial (R$)", width=200)
        self.entry_valor_inicial.pack(pady=3)

        self.entry_aporte_mensal = ctk.CTkEntry(root, placeholder_text="Aporte Mensal (R$)", width=200)
        self.entry_aporte_mensal.pack(pady=3)

        self.entry_taxa_anual = ctk.CTkEntry(root, placeholder_text="Taxa Anual (%)", width=200)
        self.entry_taxa_anual.pack(pady=3)

        self.entry_periodo = ctk.CTkEntry(root, placeholder_text="Tempo (Meses)", width=200)
        self.entry_periodo.pack(pady=3)

        self.entry_valor_inicial.bind("<Return>",lambda event: self.entry_aporte_mensal.focus()) 
        self.entry_aporte_mensal.bind("<Return>", lambda event: self.entry_taxa_anual.focus())   
        self.entry_taxa_anual.bind("<Return>", lambda event: self.entry_periodo.focus()) 
        self.entry_periodo.bind("<Return>", self.exibir_calculo)

        # button
        self.btn_calcular = ctk.CTkButton(root, text="Calcular", width=200, command=self.exibir_calculo)
        self.btn_calcular.pack(pady=7)


        # RESULT
        self.result_frame = ctk.CTkFrame(root, fg_color="transparent")
        self.result_frame.pack(pady=10, fill="x", padx=15)

        # Box 1: Investido
        self.box_investido = ctk.CTkFrame(self.result_frame, fg_color="#2b2b2b", border_width=1, border_color="#565b5e")
        self.box_investido.pack(side="left", expand=True, fill="both", padx=(0, 5)) # padx separa as duas caixas no meio

        self.lbl_investido = ctk.CTkLabel(self.box_investido, text="Investido\nR$ 0.00")
        self.lbl_investido.pack(pady=10, padx=10)

        # Box 2: Juros
        self.box_juros = ctk.CTkFrame(self.result_frame, fg_color="#2b2b2b", border_width=1, border_color="#565b5e")
        self.box_juros.pack(side="right", expand=True, fill="both", padx=(5, 0))

        self.lbl_juros = ctk.CTkLabel(self.box_juros, text="Juros\nR$ 0.00")
        self.lbl_juros.pack(pady=10, padx=10)

        # Box 3: Valor Final
        self.box_final = ctk.CTkFrame(root, fg_color="#1f538d", corner_radius=6) 
        self.box_final.pack(pady=5, fill="x", padx=15)

        self.lbl_final = ctk.CTkLabel(self.box_final, text="Valor Final: R$ 0.00", font=("Arial", 16, "bold"), text_color="white")
        self.lbl_final.pack(pady=12)

    def exibir_calculo(self, event=None):
        try:
            valor_inicial = float(self.entry_valor_inicial.get().replace(",", "."))
            aporte_mensal = float(self.entry_aporte_mensal.get().replace(",", "."))
            taxa_anual = float(self.entry_taxa_anual.get().replace(",", "."))
            periodo = int(self.entry_periodo.get())

            resultados = self.calculo(valor_inicial, aporte_mensal, taxa_anual, periodo)

            self.lbl_investido.configure(text=f"Investido: R$ {resultados['valor_investido']:.2f}")
            self.lbl_juros.configure(text=f"Juros: R$ {resultados['valor_juros']:.2f}")
            self.lbl_final.configure(text=f"Valor Final: R$ {resultados['valor_final']:.2f}")
            
        except ValueError:
            self.lbl_final.configure(text="Erro: Preencha com números válidos!")
    
    def calculo(self,valor_inicial, aporte_mensal, juros_anual, periodo) -> dict:
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