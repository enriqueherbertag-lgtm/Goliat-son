# Goliat-Son

[![License: CC BY-NC 4.0](https://img.shields.io/badge/License-CC_BY--NC_4.0-lightgrey.svg)](https://creativecommons.org/licenses/by-nc/4.0/)

**Aterrizador autónomo ajustable para cargas pesadas y tripulación.**

Goliat-Son es un módulo de aterrizaje diseñado para ser utilizado en múltiples contextos: desde misiones autónomas de exploración hasta como **Módulo de Carga y Transporte (MCT)** de la nave **Odiseo**.

## Propulsión

| Modo | Combustible | Oxidante | Isp | Uso |
|------|-------------|----------|-----|-----|
| Principal | LH₂ | LOX | 450 s | Vacío (despegue, aterrizaje, ascenso) |
| Respaldo atmosférico | LH₂ | O₂ atmosférico | 380 s | Superficie marciana, ahorro de LOX |
| Modo superficie | LH₂ | O₂ de tanques o atmosférico | Variable | Operaciones en base |

**Ventaja:** En Marte, el O₂ atmosférico se produce con torres **[ShieldAir-Mars](https://github.com/enriqueherbertag-lgtm/ShieldAir-Mars)** a partir del CO₂ (95% de la atmósfera). Goliat-Son puede reabastecer sus tanques de O₂ o usar turbinas que toman aire directamente.

## Especificaciones

| Parámetro | Valor |
|-----------|-------|
| Tripulación máxima | 6 personas |
| Capacidad de carga | 8,700 kg |
| Volumen útil | ~80 m³ |
| Aterrizaje | Propulsivo vertical (VTOL) |
| Acople | IDSS compatible |
| Autonomía en superficie | 30 días (modo base), indefinida con recursos externos |

## Sistema de aterrizaje VTOL

| Parámetro | Valor |
|-----------|-------|
| Configuración de motores | 4 principales (120 kN cada uno) + 8 thrusters de control (2 kN cada uno) |
| Delta-v desde órbita baja marciana | ~4.5 km/s (incluye frenado aerodinámico + propulsivo) |
| Sistema de control | Guía autónoma con radar altimétrico, sensores láser y retropropulsión final |
| Tren de aterrizaje | 4 patas con amortiguadores hidráulicos, altura 8.5 m (desplegadas) |

### Secuencia de aterrizaje

1. **Separación:** Goliat-Son se desacopla de Odiseo en órbita baja marciana (200 km)
2. **Desorbitación:** Encendido de motores principales (30 s, 240 kN) para reducir velocidad
3. **Entrada atmosférica:** Escudo térmico protege durante frenado aerodinámico (hasta 2,500°C)
4. **Paracaídas supersónico:** Despliegue a Mach 2.5 (10 km altitud), reduce velocidad a 100 m/s
5. **Aterrizaje propulsivo:** Motores principales al 30–70% de empuje para descenso final y toque de suelo
6. **Toque de suelo:** Thrusters + 2 motores principales al 20% para suavizar impacto

## Carga útil detallada (primer vuelo)

| Categoría | Elemento | Peso (kg) |
|-----------|---------|-----------|
| **Hábitat** | Módulos inflables (2 unidades) | 1,500 |
| | Estructuras rígidas desplegables | 500 |
| | Esclusas y compuertas | 500 |
| **Energía** | Paneles solares plegables (50 kW) | 800 |
| | Baterías de litio | 500 |
| | Cableado y controladores | 200 |
| **Producción de recursos** | Torres ShieldAir (versión Marte, 2 unidades) | 1,500 |
| | Electrolizadores | 200 |
| | Sistema Sabatier | 200 |
| | Tanques de almacenamiento (O₂, H₂O, CH₄) | 300 |
| **Agua** | Equipo de extracción de hielo | 200 |
| | Sistema de reciclaje | 200 |
| | Tanques de agua inicial | 100 |
| **Alimentos** | Raciones de respaldo (6 meses) | 600 |
| | Semillas y nutrientes para algas | 100 |
| | Sistema de cultivo hidropónico | 300 |
| **Herramientas** | Impresoras 3D (2 unidades) | 200 |
| | Kits de reparación | 200 |
| | Herramientas manuales | 100 |
| | Taladros y equipos de perforación | 100 |
| **Vehículos** | Rover presurizado (plegable) | 500 |
| | Drones de exploración (2) | 50 |
| **Equipos científicos** | Laboratorio portátil | 200 |
| | Sensores ambientales | 50 |
| | Muestreadores de suelo | 50 |
| **Emergencias** | Kit médico quirúrgico | 100 |
| | Botiquines y medicamentos | 50 |
| | Equipos de supervivencia | 50 |
| | Señales de emergencia | 20 |
| **Otros** | Repuestos y consumibles | 500 |
| **Total** | | **8,670 kg** |

## Uso en Odiseo

En la misión Odiseo a Marte, Goliat-Son:
- Transporta 6 personas + 8.7 toneladas de carga.
- Aterriza en superficie, despliega base marciana.
- Puede reabastecerse con combustible producido in situ y volver a órbita.

🔗 [Ver arquitectura completa de Odiseo](https://github.com/enriqueherbertag-lgtm/Odiseo)

## Autor

**Enrique Aguayo H.**  
Investigador independiente, Mackiber Labs  
Contacto: eaguayo@migst.cl  
ORCID: 0009-0004-4615-6825  
GitHub: [@enriqueherbertag-lgtm](https://github.com/enriqueherbertag-lgtm)
