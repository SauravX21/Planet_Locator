# Planet Locator

**Planet Locator** is a Python project that allows users to select any planet in the solar system and view its real-time position in the sky from Earth. It displays:

- Right Ascension (RA)
- Declination (Dec)
- Distance from Earth (in astronomical units)
- A simple 2D sky plot of Earth and the selected planet

It uses the [Skyfield](https://rhodesmill.org/skyfield/) library to access high-precision planetary data from NASA's JPL ephemeris files.

---

## Features

- Real-time planet selection (Mercury to Neptune)
- Calculates RA, Dec, and distance
- Plots Earth and planet positions
- Lightweight and easy to use

---

## Installation

Install the required libraries:

```bash
pip install -r requirements.txt
