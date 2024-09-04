#!/bin/bash

# Ruta al archivo de log
LOGFILE="/home/emilia/SopesLab/SO1_2S2024_200915633/LaboratorioSopes/SO1_2S2024_200915633/Proyecto1/parte1/crearConteiner.log"


# Función para crear una imagen aleatoria
create_random_image() {
  IMAGE_NAME=$(head /dev/urandom | tr -dc a-z0-9 | head -c 8)
  echo "Creando imagen $IMAGE_NAME" >> $LOGFILE

  case $((RANDOM % 4)) in
    0)
      cat <<EOF > Dockerfile
FROM ubuntu:latest
RUN apt-get update && apt-get install -y stress
CMD ["stress", "--vm", "1", "--vm-bytes", "512M", "--vm-keep", "-t", "600"]
EOF
      ;;
    1)
      cat <<EOF > Dockerfile
FROM ubuntu:latest
RUN apt-get update && apt-get install -y stress
CMD ["stress", "--cpu", "4", "-t", "600"]
EOF
      ;;
    2)
      cat <<EOF > Dockerfile
FROM ubuntu:latest
CMD ["sh", "-c", "echo 'Low RAM usage' && sleep 600"]
EOF
      ;;
    3)
      cat <<EOF > Dockerfile
FROM ubuntu:latest
CMD ["sh", "-c", "echo 'Low CPU usage' && sleep 600"]
EOF
      ;;
  esac

  sudo docker build -t $IMAGE_NAME . >> $LOGFILE 2>&1
  sudo rm Dockerfile
  echo $IMAGE_NAME
}

# Bucle principal para crear y ejecutar contenedores
while true; do
  IMAGES=()
  
  # Crear 10 imágenes
  for i in {1..10}; do
    IMAGE_NAME=$(create_random_image)
    IMAGES+=($IMAGE_NAME)
  done

  # Ejecutar 10 contenedores
  for i in {1..10}; do
    IMAGE=${IMAGES[$RANDOM % ${#IMAGES[@]}]}
    CONTAINER_NAME=$(head /dev/urandom | tr -dc A-Za-z0-9 | head -c 8)
    echo "Iniciando contenedor $CONTAINER_NAME con imagen $IMAGE" >> $LOGFILE
    sudo docker run -d --name $CONTAINER_NAME $IMAGE >> $LOGFILE 2>&1
  done

  # Esperar 30 segundos antes de la siguiente iteración
  sleep 30
done
