#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May  2 12:32:32 2022

@author: vicente
"""

import requests
import geopandas as gpd
import pandas as pd
# from dateutil import parser


df = gpd.read_file('/home/vicente/Documentos/GIS/gpkg/CIC.gpkg', layer='lm_mun_SUL')

df['confirmados'] = None
df['confirmados_por_100mil'] = None
df['mortes'] = None
df['taxa_letalidade'] = None
df['populacao_estimada2010'] = None
df['populacao_estimada2019'] = None

df['ultima_atualizacao'] = None

estados = ['RS', 'SC', 'PR']
for state in estados:
    for month in range(1,13):

        month_f = "{:02d}".format(month)
    
        token = 'd37d568ba2595cd598004b78abba369580706c9b'
        api = f'https://api.brasil.io/v1/dataset/covid19/caso/data/?islast=False&state={state}&date=2021-{month_f}-25'
        head = {"Authorization": f"Token {token}"}
        
        get = requests.get(api, headers=head)
        
        if get.ok:
            page = get.json()

        
    
for i, geocodigo in enumerate(df['cd_mun']):
        
    dados = page['results']
    
    for resultado in dados:
        if resultado['city_ibge_code'] == geocodigo:
            print(f"Quantidade de confirmados - {resultado['confirmed']} no dia {resultado['date']}")
            
            df['confirmados'][i] = resultado['confirmed']
            df['confirmados_por_100mil'][i] = resultado['confirmed_per_100k_inhabitants']
            df['mortes'][i] = resultado['deaths']
            df['taxa_letalidade'][i] = resultado['death_rate']
            df['populacao_estimada2010'][i] = resultado['estimated_population']
            df['populacao_estimada2019'][i] = resultado['estimated_population_2019']
            df['ultima_atualizacao'][i] = resultado['date']

# df['ultima_atualizacao'][i] = gpd.to_datetime
df = df.astype({
    'confirmados': 'Int64',
    'mortes': 'Int64',
    'populacao_estimada2010': 'Int64',
    'populacao_estimada2019': 'Int64',
    'confirmados_por_100mil': 'float64',
    'taxa_letalidade': 'float64'})


df.to_file(f'/home/vicente/Documentos/GIS/covid19/2021/lm_mun_covid_sul_2021_{month}_25.shp')