#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Análisis de la relación entre tasas de interés del Banco de la República 
de Colombia y las inversiones en CDT (2017-2025)
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats
from datetime import datetime
import os

# Configuraciones
plt.style.use('seaborn-v0_8-whitegrid')
plt.rcParams['figure.figsize'] = (12, 8)
plt.rcParams['font.size'] = 12
plt.rcParams['axes.titlesize'] = 16
plt.rcParams['axes.labelsize'] = 14
plt.rcParams['xtick.labelsize'] = 12
plt.rcParams['ytick.labelsize'] = 12
plt.rcParams['legend.fontsize'] = 12
plt.rcParams['figure.titlesize'] = 18

# Colores
COLOR_CDT = '#4C72B0'  # Azul
COLOR_TASA = '#C44E52'  # Rojo
COLOR_REGRESSION = '#55A868'  # Verde

# Crear carpeta para las imágenes si no existe
if not os.path.exists('imagenes'):
    os.makedirs('imagenes')

# Cargar los datos
def cargar_datos():
    """Carga y prepara los datos del CSV."""
    df = pd.read_csv('cdt_colombia_data.csv')
    
    # Convertir la columna Fecha a tipo datetime
    df['Fecha'] = pd.to_datetime(df['Fecha'])
    
    # Agregar columnas de año y mes
    df['Año'] = df['Fecha'].dt.year
    df['Mes'] = df['Fecha'].dt.month
    df['Trimestre'] = df['Fecha'].dt.to_period('Q').astype(str)
    
    # Crear columna para indicar si es dato anual o mensual
    df['Tipo'] = 'Mensual'
    df.loc[df['Fecha'].dt.is_year_end & (df['Fecha'] < '2023-01-01'), 'Tipo'] = 'Anual'
    
    # Ordenar por fecha
    df = df.sort_values('Fecha')
    
    return df

def explorar_datos(df):
    """Realiza un análisis exploratorio de los datos."""
    print("=== Resumen de Datos ===")
    print(f"Período analizado: {df['Fecha'].min().date()} a {df['Fecha'].max().date()}")
    print(f"Total de registros: {len(df)}")
    print("\n=== Estadísticas Descriptivas ===")
    print(df[['SuperFinanciera_CDT_Billones', 'TasaInteres_BancoRepublica']].describe())
    
    # Verificar correlación
    correlation = df['SuperFinanciera_CDT_Billones'].corr(df['TasaInteres_BancoRepublica'])
    print(f"\nCorrelación entre CDT y Tasas de Interés: {correlation:.4f}")
    
    return correlation

def serie_temporal_combinada(df):
    """Gráfico de serie temporal combinada de CDT y tasas de interés."""
    fig, ax1 = plt.subplots()
    
    # Graficar CDT
    ax1.set_xlabel('Fecha')
    ax1.set_ylabel('Inversión en CDT (billones COP)', color=COLOR_CDT)
    ax1.plot(df['Fecha'], df['SuperFinanciera_CDT_Billones'], marker='o', markersize=6, 
             linestyle='-', color=COLOR_CDT, label='CDT (SuperFinanciera)')
    ax1.tick_params(axis='y', labelcolor=COLOR_CDT)
    
    # Segundo eje Y para tasas de interés
    ax2 = ax1.twinx()
    ax2.set_ylabel('Tasa de Interés (%)', color=COLOR_TASA)
    ax2.plot(df['Fecha'], df['TasaInteres_BancoRepublica'], marker='s', markersize=6,
             linestyle='--', color=COLOR_TASA, label='Tasa de Interés')
    ax2.tick_params(axis='y', labelcolor=COLOR_TASA)
    
    # Marcar puntos clave
    # Punto mínimo de tasas (2021)
    min_tasa_idx = df['TasaInteres_BancoRepublica'].idxmin()
    ax2.plot(df.loc[min_tasa_idx, 'Fecha'], df.loc[min_tasa_idx, 'TasaInteres_BancoRepublica'], 
             'o', markersize=10, color='purple', label='Mínimo Tasas (2021)')
    
    # Máximo de CDT (mediados de 2024)
    max_cdt_idx = df['SuperFinanciera_CDT_Billones'].idxmax()
    ax1.plot(df.loc[max_cdt_idx, 'Fecha'], df.loc[max_cdt_idx, 'SuperFinanciera_CDT_Billones'], 
             'o', markersize=10, color='green', label='Máximo CDT (2024)')
    
    # Punto de inflexión (pandemia 2020)
    pandemic_idx = df[df['Fecha'] == '2020-12-31'].index[0]
    ax1.axvline(x=df.loc[pandemic_idx, 'Fecha'], color='gray', linestyle=':', label='Pandemia (2020)')
    
    # Agregar leyendas
    lines1, labels1 = ax1.get_legend_handles_labels()
    lines2, labels2 = ax2.get_legend_handles_labels()
    ax1.legend(lines1 + lines2, labels1 + labels2, loc='upper left')
    
    # Título y ajustes
    plt.title('Evolución de Inversiones en CDT y Tasas de Interés (2017-2025)')
    fig.tight_layout()
    plt.savefig('imagenes/serie_temporal_combinada.png', dpi=300, bbox_inches='tight')
    plt.close()

