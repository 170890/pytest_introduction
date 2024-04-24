from src.game import game
from pytest import mark

@mark.southeast
def test_where_game_recieve_sao_paulo_then_must_return_southeast():
  assert game('SAO PAULO') == 'SOUTHEAST'

@mark.southeast
def test_where_game_recieve_rio_de_janeiro_then_must_return_southeast():
  assert game('RIO DE JANEIRO') == 'SOUTHEAST'

@mark.southeast
def test_where_game_recieve_minas_gerais_then_must_return_southeast():
  assert game('MINAS GERAIS') == 'SOUTHEAST'

@mark.southeast
def test_where_game_recieve_espirito_santo_then_must_return_southeast():
  assert game('ESPIRITO SANTO') == 'SOUTHEAST'

def test_where_game_recieve_maranhao_then_must_return_north_east():
  assert game('MARANHAO') == 'NORTH EAST'

def test_where_game_recieve_bahia_then_must_return_north_east():
  assert game('BAHIA') == 'NORTH EAST'

def test_where_game_recieve_ceara_then_must_return_north_east():
  assert game('CEARA') == 'NORTH EAST'

def test_where_game_recieve_piaui_then_must_return_north_east():
  assert game('PIAUI') == 'NORTH EAST'

def test_where_game_recieve_rio_grande_do_norte_then_must_return_north_east():
  assert game('RIO GRANDE DO NORTE') == 'NORTH EAST'

def test_where_game_recieve_paraiba_then_must_return_north_east():
  assert game('PARAIBA') == 'NORTH EAST'

def test_where_game_recieve_pernambuco_then_must_return_north_east():
  assert game('PERNAMBUCO') == 'NORTH EAST'

def test_where_game_recieve_alagoas_then_must_return_north_east():
  assert game('ALAGOAS') == 'NORTH EAST'

def test_where_game_recieve_sergipe_then_must_return_north_east():
  assert game('SERGIPE') == 'NORTH EAST'

def test_where_game_recieve_acre_then_must_return_north():
  assert game('ACRE') == 'NORTH'

def test_where_game_recieve_amazonas_then_must_return_north():
  assert game('AMAZONAS') == 'NORTH'

def test_where_game_recieve_roraima_then_must_return_north():
  assert game('RORAIMA') == 'NORTH'

def test_where_game_recieve_amapa_then_must_return_north():
  assert game('AMAPA') == 'NORTH'

def test_where_game_recieve_para_then_must_return_north():
  assert game('PARA') == 'NORTH'

def test_where_game_recieve_rondonia_then_must_return_north():
  assert game('RONDONIA') == 'NORTH'

def test_where_game_recieve_tocantins_then_must_return_north():
  assert game('TOCANTINS') == 'NORTH'

def test_where_game_recieve_mato_grosso_then_must_return_midwest():
  assert game('MATO GROSSO') == 'MIDWEST'

def test_where_game_recieve_mato_grosso_do_sul_then_must_return_midwest():
  assert game('MATO GROSSO DO SUL') == 'MIDWEST'

def test_where_game_recieve_goias_then_must_return_midwest():
  assert game('GOIAS') == 'MIDWEST'

def test_where_game_recieve_brasilia_then_must_return_midwest():
  assert game('BRASILIA') == 'MIDWEST'

def test_where_game_recieve_south_then_must_return_south():
  assert game('PARANA') == 'SOUTH'

def test_where_game_recieve_santa_catarina_then_must_return_south():
  assert game('SANTA CATARINA') == 'SOUTH'

def test_where_game_recieve_rio_grande_do_sul_then_must_return_south():
  assert game('RIO GRANDE DO SUL') == 'SOUTH'