import gspread
import tkinter as tk
from tkinter import ttk, messagebox
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow

# ============================
# CONFIGURAÇÕES
# ============================
import os
from dotenv import load_dotenv # Importa a biblioteca

# Carrega as variáveis do arquivo .env
load_dotenv()

# Pega o ID que está escondido no arquivo .env
PLANILHA_ID = os.getenv("PLANILHA_ID")

# Se não achar o ID, avisa para evitar erro silencioso
if not PLANILHA_ID:
    raise ValueError("ERRO: PLANILHA_ID não encontrado no arquivo .env")
TOKEN_FILE = "token.json"
SCOPES = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive",
]


# ============================
# AUTENTICAÇÃO
# ============================
def conectar():
    creds = None

    try:
        creds = Credentials.from_authorized_user_file(TOKEN_FILE, SCOPES)
    except:
        pass

    if not creds or not creds.valid:
        flow = InstalledAppFlow.from_client_secrets_file(
            "credentials.json", SCOPES
        )
        creds = flow.run_local_server(port=0)
        with open(TOKEN_FILE, "w") as token:
            token.write(creds.to_json())

    return gspread.authorize(creds)


gc = conectar()
sh = gc.open_by_key(PLANILHA_ID)


# ============================
# FUNÇÕES PRINCIPAIS
# ============================
def localizar_celula(ws, data):
    """Localiza exatamente a célula contendo a data (ex: 13.11)."""
    try:
        cel = ws.find(data)
        return cel
    except:
        return None


def atualizar(ws, data, arquivos, gb, log_callback):
    cel = localizar_celula(ws, data)

    if not cel:
        log_callback(f"❌ Data {data} não encontrada!")
        return

    linha = cel.row
    col_arquivos = cel.col + 1
    col_gb = cel.col + 2

    ws.update_cell(linha, col_arquivos, arquivos)
    ws.update_cell(linha, col_gb, gb)

    log_callback(f"✅ Cliente '{ws.title}' atualizado: Linha {linha} | Arquivos={arquivos} | GB={gb}")


# ============================
# INTERFACE TKINTER
# ============================
def iniciar_interface():
    root = tk.Tk()
    root.title("Lançamento Automático ITL")
    root.geometry("520x480")
    root.resizable(False, False)
    root.configure(bg="#202225")

    estilo_label = {"bg": "#202225", "fg": "white", "font": ("Segoe UI", 11)}
    estilo_entry = {"font": ("Segoe UI", 12)}

    # ========== LOG ==========

    frame_log = tk.Frame(root, bg="#202225")
    frame_log.pack(side="bottom", fill="both", padx=10, pady=10)

    tk.Label(frame_log, text="LOG:", **estilo_label).pack(anchor="w")

    text_log = tk.Text(frame_log, height=10, bg="#2f3136", fg="white",
                       font=("Consolas", 10), relief="flat")
    text_log.pack(fill="x")

    def log(msg):
        text_log.insert(tk.END, msg + "\n")
        text_log.see(tk.END)

    # ========== CAMPOS ==========

    frame_top = tk.Frame(root, bg="#202225")
    frame_top.pack(pady=10)

    # Cliente
    tk.Label(frame_top, text="Cliente:", **estilo_label).grid(row=0, column=0, sticky="w")
    clientes = [ws.title for ws in sh.worksheets()]
    combo_cliente = ttk.Combobox(frame_top, values=clientes, width=28, state="readonly")
    combo_cliente.grid(row=0, column=1, padx=10)

    # Data
    tk.Label(frame_top, text="Data (ex: 13.11):", **estilo_label).grid(row=1, column=0, pady=10, sticky="w")
    entry_data = tk.Entry(frame_top, width=20, **estilo_entry)
    entry_data.grid(row=1, column=1)

    # Arquivos
    tk.Label(frame_top, text="Arquivos:", **estilo_label).grid(row=2, column=0, pady=10, sticky="w")
    entry_arquivos = tk.Entry(frame_top, width=20, **estilo_entry)
    entry_arquivos.grid(row=2, column=1)

    # GB
    tk.Label(frame_top, text="GB:", **estilo_label).grid(row=3, column=0, pady=10, sticky="w")
    entry_gb = tk.Entry(frame_top, width=20, **estilo_entry)
    entry_gb.grid(row=3, column=1)

    # ========== BOTÕES ==========

    frame_buttons = tk.Frame(root, bg="#202225")
    frame_buttons.pack(pady=20)

    def confirmar():
        cliente = combo_cliente.get()
        data = entry_data.get().strip()
        arquivos = entry_arquivos.get().strip()
        gb = entry_gb.get().strip()

        if not cliente or not data or not arquivos or not gb:
            log("❌ Preencha todos os campos.")
            return

        ws = sh.worksheet(cliente)
        atualizar(ws, data, arquivos, gb, log)

    def limpar():
        entry_data.delete(0, tk.END)
        entry_arquivos.delete(0, tk.END)
        entry_gb.delete(0, tk.END)
        log("↩ Campos limpos.")

    def pular_cliente():
        atual = combo_cliente.get()
        if atual not in clientes:
            return

        idx = clientes.index(atual)
        novo = (idx + 1) % len(clientes)
        combo_cliente.set(clientes[novo])
        log(f"⏭ Cliente alterado automaticamente para: {clientes[novo]}")

    btn_confirmar = tk.Button(frame_buttons, text="Confirmar", bg="#4CAF50", fg="white",
                              font=("Segoe UI", 12), width=14, command=confirmar)
    btn_confirmar.grid(row=0, column=0, padx=10)

    btn_voltar = tk.Button(frame_buttons, text="Voltar", bg="#FF9800", fg="white",
                           font=("Segoe UI", 12), width=14, command=limpar)
    btn_voltar.grid(row=0, column=1, padx=10)

    btn_pular = tk.Button(frame_buttons, text="Pular Cliente", bg="#2196F3", fg="white",
                          font=("Segoe UI", 12), width=14, command=pular_cliente)
    btn_pular.grid(row=0, column=2, padx=10)

    root.mainloop()


# ============================
# INÍCIO
# ============================
if __name__ == "__main__":
    iniciar_interface()
