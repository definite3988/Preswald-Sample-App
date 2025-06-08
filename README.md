# 📊 Austria Sentiment Analysis Project

🔗 **Live Project:** [Preswald App](https://preswald.app/p3eb11df5#my-data-analysis-app)

## 🔎 Overview
This project analyzes sentiment data for Austria using **Preswald** for querying and visualization.

## 🛠️ Code Snippet
```python
from preswald import connect, get_df, query, table, text, plotly
import plotly.express as px

connect()  # Initialize connection
df = get_df("data/train.csv")  # Load data

sql = "SELECT * FROM data/train.csv WHERE country = 'Austria'"
filtered_df = query(sql, "data/train.csv")

text("# Austria Sentiment Analysis")
table(filtered_df, title="Filtered Data")

fig = px.scatter(df, x="column1", y="column2", color="category")
plotly(fig)
```
