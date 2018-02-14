# Index:
# ----------------------
# 1. General options
# 2. School sites

# 1. General Options
# ======================================================
api_token = "" 												# the token you took from t.me/botfather
log_channel = ""          		            				# insert an id to send features, bugs or errors
super_user = ""								       			# for actions that just this user can do
db_name = "data.db"											# where to save data

welcome_back = "Bentornato, {}, se vuoi cambiare le tue Informazioni, digita /setup"
bug_msg = "Descrivi il tuo bug con quanti più dettagli possibili:"
feature_msg = "Descrivi la tua richiesta con quanti più dettagli possibili:"
general_info = "Ciao, {}, sono UniToHelper, un bot creato apposta per semplificarti piccole azioni quotidiane, ti farò qualche domanda, in modo tale da automatizzare alcune funzioni..."

'''
    2. School sites section
'''

# 2.1 Dipartimento di informatica
# ======================================================
di_first_years = "http://laurea.educ.di.unito.it/index.php/offerta-formativa/calendario/orari/orario-primi-anni?tipoLaurea={}&annoDiCorso={}&AA={}&semestre={}"      # Primi anni (1, 2)
di_third_year = "http://laurea.educ.di.unito.it/index.php/offerta-formativa/calendario/orari/orario-curriculum?tipoLaurea={}&corso={}&AA={}&semestre={}"              # Curricula terzo anno (3)
di_masterly = "http://magistrale.educ.di.unito.it/index.php/offerta-formativa/calendario/orari/orario-completo?tipoLaurea=M&completo=Magistrale&AA={}&semestre={}"    # Magistrale (4, 5)

courses = {'A' : 'A', 'B' : 'B', 'E' : 'Informazione e conoscenza', 'N' : 'Linguaggi e Sistemi', 'S' : 'Reti e Sistemi Informatici', 'DI-STI' : 'Sistemi per il trattamento dell\'informazione', 'DI-RVM' : 'Realtà Virtuale e Multimedialità', 'DI-RSI' : 'Reti e Sistemi Informatici'}
