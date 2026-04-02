# Goliat-Son: Aterrizador autónomo para cargas pesadas y tripulación

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.XXXXXXX.svg)](https://doi.org/10.5281/zenodo.XXXXXXX)
[![License](https://img.shields.io/badge/License-Proprietary-red.svg)](LICENSE)
[![EN](https://img.shields.io/badge/English-version-blue.svg)](./README.en.md)

En Marte, no hay pistas de aterrizaje, ni torres de control, ni infraestructura de apoyo. Cualquier misión tripulada necesita un vehículo que pueda descender con precisión, soportar temperaturas extremas y llevar todo lo necesario para establecer una base.

Goliat-Son nace para resolver ese problema.

## Que hace

Goliat-Son es un módulo de aterrizaje autónomo ajustable para cargas pesadas y tripulación. Diseñado para misiones autónomas de exploración y como Módulo de Carga y Transporte (MCT) de la nave Odiseo.

Características principales:
- Tripulación máxima: 6 personas.
- Capacidad de carga: 8,700 kg.
- Volumen útil: ~80 m³.
- Aterrizaje propulsivo vertical (VTOL).
- Acople compatible con IDSS (International Docking System Standard).

## Propulsión

| Modo | Combustible | Oxidante | Isp | Uso |
|------|-------------|----------|-----|-----|
| Principal | LH₂ | LOX | 450 s | Vacío (despegue, aterrizaje, ascenso) |
| Respaldo atmosférico | LH₂ | O₂ atmosférico | 380 s | Superficie marciana, ahorro de LOX |
| Modo superficie | LH₂ | O₂ de tanques o atmosférico | Variable | Operaciones en base |

En Marte, el O₂ atmosférico se produce con torres ShieldAir-Mars a partir del CO₂ (95% de la atmósfera). Goliat-Son puede reabastecer sus tanques de O₂ o usar turbinas que toman aire directamente.

## Sistema de aterrizaje VTOL

- Configuración de motores: 4 principales (120 kN cada uno) + 8 thrusters de control (2 kN cada uno).
- Delta-v desde órbita baja marciana: ~4.5 km/s (frenado aerodinámico + propulsivo).
- Control: guía autónoma con radar altimétrico, sensores láser y retropropulsión final.
- Tren de aterrizaje: 4 patas con amortiguadores hidráulicos, altura 8.5 m (desplegadas).

### Secuencia de aterrizaje

1. Separación: Goliat-Son se desacopla de Odiseo en órbita baja marciana (200 km).
2. Desorbitación: encendido de motores principales (30 s, 240 kN).
3. Entrada atmosférica: escudo térmico (hasta 2,500°C).
4. Paracaídas supersónico: despliegue a Mach 2.5 (10 km altitud), reduce velocidad a 100 m/s.
5. Aterrizaje propulsivo: motores principales al 30–70% de empuje.
6. Toque de suelo: thrusters + 2 motores principales al 20% para suavizar impacto.

## Carga útil detallada (primer vuelo)

| Categoría | Elemento | Peso (kg) |
|-----------|----------|-----------|
| Hábitat | Módulos inflables (2 unidades) | 1,500 |
| | Estructuras rígidas desplegables | 500 |
| | Esclusas y compuertas | 500 |
| Energía | Paneles solares plegables (50 kW) | 800 |
| | Baterías de litio | 500 |
| | Cableado y controladores | 200 |
| Producción de recursos | Torres ShieldAir (2 unidades) | 1,500 |
| | Electrolizadores | 200 |
| | Sistema Sabatier | 200 |
| | Tanques de almacenamiento (O₂, H₂O, CH₄) | 300 |
| Agua | Equipo de extracción de hielo | 200 |
| | Sistema de reciclaje | 200 |
| | Tanques de agua inicial | 100 |
| Alimentos | Raciones de respaldo (6 meses) | 600 |
| | Semillas y nutrientes para algas | 100 |
| | Sistema de cultivo hidropónico | 300 |
| Herramientas | Impresoras 3D (2 unidades) | 200 |
| | Kits de reparación | 200 |
| | Herramientas manuales | 100 |
| | Taladros y equipos de perforación | 100 |
| Vehículos | Rover presurizado (plegable) | 500 |
| | Drones de exploración (2) | 50 |
| Equipos científicos | Laboratorio portátil | 200 |
| | Sensores ambientales | 50 |
| | Muestreadores de suelo | 50 |
| Emergencias | Kit médico quirúrgico | 100 |
| | Botiquines y medicamentos | 50 |
| | Equipos de supervivencia | 50 |
| | Señales de emergencia | 20 |
| Otros | Repuestos y consumibles | 500 |
| **Total** | | **8,670 kg** |

## Uso en Odiseo

En la misión Odiseo a Marte, Goliat-Son:
- Transporta 6 personas + 8.7 toneladas de carga.
- Aterriza en superficie y despliega base marciana.
- Puede reabastecerse con combustible producido in situ y volver a órbita.

## Estado actual

- Concepto definido.
- Especificaciones técnicas completas.
- Simulaciones de aterrizaje (pendientes).
- Integración con Odiseo y ShieldAir-Mars documentada.

## Proyectos relacionados

- Odiseo — nave de infraestructura para colonizar Marte.
- ShieldAir-Mars — producción de oxígeno en Marte.
- Goliat-Orbital — reciclaje de basura espacial.

## Licencia

Copyright © 2026 Enrique Aguayo. Todos los derechos reservados.

Este proyecto está protegido por derechos de autor.

PERMITIDO:
- Uso no comercial con fines educativos o de investigación.
- Distribución sin modificación, siempre que se mantenga esta licencia y se dé crédito al autor.

PROHIBIDO sin autorización expresa por escrito:
- Uso comercial (incluyendo, pero no limitado a: ofrecerlo como servicio, SaaS, suscripción, integración en productos que generen ingresos, o cualquier uso que genere beneficio económico directo o indirecto).
- Modificación para entornos de producción.
- Distribución de versiones modificadas sin autorización.

Para licencias comerciales, soporte técnico, pilotos empresariales o consultas:
Contacto: eaguayo@migst.cl

Cualquier uso fuera de los términos permitidos requiere permiso previo del autor.

Las consultas comerciales son bienvenidas y se responderán en un plazo máximo de 7 días hábiles.

## Autor

Enrique Aguayo H.
Mackiber Labs
Contacto: eaguayo@migst.cl
ORCID: 0009-0004-4615-6825
GitHub: @enriqueherbertag-lgtm

Documentación asistida por Ana (DeepSeek), IA para investigación y optimización técnica.
