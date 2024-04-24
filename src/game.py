def game(state):

    state = state.upper()
    brazil_state = {
        "ACRE": "NORTH",
        "AMAZONAS": "NORTH",
        "RORAIMA": "NORTH",
        "AMAPA": "NORTH",
        "PARA": "NORTH",
        "RONDONIA": "NORTH",
        "TOCANTINS": "NORTH",
        "MARANHAO": "NORTH EAST",
        "PIAUI": "NORTH EAST",
        "CEARA": "NORTH EAST",
        "RIO GRANDE DO NORTE": "NORTH EAST",
        "PARAIBA": "NORTH EAST",
        "PERNAMBUCO": "NORTH EAST",
        "ALAGOAS": "NORTH EAST",
        "SERGIPE": "NORTH EAST",
        "BAHIA": "NORTH EAST",
        "MATO GROSSO": "MIDWEST",
        "MATO GROSSO DO SUL": "MIDWEST",
        "GOIAS": "MIDWEST",
        "BRASILIA": "MIDWEST",
        "MINAS GERAIS": "SOUTHEAST",
        "SAO PAULO": "SOUTHEAST",
        "ESPIRITO SANTO": "SOUTHEAST",
        "RIO DE JANEIRO": "SOUTHEAST",
        "PARANA": "SOUTH",
        "SANTA CATARINA": "SOUTH",
        "RIO GRANDE DO SUL": "SOUTH"
    }

    print('I joined in the game')

    if state in brazil_state:
        return brazil_state.get(state)
    else:
        return 'State not found'
    
    print('END GAME!')