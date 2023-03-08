def liczby(c, *cyfry):
    suma = c
    count = len(cyfry)
    print(suma)
    print(count)
    print(type(cyfry))
    for i in cyfry:
        suma += i
    print(f"Suma {suma}, średnia {suma / count}")


liczby(1, 5, 4, 6, 78, 90, 67, 89, 0, 89, 11, 222, 33, 44456767, 886, 8, 69, 679, 9, 6)


def connect(**opcje):
    print(opcje)
    connect_param = {
        'host': '127.0.0.7',
        'port': '8080'
    }
    connect_param['pwd'] = opcje
    print(connect_param)


connect(user='/home')
connect(root='/')
connect(root="/", user="/home")


def allparams(a, b, /, c=42, *args, d=256, e, **kwargs):  # / - odziela pozycyjne argumenty od argumentów z nazwa
    print('d,e', d, e)
    print('args', args)
    print('kwargs', kwargs)


allparams(1, 2,1, 2, 3, 4, 5, 6, 7, 8, 9, d=7, e=6, f=14, g=45)
