#!/usr/bin/env python3
import sys
from pathlib import Path

# Get base dir
# target_dir = sys.argv[1] if len(sys.argv) > 1 else "."

def get_files(target_dir):
  routes = []
  # rglob('*') busca recursivamente en todos los subdirectorios
  for path in Path(target_dir).rglob('*'):
    if path.is_file():
      routes.append(path)
  # Retorna tupla de rutas
  return routes