def mnozenie(a, b):
    try:
        print(int(a) * int(b))
    except ValueError:
        print("Bład Wartosci")
    except TypeError:
        print("Bład typu")
    except Exception as e:
        print("Inny bład", e)
    else:
        print("poszła")
    finally:
        print("zawsze")


def dzielenie(a, b):
    try:
        print(int(a) / int(b))
    except ValueError:
        print("Bład Wartosci")
    except TypeError:
        print("Bład typu")
    except ZeroDivisionError:
        print("Nie dziel przez zero")
    except Exception as e:
        print("Inny bład", e)
    else:
        print("poszła")
    finally:
        print("zawsze")


mnozenie(2, 3)
mnozenie(2, "3")
mnozenie("a", "3")
mnozenie("2", "3")
mnozenie((2,), "3")
print("Program działą dalej")
dzielenie(2, 0)
raise ValueError