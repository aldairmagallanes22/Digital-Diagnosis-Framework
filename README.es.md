## Proyecto de Inteligencia Comercial: Framework de diagnóstico de digitalización

[Demo de la calculadora](https://imgur.com/a/UrIWCv1) 

[Demo en Vivo](https://digital-diagnosis-framework-grz59zhqhkpgakwf923gja.streamlit.app/)


### Problema

Las micro, pequeñas y medianas empresas (mipymes) representan el 95.5% del total de empresas en México (INEGI, 2024). Actualmente, el 70% de las empresas ya inició un proceso de digitalización. Sin embargo, tanto las empresas que han iniciado este proceso como las que no, comparten el mismo obstáculo: la falta de habilidad en el capital humano para el manejo de las tecnologías. Y esto no solo sucede en México, esto se repite en varios países de Latinoamérica: en Colombia, 35% de las compañías enfrenta este problema, combinado con resistencia cultural en un 45%, y en Chile, 65% de las empresas reconoce que su personal no cuenta con la preparación digital adecuada (NIC México, 2025).

En otras palabras, las mipymes en Lationamérica y, sobre todo en México, tiene problemas para iniciar el proceso de digitalización porque los trabajadores no saben cómo utilizar la tecnología para mejorar su trabajo. Por otro lado, debemos entender que las empresas tienen parte de culpa por no hacer enfasis en la capacitación de sus trabajadores si el proceso de digitalización es algo que se consideró llevar a cabo después de un análisis exhaustivo.



______________________________________________________________________________________



## Solución

Este proyecto nace a partir de está indecisión y barreras que impiden la digitalización de las mipymes en México, y que se puede adaptar a cualquier entorno y empresa de cualquier país haciendo ajustes en cuestiones legales y de costos.

El proyecto es una calculadora que diagnostica si tu PYME/emprendimiento necesita digitalizarse calculando el ROI de tres disparadores principales.
Pero más que ser una simple calculadora, busca ser la base para un proceso de consultoría el cual sirva para dar soporte a la toma de decisiones con respecto a los diferentes sectores del proyecto que se busca digitalizar como lo puede ser desde saber si es rentable contratar la membresía de ChatGPT para analizar informes y datos, hasta saber si es rentanble contratar un sistema POS y cambiar el modelo de negocio por completo.

Actualmente el proyecto solo considera datos y condiciones dadas en empresas del sector Retail.

Principales disparadores:
    
- Disparador de eficiencia: calcula el costo de hacer las tareas de manera manual y el costo de contratar un software (en este caso un sistema POS).

- Disparador de riesgo: calcula el costo del software y la multa por pagar en caso de cometer un error al generar CFDIs, teniendo en cuenta la probabilidad de error.

- Disparador de oportunidad: calcula la ganancia que el negocio tiene sin implementar pagos con tarjeta y la ganancia que puede recuperar si se digitaliza e implementa este método de pago, con su respectiva comisión por pago con tarjeta y el aumento de ventas por la implementación del método mencionado. 



______________________________________________________________________________________

## Tecnología usada

Python
* Pandas (para el manejo de los benchmarks)
* Streamlit (para la creación de la app web interactiva)

______________________________________________________________________________________

## Ejecutar este Proyecto Localmente

1.  Clona el repositorio:
    `git clone https://github.com/aidairmagallanez22/Digital-Diagnosis-Framework.git`
2.  Navega a la carpeta:
    `cd Digital-Diagnosis-Framework`
3.  Instala las dependencias:
    `pip install -r requirements.txt`
4.  Ejecuta la app:
    `streamlit run app.py`


______________________________________________________________________________________
## Próximos pasos

- Añadir los módulos de Restaurantes y Servicios.
- Desarrollar y pulir los cálculos para obtener un mejor resultado.
- Desarrollar y mejorar la interfaz temporal hecha con Streamlit.



