import streamlit as st
import pandas as pd
import numpy as np
import geopandas as gpd
import shapefile as shp



#importar dados do excel de inventário
@st.cache(allow_output_mutation=True)
def carregarDados():    
    df = pd.read_excel("dados/GERAL_V2.xlsx", sheet_name="dados")
    
    return df 




@st.cache(allow_output_mutation=True)
def carregarDadosSHP():
    polygon = gpd.read_file("dados/Talhoes_editado10.shp")
    return polygon  

