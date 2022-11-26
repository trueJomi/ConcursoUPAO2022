"""
aadad

"""



def movimeintos(n):
    return (2**n)-1 # Formula que representa a la cantidad de movimeintos


def run():
    n= int(input())
    print(movimeintos(n))


if __name__ == "__main__":
    run()