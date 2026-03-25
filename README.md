# Goliat-Son

**Aterrizador autónomo ajustable para cargas pesadas y tripulación.**

Goliat-Son es un módulo de aterrizaje diseñado para ser utilizado en múltiples contextos: desde misiones autónomas de exploración hasta como **Módulo de Carga y Transporte (MCT)** de la nave **Odiseo**.

## Propulsión

| Modo | Combustible | Oxidante | Isp | Uso |
|------|-------------|----------|-----|-----|
| Principal | LH₂ | LOX | 450 s | Vacío (despegue, aterrizaje, ascenso) |
| Respaldo atmosférico | LH₂ | O₂ atmosférico | 380 s | Superficie marciana, ahorro de LOX |
| Modo superficie | LH₂ | O₂ de tanques o atmosférico | Variable | Operaciones en base |

**Ventaja:** En Marte, el O₂ atmosférico se produce con torres **ShieldAir** a partir del CO₂ (95% de la atmósfera). Goliat-Son puede reabastecer sus tanques de O₂ o usar turbinas que toman aire directamente.

## Especificaciones

| Parámetro | Valor |
|-----------|-------|
| Tripulación máxima | 6 personas |
| Capacidad de carga | 8,700 kg |
| Volumen útil | ~80 m³ |
| Aterrizaje | Propulsivo vertical (VTOL) |
| Acople | IDSS compatible |
| Autonomía en superficie | 30 días (modo base), indefinida con recursos externos |

## Uso en Odiseo

En la misión Odiseo a Marte, Goliat-Son:
- Transporta 6 personas + 8.7 toneladas de carga.
- Aterriza en superficie, despliega base marciana.
- Puede reabastecerse con combustible producido in situ y volver a órbita.

🔗 [Ver arquitectura completa de Odiseo](https://github.com/enriqueherbertag-lgtm/Odiseo)

## Licencia

Apache 2.0 con restricción de uso comercial.

## Autor

**Enrique Aguayo H.**  
Investigador independiente, Mackiber Labs  
Contacto: eaguayo@migst.cl  
ORCID: 0009-0004-4615-6825  
GitHub: [@enriqueherbertag-lgtm](https://github.com/enriqueherbertag-lgtm)
