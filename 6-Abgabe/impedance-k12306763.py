"""
Dateiname: impedance-k12306763
Erstellungsdatum: 07.02.2024
Name: Christos Stamou
Matrikelnummer: k12306763
Beschreibung: 

Der Python-Code enthält eine Klasse namens impedance, die komplexe Impedanzen repräsentiert. Die Klasse ermöglicht die Erstellung von Impedanzen basierend auf der Kreisfrequenz 
ω und unterstützt die Überladung der + und // Operatoren für die Serien- bzw. Parallelschaltung von Impedanzen. Die bode-Methode erstellt Bode-Diagramme für den Frequenzgang von Impedanzen.
Im Hauptprogramm werden variable Bauteilwerte (Widerstände, Kapazitäten) definiert, Impedanzen für eine Schaltung erstellt und der Frequenzgang durch Bode-Plots visualisiert. 
Der Code bietet eine flexible Möglichkeit, Schaltungen zu modellieren und ihre Antwort auf unterschiedliche Frequenzen zu analysieren.    
"""

import numpy as np
import matplotlib.pyplot as plt

class impedance:
    def __init__(self, value, unit, omega):
        self.omega = omega
        self.value = value
        self.unit = unit

        if unit == 'O':
            self.impedance_values = value * np.ones_like(omega)
        elif unit == 'F':
            self.impedance_values = 1j / (omega * value)
        elif unit == 'H':
            self.impedance_values = 1j * omega * value

    def __add__(self, other):
        result = impedance(0, 'O', self.omega)
        result.impedance_values = self.impedance_values + other.impedance_values
        return result

    def __floordiv__(self, other):
        result = impedance(0, 'O', self.omega)
        result.impedance_values = 1 / (1 / self.impedance_values + 1 / other.impedance_values)
        return result

    def bode(self, other_Z):
        total_impedance = self + other_Z

        magnitude = np.abs(total_impedance.impedance_values)
        phase = np.angle(total_impedance.impedance_values, deg=True)

        plt.figure(figsize=(10, 6))

        plt.subplot(2, 1, 1)
        plt.semilogx(self.omega, 20 * np.log10(magnitude))
        plt.title('Bode Plot - Magnitude')
        plt.xlabel('Frequency (rad/s)')
        plt.ylabel('Magnitude (dB)')
        plt.grid(True)

        plt.subplot(2, 1, 2)
        plt.semilogx(self.omega, phase)
        plt.title('Bode Plot - Phase')
        plt.xlabel('Frequency (rad/s)')
        plt.ylabel('Phase (degrees)')
        plt.grid(True)

        plt.tight_layout()
        plt.show()

# Bauteilwerte variabel gestalten
R1_value = 1000
C1_value = 1e-4
R2_value = 10
C2_value = 1e-5
C3_value = 5e-4

# Frequenzen definieren
omega = np.logspace(-3, 9, 100)

# Impedanzen erstellen
R1 = impedance(R1_value, 'O', omega)
C1 = impedance(C1_value, 'F', omega)
R2 = impedance(R2_value, 'O', omega)
C2 = impedance(C2_value, 'F', omega)
C3 = impedance(C3_value, 'F', omega)

# Schaltung aufbauen
Z_1 = (R1 // C1) + R2
Z_2 = (C2 // R2) + C3

# Bode-Plot erstellen
Z_2.bode(Z_1)
