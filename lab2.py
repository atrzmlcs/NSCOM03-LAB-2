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

# ROYGBIV frequency waves 
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

# --- Section 8: Composite Signals (Zoomed In / Decreased Cycles) ---

# Define a shorter time window specifically for composite waves to decrease cycles
# (0.4e-14 seconds instead of 1.5e-14)
t_comp = np.linspace(0, 0.4e-14, 500)

# Re-calculate composite waves using the shorter time window
waves_comp = {}
for color, wavelength in rainbow_wavelengths.items():
    f = c / (wavelength * 1e-9)
    waves_comp[color] = A * np.sin(2 * np.pi * f * t_comp + phi)

# 1. Combine 3 waveforms (RGB)
composite_rgb = waves_comp['Red'] + waves_comp['Green'] + waves_comp['Blue']

plt.figure(figsize=(10, 3))
plt.plot(t_comp, composite_rgb, color='black', label='Red + Green + Blue')
plt.title("Composite Signal - RGB (Decreased Cycles)")
plt.xlabel("Time (s)")
plt.ylabel("Amplitude")
plt.grid(True)
plt.legend()
plt.savefig('Composite_RGB.png', bbox_inches='tight')
plt.close()

# 2. Combine all 7 waveforms (Full Spectrum)
composite_all = sum(waves_comp.values())

plt.figure(figsize=(10, 3))
plt.plot(t_comp, composite_all, color='darkmagenta', label='All 7 Colors Combined')
plt.title("Composite Signal - Full Spectrum (Decreased Cycles)")
plt.xlabel("Time (s)")
plt.ylabel("Amplitude")
plt.grid(True)
plt.legend()
plt.savefig('Composite_Full.png', bbox_inches='tight')
plt.close()

# --- Section 9: Light Spectrum (Frequency Domain) ---
N = len(t_comp)          
dt = t_comp[1] - t_comp[0]    
yf = np.fft.fft(composite_all)
xf = np.fft.fftfreq(N, dt)[:N//2]

plt.figure(figsize=(10, 3))
plt.plot(xf, 2.0/N * np.abs(yf[0:N//2]), color='purple')
plt.title("Frequency Domain - Light Spectrum")
plt.xlabel("Frequency (Hz)")
plt.ylabel("Magnitude")
plt.xlim(3.5e14, 8.5e14)
plt.grid(True)
plt.savefig('Light_Spectrum.png', bbox_inches='tight')
plt.close()

plt.close()