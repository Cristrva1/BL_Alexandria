# three.js

Generado: 2026-06-25T05:01:02.236908+00:00

## Decision

REFERENCIA

## Para que sirve realmente

motor 3D (WebGL) para renderizar gráficos y escenas interactivas directamente en el navegador.

## Que problema resuelve

renderizas 3D en web

## Por que tiene valor

Aporta valor en `library` para ui, browser, animation, dataviz. Stack declarado: JavaScript/WebGL.

## Cuando usarlo

renderizas 3D en web

## Cuando NO usarlo

trabajas solo 2D.

## Tipo de instalacion

reference_only

## Stack / tecnologia detectada

JavaScript/WebGL

## Instalacion detectada

Repo local detectado: si

## Con que se combina

- `react-three-fiber`
- `gsap`

## Contra que compite

- Ninguno declarado.

## Riesgos

Riesgo bajo o medio; validar solo cuando sea necesario para una decision concreta.

## Ideas profesionales

Combinar con react-three-fiber, gsap cuando el flujo necesite mas de una pieza.

## Veredicto

Veredicto: referencia. Tiene sentido si renderizas 3D en web. No debe instalarse por inercia.
