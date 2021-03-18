# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import streamlit as st
import pandas as pd
import numpy as np
import networkx as nx
from pyvis import network as net
from IPython.core.display import display, HTML
from pyvis.network import Network
import streamlit.components.v1 as components


st.title("Demo algoritmo")
st.header("Approccio gerarchico")
st.write("Contributo algoritmico per semplificare il grafo trovando strutture ripetitive-ricorsive al suo interno.")



st.write("Procedura:")
code = '''
    Rinominare nodi del grafo G con il livello corrispondente. Tupla: (livello, nodo) 
    Identificare sottografo motif nel grafo G (motif definiti nel file pattern.ipynb)
    Collassare il motif in un solo nodo
    Memorizzare quali nodi si comprimono nel nuovo nodo
    (Aggiornare il peso e il colore degli archi)
    Riapplicare il procedimento al grafo risultante in un nuovo livello
'''
st.code(code, language='python')

df = pd.DataFrame({
  'first column': ["Singola compressione", "Multicompressione standard", "Multicompressione frattale"],
  'second column': [10, 20, 30]
})


option = st.selectbox(
    'Selezionare tipo di compressione',
     df['first column'])

'You selected: ', option


g=net.Network(height='400px', width='50%',heading='')
g.add_nodes([1,2,3,4,5,6,7,8])
g.add_edges([(7, 1), (8, 1), (7, 8), (1, 2), (2, 3), (2, 4), (2, 5), (4, 5), (3, 6), (4, 6), (5, 6)])
#g.show('example.html')
#display(HTML('example.html'))



G0 = nx.Graph()
G0.add_edges_from([(7, 1), (8, 1), (7, 8), (1, 2), (2, 3), (2, 4), (2, 5), (4, 5), (3, 6), (4, 6), (5, 6)])
nx.draw(G0)
dot = nx.nx_pydot.to_pydot(G0)
#st.graphviz_chart(dot.to_string())


col1, col2 = st.beta_columns(2)

with col1:
    HtmlFile = open("example.html", 'r', encoding='utf-8')
    source_code = HtmlFile.read() 
    components.html(source_code, height = 400,width=400)
with col2:
    st.graphviz_chart(dot.to_string())



#g=net.Network(height='400px', width='50%',heading='')
#g.add_node(1)
#g.add_node(2)
#g.add_node(3)
#g.add_edge(1,2)
#g.add_edge(2,3)
#g.show('example.html')
#display(HTML('example.html'))

chart_data = pd.DataFrame(
     np.random.randn(20, 3),
     columns=['a', 'b', 'c'])

st.line_chart(chart_data)

st.write("Here's our first attempt at using data to create a table:")
st.write(pd.DataFrame({
    'first column': [1, 2, 3, 4],
    'second column': [10, 20, 30, 40]
}))


chart_data = pd.DataFrame(
     np.random.randn(20, 3),
     columns=['a', 'b', 'c'])

st.line_chart(chart_data)


if st.checkbox('Show dataframe'):
    chart_data = pd.DataFrame(
       np.random.randn(20, 3),
       columns=['a', 'b', 'c'])

    st.line_chart(chart_data)
    


@st.cache
def get_data():
    return pd.read_csv("http://data.insideairbnb.com/united-states/ny/new-york-city/2019-09-12/visualisations/listings.csv")

df = get_data()

st.markdown("Welcome to this in-depth introduction to [Streamlit](www.streamlit.io)! For this exercise, we'll use an Airbnb [dataset](http://data.insideairbnb.com/united-states/ny/new-york-city/2019-09-12/visualisations/listings.csv) containing NYC listings.")
st.header("Customary quote")
st.markdown("> I just love to go home, no matter where I am, the most luxurious hotel suite in the world, I love to go home.\n\n—Michael Caine")
st.header("Airbnb NYC listings: data at a glance")
st.markdown("The first five records of the Airbnb data we downloaded.")
st.dataframe(df.head())
st.header("Caching our data")
st.markdown("Streamlit has a handy decorator [`st.cache`](https://streamlit.io/docs/api.html#optimize-performance) to enable data caching.")
st.code("""
@st.cache
def get_data():
    url = "http://data.insideairbnb.com/united-states/ny/new-york-city/2019-09-12/visualisations/listings.csv"
    return pd.read_csv(url)
""", language="python")
st.markdown("_To display a code block, pass in the string to display as code to [`st.code`](https://streamlit.io/docs/api.html#streamlit.code)_.")
with st.echo():
    st.markdown("Alternatively, use [`st.echo`](https://streamlit.io/docs/api.html#streamlit.echo).")

st.header("Where are the most expensive properties located?")
st.subheader("On a map")
st.markdown("The following map shows the top 1% most expensive Airbnbs priced at $800 and above.")
st.map(df.query("price>=800")[["latitude", "longitude"]].dropna(how="any"))
st.subheader("In a table")
st.markdown("Following are the top five most expensive properties.")
st.write(df.query("price>=800").sort_values("price", ascending=False).head())

st.subheader("Selecting a subset of columns")
st.write(f"Out of the {df.shape[1]} columns, you might want to view only a subset. Streamlit has a [multiselect](https://streamlit.io/docs/api.html#streamlit.multiselect) widget for this.")
defaultcols = ["name", "host_name", "neighbourhood", "room_type", "price"]
cols = st.multiselect("Columns", df.columns.tolist(), default=defaultcols)
st.dataframe(df[cols].head(10))

st.header("Average price by room type")
st.write("You can also display static tables. As opposed to a data frame, with a static table you cannot sorting by clicking a column header.")
st.table(df.groupby("room_type").price.mean().reset_index()\
    .round(2).sort_values("price", ascending=False)\
    .assign(avg_price=lambda x: x.pop("price").apply(lambda y: "%.2f" % y)))
