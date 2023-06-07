from lexico import Lexico
import re


def read(path):
    with open(path) as f:
        lines = f.read().splitlines()

    string = "".join(lines)
    return string

def print_results(results):
    # print(results)
    result = list()
    for i in range(len(results)):
        # print(results[i].__str__())
        result.append(results[i].value)
        
    return result



def main():
    # file = input('name of the .txt archive to read?: ')
    # path = f'./{file}' ###
    path = './sourceCode1.txt'
    print(path)
    chain = read(path)       #  Abrir codigo fuente
                           
    chain = re.sub(r"\s+", "", chain, flags=re.UNICODE) #Remover espacios en blanco

    #chain = re.sub(r"\/\*[\s\S]*?\*\/|\/\/.*$", "", chain) #Lee comentarios con /*---*/ y //
    chain = re.sub(r"\/\*[\s\S]*?\*\/", "", chain) #lee comentarios solo con /*---*/
    
    # print(chain)
    lexer = Lexico()
    lexer.read(chain)
    results = lexer.results
    list_results = print_results(results)
    # print(list_results)
    return list_results
