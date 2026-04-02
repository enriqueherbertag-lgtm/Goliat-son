# Goliat-Son: Autonomous lander for heavy cargo and crew

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.XXXXXXX.svg)](https://doi.org/10.5281/zenodo.XXXXXXX)
[![License](https://img.shields.io/badge/License-Proprietary-red.svg)](LICENSE)
[![ES](https://img.shields.io/badge/Spanish-version-green.svg)](./README.md)

On Mars, there are no runways, no control towers, no support infrastructure. Any crewed mission needs a vehicle that can descend precisely, withstand extreme temperatures, and carry everything needed to establish a base.

Goliat-Son was created to solve that problem.

## What it does

Goliat-Son is an autonomous adjustable lander for heavy cargo and crew. Designed for autonomous exploration missions and as a Cargo and Transport Module (MCT) for the Odiseo spacecraft.

Main features:
- Maximum crew: 6 people.
- Payload capacity: 8,700 kg.
- Usable volume: ~80 m³.
- Vertical propulsive landing (VTOL).
- IDSS-compatible docking.

## Propulsion

| Mode | Fuel | Oxidizer | Isp | Use |
|------|------|----------|-----|-----|
| Main | LH₂ | LOX | 450 s | Vacuum (takeoff, landing, ascent) |
| Atmospheric backup | LH₂ | Atmospheric O₂ | 380 s | Martian surface, saves LOX |
| Surface mode | LH₂ | Tank or atmospheric O₂ | Variable | Base operations |

On Mars, atmospheric O₂ is produced by ShieldAir-Mars towers from CO₂ (95% of the atmosphere). Goliat-Son can refill its O₂ tanks or use air-breathing turbines.

## VTOL landing system

- Engine configuration: 4 main (120 kN each) + 8 control thrusters (2 kN each).
- Delta-v from low Mars orbit: ~4.5 km/s (aerodynamic braking + propulsive).
- Control: autonomous guidance with radar altimeter, laser sensors, and final retropropulsion.
- Landing gear: 4 legs with hydraulic dampers, deployed height 8.5 m.

### Landing sequence

1. Separation: Goliat-Son undocks from Odiseo in low Mars orbit (200 km).
2. Deorbit burn: main engines ignite (30 s, 240 kN).
3. Atmospheric entry: heat shield withstands up to 2,500°C.
4. Supersonic parachute: deploys at Mach 2.5 (10 km altitude), reduces speed to 100 m/s.
5. Propulsive landing: main engines at 30–70% thrust.
6. Touchdown: thrusters + 2 main engines at 20% to soften impact.

## Detailed payload (first flight)

[Same table as in Spanish version]

## Use in Odiseo

In the Odiseo mission to Mars, Goliat-Son:
- Transports 6 people + 8.7 tons of cargo.
- Lands on the surface and deploys the Martian base.
- Can be refueled with in-situ produced fuel and return to orbit.

## Current status

- Concept defined.
- Technical specifications complete.
- Landing simulations (pending).
- Integration with Odiseo and ShieldAir-Mars documented.

## Related projects

- Odiseo — infrastructure spacecraft for colonizing Mars.
- ShieldAir-Mars — oxygen production on Mars.
- Goliat-Orbital — space debris recycling.

## License

Copyright © 2026 Enrique Aguayo. All rights reserved.

[Standard proprietary license text...]

## Author

Enrique Aguayo H.
Mackiber Labs
Contact: eaguayo@migst.cl
ORCID: 0009-0004-4615-6825
GitHub: @enriqueherbertag-lgtm

Documentation assisted by Ana (DeepSeek), AI for research and technical optimization.
