import sys
import shutil
import os

if len(sys.argv) < 2:
    print("Uso: python switch_readme.py [pt|en]")
    sys.exit(1)

idioma = sys.argv[1]
arquivo_origem = f"README.{idioma}.md"
arquivo_destino = "README.md"

if not os.path.exists(arquivo_origem):
    print(f"Erro: Arquivo não encontrado: {arquivo_origem}")
    sys.exit(1)

shutil.copyfile(arquivo_origem, arquivo_destino)
print(f"✅ README atualizado para o idioma: {idioma}")
