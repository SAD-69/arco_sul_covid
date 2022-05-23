#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 21 21:03:39 2022

@author: vicente
"""

# import seaborn as sb
import geopandas as gpd
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from esda.moran import Moran_BV, Moran_Local_BV, Moran, Moran_Local
from pysal.lib import weights
from splot.esda import moran_scatterplot, lisa_cluster, plot_local_autocorrelation, plot_moran_bv, plot_moran_bv_simulation, plot_moran

# GeoDataframes

covid = gpd.read_file('/home/vicente/Documentos/GIS/gpkg/lm_mun_covid_sul.shp')
# acessos = gpd.read_file('/home/vicente/Documentos/GIS/gpkg/CIC.gpkg', layer='acesso_ibge_2018')
ivs = gpd.read_file('/home/vicente/Documentos/GIS/gpkg/CIC.gpkg', layer='ivs')
# join = pd.merge(covid, acessos, how='inner', left_on='cd_mun', right_on='cd_geocmu')

join = pd.merge(covid, ivs, on='cd_mun')
del ivs, covid


join.drop(columns='geometry_x', inplace=True)
join.rename(columns={'geometry_y': 'geometry'}, inplace=True)

join = join[join['confirmado'].notna()]


# Matriz de distância tipo Rainha

w = weights.Queen.from_dataframe(join, geom_col='geometry')
w.transform = 'R'

# y = np.log(join['confirmado'])
y = join['taxa_letal']

join['lag'] = weights.lag_spatial(w, y)


mi = Moran(join['lag'], w)
mi_bv = Moran_BV(join['lag'], join['ivs'].values, w)
lisa = Moran_Local(join['lag'], w)
lisa_bv = Moran_Local_BV(join['lag'], join['ivs'].values, w) 

plot_moran(mi)
plot_moran_bv(mi_bv)

plot_local_autocorrelation(lisa, join, 'taxa_letal')
plot_local_autocorrelation(lisa_bv, join, 'taxa_letal')


print(mi.I)