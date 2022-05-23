#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 22 09:01:42 2022

@author: vicente
"""

import pandas as pd
import geopandas as gpd

gdf = gpd.read_file('/home/vicente/Documentos/GIS/gpkg/CIC.gpkg', layer='UY_poblacion')
df = pd.read_csv('/home/vicente/Documentos/UFRGS/TCC/csv/estadisticasUY_porDepto_detalle_ajustado.csv')

df2 = df.groupby('departamento', as_index=False).sum()

df2['NAME_1'] = df2.departamento.str.split("(").str[0]

gdf = gdf.merge(df2, on='NAME_1')

gdf.to_file('/home/vicente/Documentos/GIS/gpkg/covid_uy.geojson', driver='GeoJSON')