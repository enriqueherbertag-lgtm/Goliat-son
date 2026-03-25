# Simulación de Aterrizaje - Goliat-Son

Este script simula el perfil de descenso de Goliat-Son desde la órbita baja marciana hasta la superficie.

## Parámetros considerados

- **Atmósfera marciana:** Modelo exponencial (rho_0 = 0.020 kg/m³, H = 11.1 km)
- **Fases:** Desorbitación → frenado aerodinámico → paracaídas → aterrizaje propulsivo → toque de suelo
- **Control de empuje:** Ajuste dinámico basado en velocidad y altitud

## Cómo ejecutar

```bash
# Instalar dependencias
pip install numpy matplotlib

# Ejecutar simulación
python3 landing-simulation.py
