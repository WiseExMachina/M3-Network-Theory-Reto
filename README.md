# Reto Módulo 3: Análisis de una Red de Jugadores

**Curso:** Conceptos clave para la analítica de redes
**Programa:** Certificación Data Scientist, ITESM (Modalidad TLG)

---

## Descripción del Proyecto

Este proyecto analiza una red de transferencias en un mercado de jugadores de fútbol, representada por una matriz de adyacencias. Se calculan diversas métricas de la teoría de redes para identificar la estructura del mercado, sus actores clave (equipos) y sus propiedades generales, como la eficiencia y la formación de clústeres.

---

## Sobre este Proyecto y mi Aprendizaje 🚀

Este repositorio representa un importante viaje de aprendizaje personal.

Originalmente, el plan era usar Python únicamente para la tarea de visualizar el grafo de la red. Sin embargo, aproveché la oportunidad para profundizar en el ecosistema de análisis de datos de Python, utilizando librerías como **`networkx`**, **`numpy`** y **`matplotlib`** para realizar todos los cálculos y análisis requeridos por el reto, centralizando todo el trabajo en el script `grafo.py`.

Adicionalmente, este proyecto marcó mi primera experiencia práctica con el control de versiones desde la línea de comandos. Utilicé **Git** para documentar cada paso del proceso, desde la creación del script y la depuración de errores hasta la adición de cada nueva métrica de análisis. Este es mi primer repositorio gestionado de principio a fin con un flujo de trabajo de control de versiones.

---

## Análisis Realizado 📊

El script `grafo.py` realiza los siguientes cálculos sobre la red:

* Grado de cada uno de los vértices (equipos).
* Secuencia de grados de la red.
* Diámetro de la red.
* Distancias (caminos más cortos) entre todos los pares de vértices.
* Distribución de grados de la red.
* Coeficiente de agrupamiento (Clustering Coefficient) para nodos de interés.
* Centralidad de Intermediación (Betweenness Centrality) para nodos de interés.

---

## Cómo Ejecutar el Proyecto

Para ejecutar este análisis, sigue estos pasos:

1.  **Clona el repositorio:**
    ```bash
    git clone <URL-de-tu-repositorio>
    ```
2.  **Navega a la carpeta del proyecto:**
    ```bash
    cd <nombre-de-la-carpeta>
    ```
3.  **Crea un ambiente virtual y actívalo:**
    ```bash
    python3 -m venv env
    source env/bin/activate
    ```
4.  **Instala las dependencias:**
    ```bash
    pip install -r requirements.txt
    ```
5.  **Ejecuta el script de análisis:**
    ```bash
    python3 grafo.py
    ```


## Documentos adicionales en la era de la IA.

    Adicionalmente, este repositorio incluye el archivo prompts.md que sirve como un registro detallado de las interacciones con el modelo de IA que me asistió en cada fase del proyecto. Este documento fue generado utilizando NotebookLM, lo cual no solo documenta el proceso de resolución, sino que también refleja una práctica de trabajo transparente y un flujo de pensamiento guiado. 
