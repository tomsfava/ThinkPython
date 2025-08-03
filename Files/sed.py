import os

def sed(pattern, replacement, fin, fout):
    try:
        if not os.path.exists(fin):
            raise FileNotFoundError(f"Arquivo '{fin}' não encontrado!")
        
        with open(fin, 'r') as fin_file:
            lines = fin_file.readlines()

        new_lines = []
        for line in lines:
            new_line = line.replace(pattern, replacement)
            new_lines.append(new_line)

        with open(fout, 'w') as fout_file:
            fout_file.writelines(new_lines)

        print(f"Substituição concluída! Resultado salvo em '{fout}'.")

    except FileNotFoundError as e:
        print(f"Erro: {e}")
    except IOError as e:
        print(f"Erro de I/O: {e}")
    except Exception as e:
        print(f"Erro inesperado: {e}")

if __name__ == '__main__':
    fin = 'notas.md'
    fout = 'novasnotas.md'
    pattern = 'os'
    replacement = 'cu'
    sed(pattern, replacement, fin, fout)