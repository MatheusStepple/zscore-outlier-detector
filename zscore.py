import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from io import StringIO

def carregar_dados():
    csv_data = """Object,Band 1,Band 2,Band 3,Band 4,Band 5,Band 6,Band 7,Band 8,Band 9,Band 10,Band 11,Band 12,Band 13,Band 14,Band 15,Band 16,Band 17
Object 1,-0.21551,-0.93957,-0.51151,2.28230,-0.83028,-0.94641,-0.62991,-0.73465,1.43983,0.57004,-0.49329,0.49035,0.04179,-0.61853,-0.24966,2.05916,-0.71416
Object 2,-0.63351,-0.82253,-0.34998,2.28551,-0.78172,-0.83541,-0.47456,-0.72372,0.52422,1.29532,-0.61633,0.33520,-0.16097,-0.52182,-0.20607,2.13128,-0.62492
Object 3,-0.00491,-0.89389,-0.47903,2.19890,-0.72184,-0.87414,-0.60634,-0.70424,1.09041,0.23216,-0.63488,0.63604,-0.09271,-0.52732,-0.27050,2.24036,-0.68756
Object 4,-0.06431,-0.95763,-0.61541,2.39564,-0.89066,-0.97763,-0.59763,-0.76430,1.40777,0.82234,-0.53097,0.66456,0.14679,-0.66874,-0.30836,1.67217,-0.73096"""
    df = pd.read_csv(StringIO(csv_data)).set_index("Object")
    return df

def analisar_dados(df):
    medias = df.mean()
    desvios = df.std()
    print("== MÉDIAS POR BANDA ==")
    for col in df.columns:
        print(f"{col:<8}: média = {medias[col]:.6f} | desvio = {desvios[col]:.6f}")
    print()
    z = ((df - medias) / desvios).abs()
    print("== Z-SCORES (DESVIOS ABSOLUTOS PADRONIZADOS) POR OBJETO ==")
    print(z.round(3))
    print()
    soma = z.sum(axis=1)
    print("== SOMATÓRIO DE Z-SCORES POR OBJETO ==")
    for obj, val in soma.items():
        print(f"{obj:<8}: total de desvios = {val:.6f}")
    print()
    destaque = soma.idxmax()
    print("== RESULTADO FINAL ==\n")
    print(f"O objeto mais discrepante é: {destaque}")
    print(f"Ele possui a maior soma total de desvios padronizados: {soma[destaque]:.6f}\n")
    return medias, desvios, z, soma

def plotar(medias, desvios, z, soma):
    plt.figure(figsize=(12, 6))
    plt.plot(medias.index, medias.values, marker='o', label='Média')
    plt.fill_between(medias.index, medias - desvios, medias + desvios, alpha=0.3, color='gray', label='±1 Desvio Padrão')
    plt.xticks(rotation=45)
    plt.title('Médias e Desvios por Banda')
    plt.legend()
    plt.tight_layout()
    plt.show()

    plt.figure(figsize=(12, 6))
    sns.heatmap(z, cmap='YlOrRd', annot=True, fmt=".2f")
    plt.title('Z-scores absolutos por objeto e banda')
    plt.xlabel('Bandas')
    plt.ylabel('Objetos')
    plt.tight_layout()
    plt.show()

    plt.figure(figsize=(8, 4))
    soma.plot(kind='bar', color='steelblue')
    plt.axhline(soma.mean(), color='red', linestyle='--', label='Média dos totais')
    plt.title('Soma dos Z-scores por Objeto')
    plt.ylabel('Somatório dos Z-scores')
    plt.legend()
    plt.tight_layout()
    plt.show()

df = carregar_dados()
medias, desvios, z, soma = analisar_dados(df)
plotar(medias, desvios, z, soma)
