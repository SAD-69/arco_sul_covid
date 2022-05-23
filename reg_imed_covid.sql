SELECT  SUM(a.confirmado) as casos_confirmados, SUM(a.mortes) as mortes_confirmadas, SUM(a.populaca_1) as pop_estimada19, b.*
FROM pt_covid_sul_region a, lm_reg_imed b
WHERE a.rgi = b.rgi
GROUP BY b.rgi