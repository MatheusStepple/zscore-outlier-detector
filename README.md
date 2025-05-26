# Z-Score Outlier Detector

Este projeto realiza a análise estatística de objetos com base em suas bandas espectrais, utilizando a padronização por z-score para identificar o objeto mais discrepante.

## 📊 Descrição

Dado um conjunto de objetos com valores em diferentes bandas (Band 1 a Band 17), o script:

1. Calcula a média e o desvio padrão para cada banda.
2. Calcula o z-score absoluto padronizado para cada valor.
3. Soma os z-scores de cada objeto e identifica aquele com maior discrepância.
4. Gera visualizações para facilitar a interpretação dos dados.

## 🧪 Tecnologias e bibliotecas

- **Python 3**
- `pandas` – manipulação de dados
- `matplotlib` – geração de gráficos
- `seaborn` – visualização estatística
- `io.StringIO` – leitura de dados CSV a partir de uma string


## 🖼️ Exemplos de visualização

- Média por banda (gráfico de linha)
- Mapa de calor dos z-scores por objeto

## 🚀 Como usar

Clone o repositório e execute o script:

```bash
git clone https://github.com/seu-usuario/zscore-outlier-detector.git
cd zscore-outlier-detector
python zscore_analysis.py

