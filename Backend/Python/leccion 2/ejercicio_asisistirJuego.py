from doctest import FAIL_FAST
from re import T


vacaciones = False
diaDescanso = False

if not (vacaciones or diaDescanso):
    print("No puede asistir al juego")
else:
    print("Puede asistir al juego")