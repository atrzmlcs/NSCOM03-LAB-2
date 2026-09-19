import numpy as np
import matplotlib.pyplot as plt

# Wavelengths in nanometers (nm) based on the laboratory diagram
rainbow_wavelengths = {
    'Red': 665,
    'Orange': 630,
    'Yellow': 600,
    'Green': 550,
    'Blue': 470,
    'Indigo': 425,
    'Violet': 400
}

# Speed of light in m/s
c = 3e8

# 1. Define common sinusoidal variables
A = 1            # Amplitude
phi = 0          # Phase
samples_per_cycle = 100

# 3. Generate time array 
# Reduced the max time from 5e-14 to 1.5e-14 to show fewer cycles (spacing them out)
t = np.linspace(0, 1.5e-14, 500)

# Dictionary to store the wave data for Section 8 (Composite Signals)
waves = {}

# Loop through each color to calculate, generate, and plot
for color, wavelength in rainbow_wavelengths.items():
    # Convert wavelength to meters and calculate frequency
    f = c / (wavelength * 1e-9)
    
    # 2. Calculate sample rate for a smooth continuous wave
    sample_rate = int(samples_per_cycle * f)
    
    # 4. Generate the sinusoidal wave: x(t) = A * sin(2πft + φ)
    x = A * np.sin(2 * np.pi * f * t + phi)
    
    # Store the wave data for later composite use
    waves[color] = x
    
    # 5. Plot the individual wave
    # Added figsize=(10, 3) to make the graph wider and less tall
    plt.figure(figsize=(10, 3))
    
    # Handle Indigo's hex color since it's not a default matplotlib named color
    plot_color = color.lower() if color != 'Indigo' else '#4b0082'
    
    plt.plot(t, x, color=plot_color, label=f'{wavelength} nm ({color})') 
    plt.title(f"Sinusoidal Wave - {color}")
    plt.xlabel("Time (s)")
    plt.ylabel("Amplitude")
    plt.grid(True)
    plt.legend()

# --- Section 8: Composite Signals ---

# Combine 3 waveforms (Red, Green, Blue)
composite_rgb = waves['Red'] + waves['Green'] + waves['Blue']

plt.figure(figsize=(10, 3))
plt.plot(t, composite_rgb, color='black', label='Red + Green + Blue')
plt.title("Composite Signal - RGB")
plt.xlabel("Time (s)")
plt.ylabel("Amplitude")
plt.grid(True)
plt.legend()

# Combine all 7 waveforms (ROYGBIV)
# sum(waves.values()) mathematically adds all arrays in the dictionary together
composite_all = sum(waves.values())

plt.figure(figsize=(10, 3))
plt.plot(t, composite_all, color='gray', label='All ROYGBIV Combined')
plt.title("Composite Signal - Full Spectrum")
plt.xlabel("Time (s)")
plt.ylabel("Amplitude")
plt.grid(True)
plt.legend()

# --- Section 9: Frequency-Domain Plotting (Light Spectrum) ---

# Perform Fast Fourier Transform (FFT) on the full composite signal
N = len(t)          # Number of sample points
dt = t[1] - t[0]    # Sample spacing
yf = np.fft.fft(composite_all)
xf = np.fft.fftfreq(N, dt)[:N//2]

plt.figure(figsize=(10, 3))
# Plot the magnitude of the positive frequencies
plt.plot(xf, 2.0/N * np.abs(yf[0:N//2]), color='purple')
plt.title("Frequency Domain - Light Spectrum")
plt.xlabel("Frequency (Hz)")
plt.ylabel("Magnitude")

# Limit the X-axis to focus strictly on the visible light range (approx. 4e14 to 8e14 Hz)
plt.xlim(3.5e14, 8.5e14)
plt.grid(True)

# Display all new plots
plt.show()