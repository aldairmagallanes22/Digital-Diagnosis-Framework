import streamlit as st
import pandas as pd


def cargar_benchmarks():
    data = {
        'Sector': ['Retail'],
        'Tarea_Clave_Manual': ['Inventario y Cobro'],
        'Solucion_Digital_Recomendada': ['Software de Punto de Venta (POS)'],
        'Costo_Mensual_Software_MXN': [500], # Costo mensual del software
        'Riesgo_Clave': ['Error de Facturación (SAT)'],
        'Costo_Riesgo_MXN': [19700], # Multa mínima del SAT
        'Oportunidad_Clave': ['Aceptar Pagos Digitales'],
        'KPI_Oportunidad_Comision': [0.035], # 3.5% de comisión
        'KPI_Oportunidad_Aumento_Ticket': [0.20] # 20% de aumento en ticket
    }
    df_benchmarks = pd.DataFrame(data)
    return df_benchmarks

# FASE 2

# FUNCIÓN 1: DISPARADOR DE EFICIENCIA
def calcular_roi_eficiencia(horas_manuales, salario_admin, costo_software_mensual):
    costo_hora_hombre = salario_admin / 160
    costo_anual_manual = (horas_manuales * 52) * costo_hora_hombre
    costo_anual_software = costo_software_mensual * 12
    ahorro_anual = costo_anual_manual - costo_anual_software
    return ahorro_anual, costo_anual_manual, costo_anual_software

# FUNCIÓN 2: DISPARADOR DE RIESGO
def calcular_roi_riesgo(costo_multa_sat, costo_software_mensual, prob_error):
    riesgo_anualizado = costo_multa_sat * prob_error
    costo_anual_software = costo_software_mensual * 12
    ahorro_anual_riesgo = riesgo_anualizado - costo_anual_software
    return ahorro_anual_riesgo, riesgo_anualizado

# FUNCIÓN 3: DISPARADOR DE OPORTUNIDAD
def calcular_roi_oportunidad(clientes_perdidos, ticket_promedio, comision_pct, aumento_pct):
    ganancia_ventas_recuperadas = (clientes_perdidos * ticket_promedio) * 365
    ganancia_total_bruta = ganancia_ventas_recuperadas * (1 + aumento_pct)
    costo_comision = ganancia_total_bruta * comision_pct
    ganancia_neta_anual = ganancia_total_bruta - costo_comision
    return ganancia_neta_anual

# INTERFAZ (La App con Streamlit) 

st.set_page_config(layout="wide")
st.title("Calculadora de Diagnóstico de Digitalización para Pymes 🚀")

df_benchmarks = cargar_benchmarks()

# --- 1. SELECCIÓN DE SECTOR (El Menú) ---

sector = st.selectbox(
    "1. Selecciona el sector de tu PYME",
    ["Retail", "Servicios (Próximamente)", "Restaurante (Próximamente)"]
)

