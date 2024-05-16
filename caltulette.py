nombreUn= int(input("Entrer le nombre un"))
nombreDeux=int(input("Entre le nombre deux"))
symbole=input("Entrer un signe")
reponse=nombreUn+nombreDeux
match symbole:
    case "+":
        reponse=nombreUn+nombreDeux
        print(reponse)
    case "-":
        reponse=nombreUn-nombreDeux
        print(reponse)
    case "/":
        reponse=nombreUn/nombreDeux
        print(reponse)
    case "*":
        reponse=nombreun*nombreDeux
        print(reponse)
    case _:
        print("Singe non reconu")