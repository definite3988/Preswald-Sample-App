from preswald import connect, get_df
from preswald import query
from preswald import table, text
from preswald import plotly
import plotly.express as px

connect()  # Initialize connection to preswald.toml data sources
df = get_df("data/train.csv")  # Load data

sql = "SELECT * FROM data/train.csv WHERE country = 'Austria'"
filtered_df = query(sql, "data/train.csv")

text("# My Data Analysis App")
table(filtered_df, title="Filtered Data")

fig = px.scatter(df, x="column1", y="column2", color="category")
plotly(fig)

