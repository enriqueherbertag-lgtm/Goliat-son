"""
Simulación de aterrizaje de Goliat-Son en Marte
Modelo 1D (altitud vs tiempo) con frenado aerodinámico, paracaídas y propulsivo
"""

import numpy as np
import matplotlib.pyplot as plt

# ============================================================================
# PARÁMETROS DE MARTE
# ============================================================================
g_mars = 3.71  # m/s²
rho_0 = 0.020  # kg/m³ (densidad atmosférica a nivel del mar)
H = 11.1  # km (altitud de escala)

# ============================================================================
# PARÁMETROS DE GOLIAT-SON
# ============================================================================
m_dry = 5300      # kg (estructura seca)
m_prop = 6000     # kg (propelente)
m_cargo = 8700    # kg (carga útil)
m_total = m_dry + m_prop + m_cargo  # 20,000 kg

# Áreas de referencia
A_aero = 16       # m² (área transversal para frenado aerodinámico)
Cd_aero = 1.2     # coeficiente de arrastre (cápsula)
A_chute = 100     # m² (área del paracaídas)
Cd_chute = 1.5    # coeficiente de arrastre (paracaídas)

# Parámetros de propulsión
thrust_max = 4 * 105000   # N (4 motores a nivel mar marciano)
thrust_min = 2 * 2000     # N (thrusters de control)

# ============================================================================
# PARÁMETROS DE LA SIMULACIÓN
# ============================================================================
dt = 0.1           # s
t_max = 600        # s
altitude_initial = 200000   # m (200 km)
velocity_initial = -3500    # m/s (negativo hacia abajo)

# ============================================================================
# SIMULACIÓN
# ============================================================================
phase = "desorbitacion"  # desorbitacion, aero, parachute, propulsive, touchdown
t = 0
altitude = altitude_initial
velocity = velocity_initial
acceleration = 0

# Arrays para guardar datos
time = []
alt = []
vel = []
acc = []
thrust_history = []

print("Simulando aterrizaje...")
while altitude > 0 and t < t_max:
    # Densidad atmosférica en función de altitud
    if altitude > 0:
        rho = rho_0 * np.exp(-altitude / 1000 / H)
    else:
        rho = rho_0
    
    # Cambio de fases basado en altitud
    if altitude > 100000:
        phase = "desorbitacion"
    elif altitude > 10000:
        phase = "aero"
    elif altitude > 2000:
        phase = "parachute"
    elif altitude > 10:
        phase = "propulsive"
    else:
        phase = "touchdown"
    
    # Calcular aceleración
    gravity = -g_mars
    
    # Arrastre aerodinámico
    if phase == "aero" or phase == "parachute":
        if phase == "aero":
            A = A_aero
            Cd = Cd_aero
        else:  # parachute
            A = A_chute
            Cd = Cd_chute
        drag = 0.5 * rho * velocity**2 * Cd * A / m_total
        drag = drag * np.sign(velocity) if velocity != 0 else 0
    else:
        drag = 0
    
    # Empuje
    if phase == "propulsive":
        # Control de empuje para aterrizaje suave
        # Aumenta empuje cuando velocidad o altitud son altas
        thrust = thrust_max * min(1.0, max(0.1, (abs(velocity) + altitude/1000) / 200))
    elif phase == "touchdown":
        thrust = thrust_min * 2  # pequeños thrusters para toque suave
    else:
        thrust = 0
    
    if thrust > thrust_max:
        thrust = thrust_max
    
    # Aceleración total
    acceleration = gravity + drag + thrust / m_total
    thrust_history.append(thrust)
    
    # Actualizar velocidad y altitud
    velocity += acceleration * dt
    altitude += velocity * dt
    
    # Guardar datos
    time.append(t)
    alt.append(altitude)
    vel.append(velocity)
    acc.append(acceleration)
    
    t += dt

# ============================================================================
# RESULTADOS
# ============================================================================
print(f"\n=== RESULTADOS DE LA SIMULACIÓN ===")
print(f"Tiempo total de aterrizaje: {t:.1f} s")
print(f"Velocidad de impacto: {abs(velocity):.2f} m/s")
if abs(velocity) < 5:
    print("✅ Aterrizaje exitoso (velocidad < 5 m/s)")
else:
    print("⚠️ Aterrizaje duro (velocidad > 5 m/s)")

# ============================================================================
# GRÁFICOS
# ============================================================================
fig, axes = plt.subplots(2, 2, figsize=(12, 8))

# Altitud
axes[0, 0].plot(time, np.array(alt)/1000)
axes[0, 0].set_ylabel('Altitud (km)')
axes[0, 0].set_xlabel('Tiempo (s)')
axes[0, 0].grid(True)
axes[0, 0].set_title('Altitud vs Tiempo')

# Velocidad
axes[0, 1].plot(time, np.abs(vel))
axes[0, 1].set_ylabel('Velocidad (m/s)')
axes[0, 1].set_xlabel('Tiempo (s)')
axes[0, 1].grid(True)
axes[0, 1].set_title('Velocidad vs Tiempo')

# Aceleración
axes[1, 0].plot(time, acc)
axes[1, 0].set_ylabel('Aceleración (m/s²)')
axes[1, 0].set_xlabel('Tiempo (s)')
axes[1, 0].grid(True)
axes[1, 0].set_title('Aceleración vs Tiempo')

# Empuje
axes[1, 1].plot(time, np.array(thrust_history)/1000)
axes[1, 1].set_ylabel('Empuje (kN)')
axes[1, 1].set_xlabel('Tiempo (s)')
axes[1, 1].grid(True)
axes[1, 1].set_title('Empuje vs Tiempo')

plt.suptitle('Simulación de Aterrizaje - Goliat-Son en Marte')
plt.tight_layout()
plt.savefig('landing_profile.png', dpi=150)
print("\n✅ Gráfico guardado como landing_profile.png")
plt.show()
