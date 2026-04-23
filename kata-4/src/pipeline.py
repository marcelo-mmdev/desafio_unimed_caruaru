import pandas as pd
from datetime import datetime

# ---------------------------
# Funções auxiliares
# ---------------------------

def parse_date(value):
    try:
        if pd.isna(value):
            return None

        # timestamp
        if str(value).isdigit():
            return datetime.fromtimestamp(int(value))

        return pd.to_datetime(value, dayfirst=True, errors='coerce')
    except:
        return None


def normalize_city(city):
    if pd.isna(city):
        return None
    return city.strip().lower().title()


def parse_value(value):
    if pd.isna(value):
        return 0
    return float(str(value).replace(",", "."))


# ---------------------------
# Pipeline
# ---------------------------

def run_pipeline():
    pedidos = pd.read_csv("../data/pedidos.csv")
    clientes = pd.read_csv("../data/clientes.csv")
    entregas = pd.read_csv("../data/entregas.csv")

    # --- LIMPEZA ---

    pedidos["data_pedido"] = pedidos["data_pedido"].apply(parse_date)
    pedidos["valor_total"] = pedidos["valor_total"].apply(parse_value)

    clientes["cidade"] = clientes["cidade"].apply(normalize_city)

    entregas["data_prevista"] = entregas["data_prevista"].apply(parse_date)
    entregas["data_realizada"] = entregas["data_realizada"].apply(parse_date)

    # --- REMOVER ORPHANS ---
    entregas = entregas[entregas["id_pedido"].isin(pedidos["id_pedido"])]

    # --- JOIN ---
    df = pedidos.merge(clientes, on="id_cliente", how="left")
    df = df.merge(entregas, on="id_pedido", how="left")

    # --- CALCULAR ATRASO ---
    def calc_atraso(row):
        if pd.isna(row["data_realizada"]) or pd.isna(row["data_prevista"]):
            return None
        return (row["data_realizada"] - row["data_prevista"]).days

    df["atraso_dias"] = df.apply(calc_atraso, axis=1)

    # --- SELEÇÃO FINAL ---
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

    df_final.to_csv("../output/consolidado.csv", index=False)

    return df_final


# ---------------------------
# Indicadores
# ---------------------------

def gerar_indicadores(df):
    indicadores = {}

    indicadores["total_por_status"] = df["status_pedido"].value_counts().to_dict()

    indicadores["ticket_medio_por_estado"] = (
        df.groupby("estado")["valor_total"].mean().to_dict()
    )

    entregues = df.dropna(subset=["atraso_dias"])

    no_prazo = (entregues["atraso_dias"] <= 0).sum()
    atraso = (entregues["atraso_dias"] > 0).sum()

    total = no_prazo + atraso

    indicadores["percentual_no_prazo"] = no_prazo / total if total else 0
    indicadores["percentual_atraso"] = atraso / total if total else 0

    indicadores["top_3_cidades"] = (
        df["cidade_normalizada"].value_counts().head(3).to_dict()
    )

    indicadores["media_atraso"] = (
        entregues[entregues["atraso_dias"] > 0]["atraso_dias"].mean()
    )

    print(indicadores)

    return indicadores


# ---------------------------
# Execução
# ---------------------------

if __name__ == "__main__":
    df = run_pipeline()
    gerar_indicadores(df)