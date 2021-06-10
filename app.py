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
#from IPython.core.display import display, HTML
#from pyvis.network import Network
import streamlit.components.v1 as components
#import matplotlib
#import pydot
import altair as alt


st.header("Daucus Fractal Network Analyzer")
st.subheader("Federica Trevisan")
st.write("Contributo algoritmico per semplificare il grafo trovando strutture ripetitive-ricorsive al suo interno.")


st.subheader("Grafo:")

g=net.Network(height='400px', width='50%',heading='')
g.add_nodes([1,2,3,4,5,6,7,8])
g.add_edges([(7, 1), (8, 1), (7, 8), (1, 2), (2, 3), (2, 4), (2, 5), (4, 5), (3, 6), (4, 6), (5, 6)])
#g.show('example.html')
#display(HTML('example.html'))
HtmlFile = open("example.html", 'r', encoding='utf-8')
source_code = HtmlFile.read() 
components.html(source_code, height = 400,width=1400)


st.subheader("Choose a compression method:")

df = pd.DataFrame({
  'first column': ["Singola compressione", "Multicompressione standard", "Multicompressione frattale"],
  'second column': [10, 20, 30]
})


option = st.selectbox(
    'Selezionare tipo di compressione',
     df['first column'])

'You selected: ', option

st.subheader("Choose motif:")

df = pd.DataFrame({
  'first column': ["Triangolo", "Quadrato"],
  'second column': [10, 20]
})


option = st.selectbox(
    'Selezionare tipo di motif',
     df['first column'])

'You selected: ', option

st.subheader("Animazione verticale")
st.write("esploso assonometrico. un plot per livello. colori che s'inscuriscono più vengono compressi (effetto sfumato)")

st.subheader("Animazione sul piano orizzontale")
st.write("si evidenziano i motif")

st.subheader("Risultati")
st.write("Grafo iniziale")
st.write("Grafo finale")
st.write("metriche, indici, statistiche varie in un unico vettore")
st.write("plot n. nodi per livello")

#G0 = nx.Graph()
#G0.add_edges_from([(7, 1), (8, 1), (7, 8), (1, 2), (2, 3), (2, 4), (2, 5), (4, 5), (3, 6), (4, 6), (5, 6)])
#nx.draw(G0)
#dot = nx.nx_pydot.to_pydot(G0)
#st.graphviz_chart(dot.to_string())


#col1, col2 = st.beta_columns(2)

#with col1:
#    HtmlFile = open("example.html", 'r', encoding='utf-8')
#    source_code = HtmlFile.read() 
#    components.html(source_code, height = 400,width=400)
#with col2:
#    st.graphviz_chart(dot.to_string())



#g=net.Network(height='400px', width='50%',heading='')
#g.add_node(1)
#g.add_node(2)
#g.add_node(3)
#g.add_edge(1,2)
#g.add_edge(2,3)
#g.show('example.html')
#display(HTML('example.html'))

st.subheader("Animazione sul piano orizzontale")

st.header("Risultati")
col1, col2 = st.beta_columns(2)

with col1:
    st.subheader("Grafo iniziale")
    
with col2:
    st.subheader("Grafo finale")

st.subheader("Metriche, indici, plot e statistiche")

df = pd.DataFrame(
     np.random.randn(200, 3),
     columns=['a', 'b', 'c'])

c = alt.Chart(df).mark_circle().encode(
    x='a', y='b', size='c', color='c', tooltip=['a', 'b', 'c'])

st.write(c)

chart_data = pd.DataFrame(
   np.random.randn(20, 3),
   columns=['a', 'b', 'c'])

st.line_chart(chart_data)
    