def analisis_correlacion(df):
    """Análisis de correlación entre CDT y tasas de interés."""
    x = df['TasaInteres_BancoRepublica']
    y = df['SuperFinanciera_CDT_Billones']
    
    # Cálculo de la regresión lineal
    slope, intercept, r_value, p_value, std_err = stats.linregress(x, y)
    
    # Crear gráfico
    plt.figure()
    
    # Scatter plot
    plt.scatter(x, y, color=COLOR_CDT, alpha=0.7, s=80, label='Datos observados')
    
    # Línea de regresión
    x_line = np.linspace(x.min(), x.max(), 100)
    y_line = slope * x_line + intercept
    plt.plot(x_line, y_line, color=COLOR_REGRESSION, linewidth=2, 
             label=f'Regresión: y = {slope:.2f}x + {intercept:.2f}')
    
    # Agregar etiquetas de año a algunos puntos clave
    for idx, row in df.iterrows():
        if row['Fecha'].month == 12 or row['Fecha'] == df['Fecha'].max():
            plt.annotate(str(row['Año']), 
                        (row['TasaInteres_BancoRepublica'], row['SuperFinanciera_CDT_Billones']),
                        xytext=(5, 5), textcoords='offset points')
    
    # Detalles del gráfico
    plt.xlabel('Tasa de Interés del Banco de la República (%)')
    plt.ylabel('Inversión en CDT (billones COP)')
    plt.title('Correlación entre Tasas de Interés e Inversiones en CDT')
    
    # Agregar texto con estadísticas
    stats_text = (f"Correlación (r): {r_value:.4f}\n"
                 f"R²: {r_value**2:.4f}\n"
                 f"Valor p: {p_value:.4f}\n"
                 f"Error estándar: {std_err:.4f}\n"
                 f"Pendiente: {slope:.2f}")
    plt.annotate(stats_text, xy=(0.05, 0.95), xycoords='axes fraction', 
                 bbox=dict(boxstyle="round,pad=0.3", fc="white", ec="gray", alpha=0.8),
                 va='top', ha='left')
    
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.savefig('imagenes/correlacion_cdt_tasas.png', dpi=300, bbox_inches='tight')
    plt.close()
    
    return slope, intercept, r_value**2

