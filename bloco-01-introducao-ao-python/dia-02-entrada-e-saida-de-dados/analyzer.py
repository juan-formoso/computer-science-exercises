from importer import import_games

def get_publisher(video_games):
  publishers = set()
  for game in video_games:
    publishers.add(game["Publisher"])
  return publishers

if __name__ == "__main__":
  games = import_games("video_games.json")
  print(get_publisher(games))
