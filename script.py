# -*- coding: utf-8 -*-
"""
Created on Tue May 18 02:15:34 2021

@author: leotm
"""


#código usado para as analises

import pandas as pd

data_2006 = pd.read_csv('ETLSINASC.DNRES_2006.csv', sep='\t')

rp_2006 = data_2006.loc[data_2006['nasc_MUNNOMEX'] == 'RIBEIRAO PRETO']

sinha_2006 = rp_2006.loc[rp_2006['CODESTAB'] == 2078791]

hc_2006 = rp_2006.loc[rp_2006['CODESTAB'] == 2082187]

hosp_sao_paulo_2006 = rp_2006.loc[rp_2006['CODESTAB'] == 2079038]

mater_2006 = rp_2006.loc[rp_2006['CODESTAB'] == 2079119]

santa_casa_2006 = rp_2006.loc[rp_2006['CODESTAB'] == 2084414]

sao_lucas_2006 = rp_2006.loc[rp_2006['CODESTAB'].isin([5171946, 2077973, 3604624])]

santa_lydia_2006 = rp_2006.loc[rp_2006['CODESTAB'] == 2081164]

electro_bonini_2006 = rp_2006.loc[rp_2006['CODESTAB'] == 3314766]

publico = [mater_2006, santa_casa_2006, hc_2006, santa_lydia_2006, electro_bonini_2006]

publico_2006 = pd.concat(publico)

privado = [sinha_2006, hosp_sao_paulo_2006, sao_lucas_2006]

privado_2006 = pd.concat(privado)





publico = [publico_2017, publico_2016, publico_2014, publico_2013, publico_2012, publico_2011, publico_2010, publico_2009, publico_2008, publico_2007, publico_2006]

publico_df = pd.concat(publico)

privado = [privado_2017, privado_2016, privado_2014, privado_2013, privado_2012, privado_2011, privado_2010, privado_2009, privado_2008, privado_2007, privado_2006]

privado_df = pd.concat(privado)










publico_df[['NUMERODN', 'def_parto']].groupby( 'def_parto' ).count()

privado_df[['NUMERODN', 'def_parto']].groupby( 'def_parto' ).count()



publico_df['idade'] = 'idade'
privado_df['idade'] = 'idade'

publico_df.loc[publico_df['IDADEMAE'] < 20, 'idade'] = '<20'
publico_df.loc[publico_df['IDADEMAE'] >= 20, 'idade'] = '20-30'
publico_df.loc[publico_df['IDADEMAE'] > 30, 'idade'] = '>30'

privado_df.loc[privado_df['IDADEMAE'] < 20, 'idade'] = '<20'
privado_df.loc[privado_df['IDADEMAE'] >= 20, 'idade'] = '20-30'
privado_df.loc[privado_df['IDADEMAE'] > 30, 'idade'] = '>30'


publico_df[['NUMERODN', 'idade']].groupby( 'idade' ).count()

privado_df[['NUMERODN', 'idade']].groupby( 'idade').count()



publico_df[['NUMERODN', 'def_raca_cor']].groupby( 'def_raca_cor' ).count()

privado_df[['NUMERODN', 'def_raca_cor']].groupby( 'def_raca_cor' ).count()



publico_df[['NUMERODN', 'def_est_civil']].groupby( 'def_est_civil' ).count()

privado_df[['NUMERODN', 'def_est_civil']].groupby( 'def_est_civil' ).count()


publico_df[['NUMERODN', 'def_escol_mae']].groupby( 'def_escol_mae' ).count()

privado_df[['NUMERODN', 'def_escol_mae']].groupby( 'def_escol_mae' ).count()


publico_df[['NUMERODN', 'PARIDADE']].groupby( 'PARIDADE' ).count()

privado_df[['NUMERODN', 'PARIDADE']].groupby( 'PARIDADE' ).count()


publico_df[['NUMERODN', 'def_gravidez']].groupby( 'def_gravidez' ).count()

privado_df[['NUMERODN', 'def_gravidez']].groupby( 'def_gravidez' ).count()


