def open_file(filePath):
  try:
    with open(filePath, mode='r') as file:
       print(file.read())
      
  except FileNotFoundError:
    print("No such file found")
  
def userpath():
  path = input("Enter you file path (Notes/Wisdom.txt): ")
  if path:
     return f"/storage/emulated/0/{path}"
  else:
    print("Home dir")
    return "/storage/emulated/0"
  
path = userpath()
open_file(path)      
