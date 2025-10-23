# Análise Estatística da População de Exoplanetas da Missão Kepler

## Visão Geral  
Este projeto consiste em uma análise estatística exploratória da população de exoplanetas detectados pela missão Kepler, com foco na relação entre o tipo de planeta (rocheoso, super-Terra, netuniano e gasoso) e as propriedades das estrelas hospedeiras, especialmente a temperatura efetiva. Os dados utilizados provêm do catálogo KOI (Q1–Q17 DR24) e são processados em Python.

## Dados  
- Origem: NASA Exoplanet Archive (catálogo KOI).  
- Filtros aplicados: apenas planetas com `koi_disposition` igual a “CONFIRMED” ou “CANDIDATE” foram considerados; “FALSE POSITIVE” foram excluídos.  
- Variáveis-chave: `koi_prad` (raio planetário), `koi_steff` (temperatura efetiva da estrela hospedeira), `kepoi_name` (identificador da estrela/planeta).

## Metodologia  
- Classificação dos planetas com base em `koi_prad`:  
  - Rochoso: ≤ 1.6 R⊕  
  - Super-Terra: > 1.6 e ≤ 4.0 R⊕  
  - Gasoso: > 4.0 R⊕  
  - Netuniano: faixa definida conforme contexto da amostra  
- Visualizações e estatísticas geradas usando Python (bibliotecas: pandas, NumPy, matplotlib).  
- Análise da frequência por tipo de planeta, frequência de planetas por estrela e correlação entre tipo de planeta e faixa de temperatura estelar.

## Resultados Principais  
- Super-Terras e planetas rochosos são predominantes na amostra, especialmente em estrelas de **temperatura intermediária**.  
- Planetas netunianos aparecem em menor número e estão ausentes em faixas de estrela com temperaturas muito baixas (< 4661 K) ou muito altas (~8661 K).  
- Planetas gasosos têm presença moderada em diversas faixas de temperatura, com maior contagem observada em torno de ~6661 K.  
- A análise reforça a ideia de que a formação de planetas e sua detecção são influenciadas pelas características da estrela hospedeira, bem como por vieses observacionais.


