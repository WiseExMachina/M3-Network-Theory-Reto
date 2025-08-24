#!/bin/bash

echo "--- Creando el ambiente virtual... ---"
python3 -m venv graph_env

echo "--- Activando el ambiente e instalando paquetes... ---"
source graph_env/bin/activate
pip install networkx numpy matplotlib scipy

echo "--- Configurando Git por primera vez... ---"
git config --global user.name "Bernardo Lozano Wise"
git config --global user.email "bernardolw@gmail.com"

echo "✅ ¡Configuración completada!"
echo "Recuerda activar tu ambiente con: source graph_env/bin/activate"
