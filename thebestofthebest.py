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

# // -- tabela de setores tem q ter o nome de pacotao EXEMPLO autoincremento(35, 134, 100,1)
