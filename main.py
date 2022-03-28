from functions import top_retweet

def main():
    print("""
        0. Salir
        1. Los top 10 tweets más retweeted.
        2. Los top 10 usuarios en función a la cantidad de tweets que emitieron.
        3. Los top 10 días donde hay más tweets.
        4. Top 10 hashtags más usados.
        """)
    opcion = input("Escoja una opción: ")
    try:
        if int(opcion) == 0:
            return True
        elif int(opcion) == 1:
            respuesta = top_retweet()
            print("Los top 10 tweets más retweeted son:")
            for i in range(len(respuesta)):
                print(f"{i + 1}. {respuesta[i]['url']}")
        elif int(opcion) == 2:
            pass
        elif int(opcion) == 3:
            pass 
        elif int(opcion) == 4:
            pass 
        else:
            print("Input no válido")
    except ValueError as error:
        print(f"{error} no es convertible a int")

if __name__ == "__main__":
    while not main():
        pass