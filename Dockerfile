# Usa la imagen oficial de Python 3.9 slim como base
FROM python:3.9-slim

# Establece el directorio de trabajo en /app
WORKDIR /app

# Copia el archivo requirements.txt al directorio de trabajo
COPY requirements.txt .

# Instala las dependencias del proyecto
RUN pip install --no-cache-dir -r requirements.txt

# Copia el resto de la aplicación al directorio de trabajo
COPY . .

# Expone el puerto 80 en el contenedor
EXPOSE 5000

# Define la variable de entorno FLASK_APP
ENV FLASK_APP=main.py

# Comando para ejecutar la aplicación cuando se inicie el contenedor
CMD ["flask", "run", "--host", "0.0.0.0", "--port", "80"]
