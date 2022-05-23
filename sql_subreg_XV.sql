SELECT a.* 
FROM lml_municipio_a a
WHERE a.nome IN ('Altônia','Cafezal do Sul','Cidade Gaúcha','Cruzeiro do Oeste',
'Douradina','Esperança Nova','Guaíra','Icaraíma','Ivaté','Maria Helena','Nova
Olímpia','Perobal','Pérola','Querência do Norte','Rondon','Santa Cruz do Monte
Castelo','Santa Isabel do Ivaí','Santa Mônica','São José do Patrocínio','Tapejara',
'Tapira','Umuarama','Vila Alta','Xambrê') 
AND  SUBSTRING(a.geocodigo, 1, 2) IN ('41')