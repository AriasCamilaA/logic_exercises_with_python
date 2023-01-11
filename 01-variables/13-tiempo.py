# Solicitar tiempo en segundos y transformar a horas y minutos
seg = int(input("Ingrese los segundos: "))

min = seg//60
hor = int(min//60)
min -= int(hor*60)
seg_f = seg - hor*3600 - min*60

print(f"{seg} equivalen a {hor} hh: {min} mm: {seg_f} ss")