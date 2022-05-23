#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 19 18:24:34 2022

@author: vicente
"""

import pandas as pd
import geopandas as gpd

df = pd.read_excel('/home/vicente/Documentos/UFRGS/TCC/csv/IVS_arco_sul.xlsx')
gdf = gpd.read_file('/home/vicente/Documentos/GIS/gpkg/CIC.gpkg', layer='lm_mun_SUL')


df = df.loc[df['nivel'] == 'regiao,uf,rm,municipio']
df = df.loc[df['ano'] == 2010]
df = df.loc[df['label_cor'] == 'Total Cor']
df = df.loc[df['label_sexo'] == 'Total Sexo']

df = df.loc[df['label_sit_dom'] == 'Total Situação de Domicílio']
df.rename(columns={'municipio': 'cd_mun'}, inplace=True)
df.cd_mun = df.cd_mun.astype(str)

doutor = gdf.merge(df, on='cd_mun')
doutor.to_file('/home/vicente/Documentos/UFRGS/TCC/qgis/ivs.shp')