publico_df[['NUMERODN', 'STCESPARTO']].groupby( 'STCESPARTO' ).count()

privado_df[['NUMERODN', 'STCESPARTO']].groupby( 'STCESPARTO' ).count()


publico_df[['NUMERODN', 'STTRABPART']].groupby( 'STTRABPART' ).count()

privado_df[['NUMERODN', 'STTRABPART']].groupby( 'STTRABPART' ).count()

publico_df[['NUMERODN', 'TPROBSON']].groupby( 'TPROBSON' ).count()

privado_df[['NUMERODN', 'TPROBSON']].groupby( 'TPROBSON' ).count()


publico_df['ces_prev'] = 'prev'
privado_df['ces_prev'] = 'prev'


publico_df.loc[publico_df['QTDPARTCES'] == 0, 'ces_prev'] = 'Não'
publico_df.loc[publico_df['QTDPARTCES'] > 0, 'ces_prev'] = 'Sim'

privado_df.loc[privado_df['QTDPARTCES'] == 0, 'ces_prev'] = 'Não'
privado_df.loc[privado_df['QTDPARTCES'] > 0, 'ces_prev'] = 'Sim'


publico_df[['NUMERODN', 'ces_prev']].groupby( 'ces_prev' ).count()

privado_df[['NUMERODN', 'ces_prev']].groupby( 'ces_prev' ).count()


publico_df[['NUMERODN', 'def_consultas']].groupby( 'def_consultas' ).count()

privado_df[['NUMERODN', 'def_consultas']].groupby( 'def_consultas' ).count()


#registros publicos e privados

registros_publicos = publico_2006.shape[0] + publico_2007.shape[0] + publico_2008.shape[0] + publico_2009.shape[0] + publico_2010.shape[0] + publico_2011.shape[0] + publico_2012.shape[0] + publico_2013.shape[0] + publico_2014.shape[0] + publico_2016.shape[0] + publico_2017.shape[0]

registros_privados = privado_2006.shape[0] + privado_2007.shape[0] + privado_2008.shape[0] + privado_2009.shape[0] + privado_2010.shape[0] + privado_2011.shape[0] + privado_2012.shape[0] + privado_2013.shape[0] + privado_2014.shape[0] + privado_2016.shape[0] + privado_2017.shape[0]






registros_sinha = sinha_2006.shape[0] + sinha_2007.shape[0] + sinha_2008.shape[0] + sinha_2009.shape[0] + sinha_2010.shape[0] + sinha_2011.shape[0] + sinha_2012.shape[0] + sinha_2013.shape[0] + sinha_2014.shape[0] + sinha_2016.shape[0] + sinha_2017.shape[0]

registros_mater = mater_2006.shape[0] + mater_2007.shape[0] + mater_2008.shape[0] + mater_2009.shape[0] + mater_2010.shape[0] + mater_2011.shape[0] + mater_2012.shape[0] + mater_2013.shape[0] + mater_2014.shape[0] + mater_2016.shape[0] + mater_2017.shape[0]

registros_hosp_sao_paulo = hosp_sao_paulo_2006.shape[0] + hosp_sao_paulo_2007.shape[0] + hosp_sao_paulo_2008.shape[0] + hosp_sao_paulo_2009.shape[0] + hosp_sao_paulo_2010.shape[0] + hosp_sao_paulo_2011.shape[0] + hosp_sao_paulo_2012.shape[0] + hosp_sao_paulo_2013.shape[0] + hosp_sao_paulo_2014.shape[0] + hosp_sao_paulo_2016.shape[0] + hosp_sao_paulo_2017.shape[0]

registros_hc = hc_2006.shape[0] + hc_2007.shape[0] + hc_2008.shape[0] + hc_2009.shape[0] + hc_2010.shape[0] + hc_2011.shape[0] + hc_2012.shape[0] + hc_2013.shape[0] + hc_2014.shape[0] + hc_2016.shape[0] + hc_2017.shape[0]