def analisis_reciente(df):
    """Análisis detallado del período reciente (2023-2025)."""
    # Filtrar datos recientes
    df_reciente = df[df['Fecha'] >= '2023-01-01'].copy()
    
    # Calcular variación mensual (solo para datos mensuales contiguos)
    df_reciente['Variacion_CDT'] = df_reciente['SuperFinanciera_CDT_Billones'].pct_change() * 100
    
    # Gráfico combinado de barras y líneas
    fig, ax1 = plt.subplots()
    
    # Gráfico de barras para variación mensual
    ax1.bar(df_reciente['Fecha'], df_reciente['Variacion_CDT'], 
            color=COLOR_CDT, alpha=0.5, label='Variación Mensual CDT (%)')
    ax1.set_xlabel('Fecha')
    ax1.set_ylabel('Variación Mensual CDT (%)', color=COLOR_CDT)
    ax1.tick_params(axis='y', labelcolor=COLOR_CDT)
    
    # Línea para tasa de interés
    ax2 = ax1.twinx()
    ax2.set_ylabel('Tasa de Interés (%)', color=COLOR_TASA)
    ax2.plot(df_reciente['Fecha'], df_reciente['TasaInteres_BancoRepublica'], 
             marker='o', linestyle='-', color=COLOR_TASA, label='Tasa de Interés')
    ax2.tick_params(axis='y', labelcolor=COLOR_TASA)
    
    # Leyenda
    lines1, labels1 = ax1.get_legend_handles_labels()
    lines2, labels2 = ax2.get_legend_handles_labels()
    ax1.legend(lines1 + lines2, labels1 + labels2, loc='lower left')
    
    # Títulos y ajustes
    plt.title('Variación Mensual de CDT y Tasas de Interés (2023-2025)')
    plt.xticks(rotation=45)
    fig.tight_layout()
    plt.savefig('imagenes/analisis_reciente.png', dpi=300, bbox_inches='tight')
    plt.close()
    
    # Estadísticas del período reciente
    print("\n=== Análisis del Período Reciente (2023-2025) ===")
    print(f"Máximo CDT: {df_reciente['SuperFinanciera_CDT_Billones'].max()} billones COP")
    max_idx = df_reciente['SuperFinanciera_CDT_Billones'].idxmax()
    print(f"Fecha máximo CDT: {df_reciente.loc[max_idx, 'Fecha'].strftime('%B %Y')}")
    
    print(f"\nVariación CDT Q1 2025: {df_reciente.iloc[-1]['SuperFinanciera_CDT_Billones'] - df_reciente.iloc[-4]['SuperFinanciera_CDT_Billones']:.1f} billones COP")
    print(f"Variación CDT Q1 2025 (%): {(df_reciente.iloc[-1]['SuperFinanciera_CDT_Billones'] / df_reciente.iloc[-4]['SuperFinanciera_CDT_Billones'] - 1) * 100:.2f}%")

