# Exploración de Datos (EDA) en Netflix

## 📖 Contexto y Objetivos

Netflix, una de las principales plataformas de streaming a nivel mundial, cuenta con una vasta biblioteca de contenido. Este análisis tiene como objetivo comprender patrones clave de producción, clasificaciones y duración para identificar oportunidades estratégicas.

### **Objetivos del análisis**
1. Explorar y comparar patrones en las producciones de Netflix.
2. Contrastar hipótesis planteadas sobre géneros y clasificaciones.
3. Generar insights que puedan guiar estrategias de contenido.

---

## 🧐 Hipótesis y Preguntas a Responder

### **Hipótesis Principal:**
Los géneros más populares en películas son distintos de los géneros más populares en programas de TV.

### **Hipótesis Secundaria:**
La mayoría de las producciones recientes (2010-2023) tienen clasificaciones orientadas al público joven (PG-13, TV-14).

### **Preguntas clave:**
1. ¿Qué géneros son más frecuentes en películas comparado con programas de TV?
2. ¿Cómo ha variado la producción de contenido a lo largo de los años (1950-2023)?
3. ¿Qué clasificaciones por edades son más comunes y cómo se distribuyen por tipo?
4. ¿Cuáles son los países que más producen contenido en Netflix?
5. ¿Existe una diferencia notable en la duración promedio entre géneros?

---

## 🔧 Metodología

### **Datos:**
- **Fuente:** Dataset público de Netflix Movies and TV Shows.
- **Variables clave:** Type, Genre, Rating, Release Year, Duration, Country.

### **Herramientas:**
- Python: `pandas`, `numpy`, `matplotlib`, `seaborn`.

### **Procesos:**
1. Limpieza y transformación de datos.
2. Análisis Univariante, Bivariante y Multivariante.
3. Visualización y generación de insights clave.

---

## 📝 Resultados y Contraste con Hipótesis

### **1. Hipótesis Principal:**
- **Insight Clave:**
  - **Movies:** Thriller y Romance son los géneros más frecuentes.
  - **TV Shows:** Sci-Fi y Horror lideran las producciones.
- **Conclusión:** Se confirma que los géneros más populares son distintos entre Movies y TV Shows.

### **2. Hipótesis Secundaria:**
- **Insight Clave:**
  - Clasificaciones más frecuentes: TV-14, R, PG y PG-13.
  - **Movies:** Más títulos clasificados como R y PG-13.
  - **TV Shows:** Dominan las clasificaciones G, PG y TV-14.
- **Conclusión:** Parcialmente confirmada. Aunque PG-13 y TV-14 son populares, R también tiene gran presencia.

### **3. Producción de contenido a lo largo del tiempo:**
- **Insight Clave:**
  - Picos de producción en 2005, 1979 y 1983.
  - Tendencia decreciente en años recientes (2015-2023).
- **Conclusión:** La producción ha fluctuado con picos notables y luego declina.

### **4. Producción por país:**
- **Insight Clave:**
  - **Canadá** lidera con 421 producciones, seguido por Reino Unido y Corea del Sur.
  - Fuerte presencia en mercados anglosajones y asiáticos.
- **Conclusión:** Netflix domina en mercados clave como Canadá y Reino Unido.

### **5. Duración promedio por género:**
- **Insight Clave:**
  - **TV Shows:** Duración promedio de 600-700 minutos.
  - **Movies:** Duración promedio estable de 130 minutos.
- **Conclusión:** Existe una diferencia clara en la duración promedio por tipo.

---

## 📊 Visualizaciones

Las gráficas generadas incluyen:
- Distribución de géneros por tipo.
- Clasificaciones más comunes.
- Producción por país y año.
- Análisis de correlaciones y pairplots.

---

## 🚀 Plan de Acción y Recomendaciones

1. **Contenidos:**
   - Impulsar géneros Sci-Fi y Horror en TV Shows.
   - Enfocar clasificaciones PG-13 y TV-14 para atraer al público joven.
   - Colaborar con países líderes en producción (Canadá, Reino Unido, EE. UU.).

2. **Productivización:**
   - Crear un dashboard interactivo para monitorear la evolución de contenido por tipo, género y país.

3. **Comunicación:**
   - Presentar los insights al equipo de contenido.
   - Realizar workshops internos para implementar estrategias basadas en datos.

---

## 📬 Contacto

**Autor:** Miguel Ángel Silva Uria  
**Proyecto:** Análisis Exploratorio de Datos en Netflix  