registros_santa_casa = santa_casa_2006.shape[0] + santa_casa_2007.shape[0] + santa_casa_2008.shape[0] + santa_casa_2009.shape[0] + santa_casa_2010.shape[0] + santa_casa_2011.shape[0] + santa_casa_2012.shape[0] + santa_casa_2013.shape[0] + santa_casa_2014.shape[0] + santa_casa_2016.shape[0] + santa_casa_2017.shape[0]

registros_sao_lucas = sao_lucas_2006.shape[0] + sao_lucas_2007.shape[0] + sao_lucas_2008.shape[0] + sao_lucas_2009.shape[0] + sao_lucas_2010.shape[0] + sao_lucas_2011.shape[0] + sao_lucas_2012.shape[0] + sao_lucas_2013.shape[0] + sao_lucas_2014.shape[0] + sao_lucas_2016.shape[0] + sao_lucas_2017.shape[0]

registros_electro_bonini = electro_bonini_2014.shape[0] + electro_bonini_2016.shape[0] + electro_bonini_2017.shape[0]

registros_santa_lydia = santa_lydia_2006.shape[0] + santa_lydia_2007.shape[0] + santa_lydia_2008.shape[0] + santa_lydia_2009.shape[0] + santa_lydia_2010.shape[0] + santa_lydia_2011.shape[0] + santa_lydia_2012.shape[0] + santa_lydia_2013.shape[0] + santa_lydia_2014.shape[0] + santa_lydia_2016.shape[0] + santa_lydia_2017.shape[0]

