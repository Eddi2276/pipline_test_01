from math import pi

def kreis_flache(r):
    return pi*(r**2)

# test function

radii =[2, 0, -3, 2 + 5j]
message = "Kreisflaeche von r = {radius} ist {flaeche}."

for r in radii:
    A = kreis_flache(r)
    print(message.format(radius =r,flaeche=A ))