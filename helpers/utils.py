import os

def full_path(path: str) -> None:
  return os.path.join(os.getcwd(), path)