# Filtrar benchmarks para el sector elegido
# Solo funciona si eligen "Retail"
if sector == "Retail":
    benchmarks = df_benchmarks[df_benchmarks['Sector'] == 'Retail'].iloc[0]

    st.header(f"Diagnóstico para sector: {sector}", divider="gray")
    
    # --- 2. CUESTIONARIO (Los Inputs del Usuario) ---
    st.subheader("Por favor, responde con tus datos actuales:")
    
    col1, col2 = st.columns(2) # Dividimos en 2 columnas

    with col1:
        st.info("Disparador de Eficiencia")
        sim_horas_manuales_semana = st.slider(
            "¿Cuántas horas a la semana gastas en tareas manuales (inventario, facturación)?", 0, 40, 10
        )
        sim_salario_admin_mes = st.number_input(
            "¿Cuál es el salario mensual de quien hace esas tareas?", 0, 50000, 8000, step=1000
        )

    with col2:
        st.info("Disparador de Oportunidad")
        sim_clientes_perdidos_dia = st.slider(
            "¿Cuántos clientes (aprox.) pierdes al día por no aceptar tarjeta?", 0, 10, 2
        )
        sim_ticket_promedio_efectivo = st.number_input(
            "¿Cuál es tu ticket promedio en efectivo ($MXN)?", 0, 2000, 150, step=10
        )
    
    # Input de Riesgo (ocupa toda la fila)
    st.info("Disparador de Riesgo")
    prob_input = st.slider(
        "Del 1 (nula) al 10 (alta), ¿qué tan probable crees que sea cometer un error grave de facturación manual este año?", 1, 10, 3
    )
    sim_probabilidad_error_sat = prob_input / 10.0 # Convertimos 3 a 0.3


    # EL BOTÓN Y DIAGNÓSTICO
    st.divider()
    if st.button("Calcular Diagnóstico", type="primary"):
        
        # Ejecutar Función 1 (Eficiencia)
        ahorro_eficiencia, costo_manual, costo_sw = calcular_roi_eficiencia(
            sim_horas_manuales_semana,
            sim_salario_admin_mes,
            benchmarks['Costo_Mensual_Software_MXN']
        )
        
        # Ejecutar Función 2 (Riesgo)
        ahorro_riesgo, riesgo_anual = calcular_roi_riesgo(
            benchmarks['Costo_Riesgo_MXN'],
            benchmarks['Costo_Mensual_Software_MXN'],
            sim_probabilidad_error_sat
        )
        
        # Ejecutar Función 3 (Oportunidad)
        ganancia_neta = calcular_roi_oportunidad(
            sim_clientes_perdidos_dia,
            sim_ticket_promedio_efectivo,
            benchmarks['KPI_Oportunidad_Comision'],
            benchmarks['KPI_Oportunidad_Aumento_Ticket']
        )

        # MOSTRAR LOS RESULTADOS 
        st.header("📈 Tu Diagnóstico Financiero (Resultados Anuales)")
        
        # Crear 3 columnas para los KPIs principales
        kpi1, kpi2, kpi3 = st.columns(3)
        
        kpi1.metric(
            label="Ahorro neto por Eficiencia",
            value=f"${ahorro_eficiencia:,.2f} MXN",
            delta="Positivo" if ahorro_eficiencia > 0 else "Negativo"
        )
        
        kpi3.metric(
            label="Ganancia Neta por Oportunidad",
            value=f"${ganancia_neta:,.2f} MXN",
            delta="Ingreso Nuevo"
        )

        kpi2.metric(
            label="Riesgo Anualizado vs Costo del Software",
            value=f"${ahorro_riesgo:,.2f} MXN",
            help=f"Tu riesgo anualizado es de $ {riesgo_anual:,.2f}\u00A0vs.\u00A0un\u00A0costo\u00A0de\u00A0software\u00A0de\u00A0$ {costo_sw:,.2f}. Este es el ahorro neto por protegerte."
        )

        # VEREDICTO 
        st.header("📋 Plan de Acción (Prioridades de Digitalización)")
        
        # Lógica para priorizar
        prioridades = {
            "Implementar Pagos Digitales": ganancia_neta,
            "Automatizar Procesos (POS)": ahorro_eficiencia + ahorro_riesgo
        }
        
        # Ordenar por el mayor impacto financiero
        plan_ordenado = sorted(prioridades.items(), key=lambda item: item[1], reverse=True)
        
        st.success(f"**Prioridad #1: {plan_ordenado[0][0]}**")
        st.write(f"Impacto financiero anual estimado: **${plan_ordenado[0][1]:,.2f} MXN**")

        st.warning(f"**Prioridad #2: {plan_ordenado[1][0]}**")
        st.write(f"Impacto financiero anual estimado: **${plan_ordenado[1][1]:,.2f} MXN**")

# Mensaje para sectores no implementados
elif sector != "Retail":
    st.error("¡Gracias por tu interés! El módulo de diagnóstico para tu sector está en desarrollo.")
    st.write("El framework está listo, solo necesitamos cargar los benchmarks de tu sector.")

