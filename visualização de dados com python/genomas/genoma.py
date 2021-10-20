def gera_mapa(arquivo_fasta):
    sequencia_dna = open(f'{arquivo_fasta}.fasta').read()
    sequencia_dna = sequencia_dna.replace('\n', '')

    moleculas = ['A', 'T', 'C', 'G']

    cont = {}

    for i in moleculas:
        for j in moleculas:
            cont[i + j] = 0

    for i in range(len(sequencia_dna) - 1):
        cont[sequencia_dna[i] + sequencia_dna[i + 1]] += 1

    html= open(f'{arquivo_fasta}.html', 'w')

    i = 1
    for j in cont:
        transparencia = cont[j] / max(cont.values())

        html.write(f'''<div style="
            width: 100px;
            height: 100px;
            border: 1px solid #111;
            float: left;
            color: #fff;
            background-color: rgba(0, 0, 255, {str(transparencia)});
        ">{j}</div>''')

        if i % 4 == 0:
            html.write('<div style="clear: both"></div>')
        
        i += 1
    html.close()

gera_mapa('bacteria')