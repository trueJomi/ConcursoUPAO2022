from data import Marciano1

def cifrar(frase:str):
    mensaje=''
    for i in frase:
        for f in Marciano1:
            k=Marciano1.get(f)
            if i.upper()==f:
                mensaje=mensaje+k
                break
        else:
            mensaje=mensaje+i
    return mensaje


def run():
    frase='hola1'
    print(cifrar(frase))

if __name__ == "__main__":
    run()