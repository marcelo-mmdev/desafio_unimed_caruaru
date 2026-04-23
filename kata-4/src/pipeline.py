import pandas as pd
from datetime import datetime

# ---------------------------
# Funções auxiliares
# ---------------------------

def parse_date(value):
    """
    Converte datas em múltiplos formatos:
    - DD/MM/YYYY
    - YYYY-MM-DD
    - timestamp
    Retorna datetime ou None
    """
    try:
        if pd.isna(value):
            return None

        value_str = str(value).strip()

        # timestamp (apenas números)
        if value_str.isdigit():
            return datetime.fromtimestamp(int(value_str))

        # parsing flexível
        return pd.to_datetime(value_str, dayfirst=True, errors='coerce')

    except Exception:
        return None


def normalize_city(city):
    """
    Normaliza nomes de cidades:
    - remove espaços extras
    - lowercase
    - Title Case
    """
    if pd.isna(city):
        return None

    return city.strip().lower().title()


def parse_value(value):
    """
    Converte valores monetários:
    - aceita vírgula como decimal
    - trata valores inválidos
    """
    try:
        if pd.isna(value):
            return 0.0

        value_str = str(value).replace(",", ".").strip()
        return float(value_str)

    except Exception:
        return 0.0


# ---------------------------
# Pipeline
# ---------------------------

def run_pipeline():
    print("📥 Lendo arquivos...")

    pedidos = pd.read_csv("../data/pedidos.csv")
    clientes = pd.read_csv("../data/clientes.csv")
    entregas = pd.read_csv("../data/entregas.csv")

    print("🧹 Aplicando limpeza...")

    # --- LIMPEZA ---
    pedidos["data_pedido"] = pedidos["data_pedido"].apply(parse_date)
    pedidos["valor_total"] = pedidos["valor_total"].apply(parse_value)

    clientes["cidade"] = clientes["cidade"].apply(normalize_city)

    entregas["data_prevista"] = entregas["data_prevista"].apply(parse_date)
    entregas["data_realizada"] = entregas["data_realizada"].apply(parse_date)

    # --- REMOVER ORPHANS ---
    print("🔍 Removendo registros órfãos...")
    entregas = entregas[entregas["id_pedido"].isin(pedidos["id_pedido"])]

    # --- JOIN ---
    print("🔗 Realizando joins...")

    df = pedidos.merge(clientes, on="id_cliente", how="left")
    df = df.merge(entregas, on="id_pedido", how="left")

    # --- CALCULAR ATRASO ---
    print("⏱ Calculando atraso...")

    def calc_atraso(row):
        if pd.isna(row["data_realizada"]) or pd.isna(row["data_prevista"]):
            return None

        return (row["data_realizada"] - row["data_prevista"]).days

    df["atraso_dias"] = df.apply(calc_atraso, axis=1)

    # --- SELEÇÃO FINAL ---
    print("📊 Gerando dataset final...")

    df_final = df[[
        "id_pedido",
        "nome",
        "cidade",
        "estado",
        "valor_total",
        "status",
        "data_pedido",
        "data_prevista",
        "data_realizada",
        "atraso_dias",
        "status_entrega"
    ]]

    df_final.columns = [
        "id_pedido",
        "nome_cliente",
        "cidade_normalizada",
        "estado",
        "valor_total",
        "status_pedido",
        "data_pedido",
        "data_prevista_entrega",
        "data_realizada_entrega",
        "atraso_dias",
        "status_entrega"
    ]

    # --- GARANTIR TIPOS ---
    df_final["valor_total"] = df_final["valor_total"].astype(float)

    # --- EXPORT ---
    print("💾 Salvando arquivo consolidado...")

    df_final.to_csv("../output/consolidado.csv", index=False)

    print("✅ Pipeline concluído!")

    return df_final


# ---------------------------
# Indicadores
# ---------------------------

def gerar_indicadores(df):
    print("📈 Gerando indicadores...")

    indicadores = {}

    # Total por status
    indicadores["total_por_status"] = df["status_pedido"].value_counts().to_dict()

    # Ticket médio por estado
    indicadores["ticket_medio_por_estado"] = (
        df.groupby("estado")["valor_total"].mean().round(2).to_dict()
    )

    # Entregas no prazo vs atraso
    entregues = df.dropna(subset=["atraso_dias"])

    no_prazo = (entregues["atraso_dias"] <= 0).sum()
    atraso = (entregues["atraso_dias"] > 0).sum()

    total = no_prazo + atraso

    indicadores["percentual_no_prazo"] = round(no_prazo / total, 2) if total else 0
    indicadores["percentual_atraso"] = round(atraso / total, 2) if total else 0

    # Top 3 cidades
    indicadores["top_3_cidades"] = (
        df["cidade_normalizada"].value_counts().head(3).to_dict()
    )

    # Média de atraso
    indicadores["media_atraso"] = round(
        entregues[entregues["atraso_dias"] > 0]["atraso_dias"].mean(), 2
    )

    print("\n📊 Indicadores:")
    for k, v in indicadores.items():
        print(f"{k}: {v}")

    return indicadores


# ---------------------------
# Execução
# ---------------------------

if __name__ == "__main__":
    df = run_pipeline()
    gerar_indicadores(df)