def proyeccion_2026(df, slope, intercept):
    """Proyección para 2025-2026 basada en el modelo de regresión."""
    # Crear datos de proyección
    proyeccion = pd.DataFrame({
        'Periodo': ['Mar-2025', 'Jun-2025', 'Sep-2025', 'Dic-2025',
                   'Mar-2026', 'Jun-2026', 'Sep-2026', 'Dic-2026'],
        'Tasa': [10.00, 9.00, 8.25, 7.50, 6.75, 6.00, 5.50, 5.00],
        'Tipo': ['Actual', 'Proyección', 'Proyección', 'Proyección',
                'Proyección', 'Proyección', 'Proyección', 'Proyección']
    })
    
    # Calcular CDT proyectado
    proyeccion['CDT_Proyectado'] = slope * proyeccion['Tasa'] + intercept
    
    # Calcular variación respecto al máximo histórico
    maximo_cdt = df['SuperFinanciera_CDT_Billones'].max()
    proyeccion['Variacion_vs_Maximo'] = (proyeccion['CDT_Proyectado'] / maximo_cdt - 1) * 100
    
    # Gráfico de proyección
    plt.figure()
    
    # Diferenciar entre datos reales y proyección
    mask_actual = proyeccion['Tipo'] == 'Actual'
    mask_proyeccion = proyeccion['Tipo'] == 'Proyección'
    
    # Graficar CDT proyectado
    plt.plot(proyeccion.loc[mask_actual, 'Periodo'], 
             proyeccion.loc[mask_actual, 'CDT_Proyectado'], 
             'o-', color=COLOR_CDT, linewidth=2, markersize=8, label='CDT (Actual)')
    
    plt.plot(proyeccion.loc[mask_proyeccion, 'Periodo'], 
             proyeccion.loc[mask_proyeccion, 'CDT_Proyectado'], 
             'o--', color=COLOR_CDT, linewidth=2, markersize=8, label='CDT (Proyección)')
    
    # Graficar tasas
    plt.plot(proyeccion.loc[mask_actual, 'Periodo'], 
             proyeccion.loc[mask_actual, 'Tasa'], 
             's-', color=COLOR_TASA, linewidth=2, markersize=8, label='Tasa (Actual)')
    
    plt.plot(proyeccion.loc[mask_proyeccion, 'Periodo'], 
             proyeccion.loc[mask_proyeccion, 'Tasa'], 
             's--', color=COLOR_TASA, linewidth=2, markersize=8, label='Tasa (Proyección)')
    
    # Línea vertical para separar actual de proyección
    plt.axvline(x=0.5, color='gray', linestyle=':', linewidth=1.5)
    
    # Detalles del gráfico
    plt.title('Proyección de CDT y Tasas de Interés (2025-2026)')
    plt.ylabel('Valores (CDT en billones COP, Tasa en %)')
    plt.grid(True, alpha=0.3)
    plt.legend()
    plt.tight_layout()
    plt.savefig('imagenes/proyeccion_2026.png', dpi=300, bbox_inches='tight')
    plt.close()
    
    # Crear tabla de escenarios alternativos
    escenarios = pd.DataFrame({
        'Escenario': ['Reducción Acelerada', 'Escenario Base', 'Reducción Pausada'],
        'Tasa_2026': [3.00, 5.00, 7.00],
        'CDT_2026': [slope * 3.00 + intercept, slope * 5.00 + intercept, slope * 7.00 + intercept],
    })
    
    escenarios['Variacion_vs_Maximo'] = (escenarios['CDT_2026'] / maximo_cdt - 1) * 100
    
    # Gráfico de escenarios alternativos
    plt.figure()
    bars = plt.bar(escenarios['Escenario'], escenarios['CDT_2026'], color=COLOR_CDT, alpha=0.7)
    
    # Agregar etiquetas de valores
    for bar in bars:
        height = bar.get_height()
        plt.text(bar.get_x() + bar.get_width()/2., height + 1,
                 f'{height:.1f}',
                 ha='center', va='bottom')
    
    plt.title('Escenarios Alternativos para CDT (Dic 2026)')
    plt.ylabel('CDT Proyectado (billones COP)')
    plt.tight_layout()
    plt.savefig('imagenes/escenarios_alternativos.png', dpi=300, bbox_inches='tight')
    plt.close()
    
    # Imprimir proyecciones
    print("\n=== Proyecciones para 2025-2026 ===")
    print(proyeccion[['Periodo', 'Tasa', 'CDT_Proyectado', 'Variacion_vs_Maximo']].to_string(index=False))
    
    print("\n=== Escenarios Alternativos para Dic-2026 ===")
    print(escenarios.to_string(index=False))
    
    return proyeccion, escenarios

def main():
    """Función principal que ejecuta todo el análisis."""
    print("Iniciando análisis de CDT y tasas de interés en Colombia...\n")
    
    # Cargar datos
    df = cargar_datos()
    
    # Explorar datos
    correlation = explorar_datos(df)
    
    # Generar visualizaciones
    serie_temporal_combinada(df)
    slope, intercept, r_squared = analisis_correlacion(df)
    analisis_reciente(df)
    proyeccion, escenarios = proyeccion_2026(df, slope, intercept)
    
    # Resumen de resultados
    print("\n=== CONCLUSIONES DEL ANÁLISIS ===")
    print(f"1. Correlación positiva significativa (r = {correlation:.4f}, R² = {r_squared:.4f})")
    print(f"2. Modelo de regresión: CDT = {slope:.2f} × Tasa + {intercept:.2f}")
    print(f"3. Por cada punto porcentual de cambio en la tasa, el impacto es de {slope:.2f} billones de pesos en CDT")
    print(f"4. Nivel máximo histórico de CDT: {df['SuperFinanciera_CDT_Billones'].max():.1f} billones COP")
    print(f"5. Contracción proyectada hasta Dic-2026: {escenarios.loc[1, 'Variacion_vs_Maximo']:.1f}%")
    
    print("\nAnálisis completado. Las visualizaciones se han guardado en la carpeta 'imagenes'.")
    
if __name__ == "__main__":
    main()