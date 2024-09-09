# Usa una imagen base de Python
FROM python:3.9-slim

# Establece el directorio de trabajo
WORKDIR /app

# Copia los archivos necesarios
COPY requirements.txt /app/requirements.txt
COPY servisPython.py /app/servisPython.py

# Instala las dependencias
RUN pip install --no-cache-dir -r /app/requirements.txt


# Exponer el puerto 5000 para Flask
EXPOSE 5000

# Comando para ejecutar la aplicación
CMD ["python", "servisPython.py"]
