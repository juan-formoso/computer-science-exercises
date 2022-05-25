from analyzer import get_publisher
from importer import import_games
from exporter import export_data

START_MENU = """
1- VENDAS POR PUBLICANTE
2- SAIR
"""

if __name__ == "__main__":
  games = import_games("video_games.json")
  option = input(START_MENU)
  if option == "1":
    export_data(get_publisher(games))
    print("Exportado com sucesso!")
  elif option == "2":
    print("Saindo...")
  else:
    print("Opção inválida")
