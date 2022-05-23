#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 22 09:14:33 2022

@author: vicente
"""

import pandas as pd
import geopandas as gpd

df = pd.read_csv('/home/vicente/Documentos/UFRGS/TCC/csv/par_covid.csv', encoding='utf-16', sep='\t')
gdf = gpd.read_file('/home/vicente/Documentos/GIS/gpkg/CIC.gpkg', layer='PRY_adm1')

df2 = df.groupby('Departamento Residencia', as_index=False).sum()
df2.rename(columns={'Departamento Residencia': 'name_1'}, inplace=True)

df2.name_1 = df2.name_1.str.title()
gdf.name_1 = gdf.name_1.str.normalize('NFKD').str.encode('ascii', errors='ignore').str.decode('utf-8')

gdf2 = gdf.merge(df2, on='name_1')

gdf2.to_file('/home/vicente/Documentos/GIS/gpkg/par_covid.geojson', driver='GeoJSON')