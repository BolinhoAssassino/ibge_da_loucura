
def autoincremento(vinicial,vfinal, idade_final, idade_inicial):
	vinicial2 = vinicial 
	while vinicial <= vfinal:
		if vinicial < 100:
			print('UPDATE "Pessoa13_RR" set "V0{}" = null where "V0{}" = {} ;'.format(vinicial,vinicial, "'X'"))
		else:
			print('UPDATE "Pessoa13_RR" set "V{}" = null where "V{}" = {};'.format(vinicial,vinicial, "'X'"))
		vinicial += 1
		
	while idade_inicial<= idade_final:
		if vinicial2 < 100:
			print('insert into populacao_ano(setor, ano_nascimento ,populacao) select b.id,{}, "V0{}"::integer from "Pessoa13_RR" a, "pacotao" b where a."Cod_setor" = b."CD_GEOCODI"; '.format(" ((2020-{}||'-01-01')::varchar)::date ".format(idade_inicial),vinicial2) )
		else:
			print(' insert into populacao_ano(setor, ano_nascimento ,populacao)  select b.id,{}, "V{}"::integer from "Pessoa13_RR" a, "pacotao" b where a."Cod_setor" = b."CD_GEOCODI"; '.format(" ((2020-{}||'-01-01')::varchar)::date ".format(idade_inicial),vinicial2) )

		vinicial2 += 1
		idade_inicial += 1
def bituim(inicieixon, finalizeixon, entre):
        rank = 0
        print('with tabela as (SELECT c.id,    a.quantidade,    b.domicilios_particulares,    b.domicilios_particulares_permanentes,    c.geom ,  case ')
        while inicieixon <= finalizeixon:
                soma = inicieixon+entre
                print("when domicilios_particulares between {} and {} then '{}'".format(inicieixon,soma,'{}-{}'.format(inicieixon, soma)))
                inicieixon += entre
        print("when domicilios_particulares > {} then '{}+'".format(finalizeixon, finalizeixon))
        
        print("end  as entre FROM domicilios_renda b,    domicilios_todos a,   pacotao c  WHERE b.domicilios_id = a.id AND a.setor = c.id) select *, regexp_replace(case when entre = '1000000+' then '990000100000009999' else entre end ,'[-+]','')::bigint as rank  from tabela")
# // -- tabela de setores tem q ter o nome de pacotao EXEMPLO autoincremento(35, 134, 100,1)
