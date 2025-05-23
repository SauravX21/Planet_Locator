from skyfield.api import load
import matplotlib.pylab as plt

planets = {
    "mercury": 1,
    "venus": 2,
    "mars": 4,
    "jupiter": 5,
    "saturn": 6,
    "uranus": 7,
    "neptune": 8,
}
planet_data = load("de421.bsp")

earth = planet_data[3]
t = load.timescale().now()

planet_name = str(input("Enter the planet name:-")).lower()
for key in planets:
    if key in planet_name:
        planet_id = planet_data[planets[key]]
        planet_posi = earth.at(t).observe(planet_id)
        ra, dec, distance = planet_posi.radec()
        plt.scatter(0, 0, color="blue")
        plt.text(0, 0, "Earth", color="blue")
        plt.scatter(ra.hours * 15, dec.degrees, color="red")
        plt.text(ra.hours * 15, dec.degrees, key.capitalize(), color="red")
        plt.title(f"Position of planet {key.capitalize()} with respect to Earth")
        plt.xlabel("Right ascension in degrees")
        plt.ylabel("Declination in degrees")
        plt.show()
    
