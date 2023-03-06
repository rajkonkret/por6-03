lista = []
lang = input("Wpisz znany Ci jezyk programowania")
a = "ab"
match lang.lower():
    case "python":
        lista.append(lang)
    case "java":
        lista.append(lang)
    case "c++":
        match a:
            case "ab":
                lista.append("ab")
        lista.append(lang)
    case _:
        print("nie mam takiego jezyka")
print(lista)
