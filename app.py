import pandas as pd

a = pd.read_csv("resources/cities.csv")

a.to_html("data_index.html")