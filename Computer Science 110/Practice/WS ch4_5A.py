def f2c(fahr):
    Celsius_degrees = (fahr-32)/1.8
    return Celsius_degrees
    
def f2k(fahr):
    Kelvin_degrees = f2c(fahr)+273.15
    return Kelvin_degrees

print(f2k(212))
