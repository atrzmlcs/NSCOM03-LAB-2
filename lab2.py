import numpy as np
import matplotlib.pyplot as plt

# wavelengths in nanometers (nm)
rainbow_wavelengths = {
    'Red': 665,
    'Orange': 630,
    'Yellow': 600,
    'Green': 550,
    'Blue': 470,
    'Indigo': 425,
    'Violet': 400
}

# speed of light in m/s
c = 3e8

# common sinusoidal variables to isolate frequency
A = 1            # amplitude
phi = 0          # phase
samples_per_cycle = 100 #time samples per cycle

t = np.linspace(0, 1.5e-14, 500)

waves = {}

# ROYGBIV Waves 
for color, wavelength in rainbow_wavelengths.items():
    f = c / (wavelength * 1e-9)
    sample_rate = int(samples_per_cycle * f)
    x = A * np.sin(2 * np.pi * f * t + phi)
    waves[color] = x
    
    plt.figure(figsize=(10, 3))
    plot_color = color.lower() if color != 'Indigo' else '#4b0082'
    
    plt.plot(t, x, color=plot_color, label=f'{wavelength} nm ({color})') 
    plt.title(f"Sinusoidal Wave - {color}")
    plt.xlabel("Time (s)")
    plt.ylabel("Amplitude")
    plt.grid(True)
    plt.legend()
    
    # Save the individual color wave
    plt.savefig(f'{color}_Wave.png', bbox_inches='tight')
    plt.close() 


plt.close()