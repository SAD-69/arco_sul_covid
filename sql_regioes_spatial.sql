SELECT
	covid_pt.*, 
	b.rgint
FROM  
	(SELECT 
	a.*,
	b.rgi
	 FROM 
	covid_arco_sul_pts a, lm_reg_imed b
	 WHERE ST_INTERSECTS(a.geom, b.geom)) AS covid_pt,  
	lm_reg_int b

WHERE ST_INTERSECTS(covid_pt.geom, b.geom)
