import sys

def get_param(param_index, desc = ''):
    value_param = ''
    try:
        value_param = sys.argv[param_index]
    except:
        print('Houve um erro ao ler o parâmetro')
    
    return value_param

parametro = float(get_param(1))
print(f"{parametro:.0f}")