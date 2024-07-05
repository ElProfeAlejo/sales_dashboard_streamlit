import pandas as pd
import plotly.express as px

def crear_grafico(df):
	revenue_productos = df.groupby('product_category_name')[['valor_total']].sum().sort_values('valor_total', ascending = True).reset_index()

	fig = px.bar(revenue_productos.tail(10),
		x = 'valor_total',
		y = 'product_category_name',
		text = 'valor_total',
		title = 'Top Ingresos por Producto ($)'
	)
	fig.update_layout(yaxis_title = 'Productos', xaxis_title='Ingresos ($)', showlegend=False)
	fig.update_traces(texttemplate = '%{text:.3s}')

	return fig