'''

#td = rp_2017[rp_2017['CODESTAB'] != 2079119]
#tdb = td[td['CODESTAB'] != 2078791]
#tdc = tdb[tdb['CODESTAB'] != 2082187]
#tdd = tdc[tdc['CODESTAB'] != 2079038]
#tde = tdd[tdd['CODESTAB'] != 2084414]
#tdf = tde[tde['CODESTAB'] != 5171946]
#tdg = tdf[tdf['CODESTAB'] != 2081164]
#tdh = tdg[tdg['CODESTAB'] != 3314766]
#tdi = tdh[tdh['CODESTAB'] != 2077973]
#tdj = tdi[tdi['CODESTAB'] != 3604624]
#print(rp_2017.head())

#print(rp_2017[['nasc_MUNNOME','CODESTAB', 'IDADEMAE', 'QTDFILVIVO']].sort_values( 'QTDFILVIVO', ascending=False  ))

#sp = data_2017[data_2017['nasc_MUNNOMEX'] == 'SAO PAULO']
#print(sp[['nasc_MUNNOME','CODESTAB', 'IDADEMAE']].sort_values( 'IDADEMAE' ))

#print(tdj[['nasc_MUNNOME','CODESTAB', 'IDADEMAE']].sort_values( 'IDADEMAE' ))


registros_sinha = sinha_2017.shape[0] + sinha_2007.shape[0] + sinha_2008.shape[0] + sinha_2009.shape[0] + sinha_2010.shape[0] + sinha_2011.shape[0] + sinha_2012.shape[0] + sinha_2013.shape[0] + sinha_2014.shape[0] + sinha_2016.shape[0] + sinha_2017.shape[0]

registros_mater = mater_2017.shape[0] + mater_2007.shape[0] + mater_2008.shape[0] + mater_2009.shape[0] + mater_2010.shape[0] + mater_2011.shape[0] + mater_2012.shape[0] + mater_2013.shape[0] + mater_2014.shape[0] + mater_2016.shape[0] + mater_2017.shape[0]

registros_hosp_sao_paulo = hosp_sao_paulo_2017.shape[0] + hosp_sao_paulo_2007.shape[0] + hosp_sao_paulo_2008.shape[0] + hosp_sao_paulo_2009.shape[0] + hosp_sao_paulo_2010.shape[0] + hosp_sao_paulo_2011.shape[0] + hosp_sao_paulo_2012.shape[0] + hosp_sao_paulo_2013.shape[0] + hosp_sao_paulo_2014.shape[0] + hosp_sao_paulo_2016.shape[0] + hosp_sao_paulo_2017.shape[0]

registros_hc = hc_2017.shape[0] + hc_2007.shape[0] + hc_2008.shape[0] + hc_2009.shape[0] + hc_2010.shape[0] + hc_2011.shape[0] + hc_2012.shape[0] + hc_2013.shape[0] + hc_2014.shape[0] + hc_2016.shape[0] + hc_2017.shape[0]

registros_santa_casa = santa_casa_2017.shape[0] + santa_casa_2007.shape[0] + santa_casa_2008.shape[0] + santa_casa_2009.shape[0] + santa_casa_2010.shape[0] + santa_casa_2011.shape[0] + santa_casa_2012.shape[0] + santa_casa_2013.shape[0] + santa_casa_2014.shape[0] + santa_casa_2016.shape[0] + santa_casa_2017.shape[0]

registros_sao_lucas = sao_lucas_2017.shape[0] + sao_lucas_2007.shape[0] + sao_lucas_2008.shape[0] + sao_lucas_2009.shape[0] + sao_lucas_2010.shape[0] + sao_lucas_2011.shape[0] + sao_lucas_2012.shape[0] + sao_lucas_2013.shape[0] + sao_lucas_2014.shape[0] + sao_lucas_2016.shape[0] + sao_lucas_2017.shape[0]

registros_electro_bonini = electro_bonini_2014.shape[0] + electro_bonini_2016.shape[0] + electro_bonini_2017.shape[0]

registros_santa_lydia = santa_lydia_2017.shape[0] + santa_lydia_2007.shape[0] + santa_lydia_2008.shape[0] + santa_lydia_2009.shape[0] + santa_lydia_2010.shape[0] + santa_lydia_2011.shape[0] + santa_lydia_2012.shape[0] + santa_lydia_2013.shape[0] + santa_lydia_2014.shape[0] + santa_lydia_2016.shape[0] + santa_lydia_2017.shape[0]


rp_2017[['NUMERODN', 'def_parto']].groupby( 'def_parto' ).count()

rp_1997[['NUMERODN', 'def_parto']].groupby( 'def_parto' ).count()

rp_1998[['NUMERODN', 'def_parto']].groupby( 'def_parto' ).count()

rp_1999[['NUMERODN', 'def_parto']].groupby( 'def_parto' ).count()

rp_2000[['NUMERODN', 'def_parto']].groupby( 'def_parto' ).count()

rp_2001[['NUMERODN', 'def_parto']].groupby( 'def_parto' ).count()

rp_2002[['NUMERODN', 'def_parto']].groupby( 'def_parto' ).count()

rp_2003[['NUMERODN', 'def_parto']].groupby( 'def_parto' ).count()

rp_2004[['NUMERODN', 'def_parto']].groupby( 'def_parto' ).count()

rp_2005[['NUMERODN', 'def_parto']].groupby( 'def_parto' ).count()

rp_2006[['NUMERODN', 'def_parto']].groupby( 'def_parto' ).count()

rp_2007[['NUMERODN', 'def_parto']].groupby( 'def_parto' ).count()

rp_2008[['NUMERODN', 'def_parto']].groupby( 'def_parto' ).count()

rp_2009[['NUMERODN', 'def_parto']].groupby( 'def_parto' ).count()

rp_2010[['NUMERODN', 'def_parto']].groupby( 'def_parto' ).count()

rp_2011[['NUMERODN', 'def_parto']].groupby( 'def_parto' ).count()

rp_2012[['NUMERODN', 'def_parto']].groupby( 'def_parto' ).count()

rp_2013[['NUMERODN', 'def_parto']].groupby( 'def_parto' ).count()

rp_2014[['NUMERODN', 'def_parto']].groupby( 'def_parto' ).count()

rp_2016[['NUMERODN', 'def_parto']].groupby( 'def_parto' ).count()

rp_2017[['NUMERODN', 'def_parto']].groupby( 'def_parto' ).count()

'''








