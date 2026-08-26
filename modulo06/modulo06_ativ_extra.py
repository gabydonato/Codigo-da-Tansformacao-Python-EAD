import shutil
import os

origem = "arquivos_importantes"
destino = "backup"

if not os.path.exists(destino):
    os.mkdir(destino)

shutil.copy("arquivos_importantes/documento.txt", destino)

print("Backup realizado com sucesso!")