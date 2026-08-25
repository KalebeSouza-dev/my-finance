# My Finance

Um sistema de controle financeiro pessoal *open source*, projetado para ser executado localmente no seu computador. 
O objetivo do projeto é oferecer um widget simples, rápido e privado para você registrar suas transações financeiras diárias.

**Status do Projeto:** Ainda em desenvolvimento.

## Tecnologias Utilizadas

Este projeto foi construído utilizando:
* **Python 3**
* **SQLite**: Banco de dados local
* **CustomTkinter**: Interface Gráfica Python.

---

Para buildar o app localmente, execute os seguintes comandos em um ambiente python:

```bash
    pip install pyinstaller
    pip install -r requirements.txt
        
    pyinstaller --noconsole --onefile my-finance.py
```