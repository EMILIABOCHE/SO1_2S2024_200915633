#REPOSITORIO https://github.com/EMILIABOCHE/SO1_2S2024_200915633/tree/main/tarea2
#!/bin/bash
 
if ! command -v docker &> /dev/null
then
    echo "Docker no está instalado. Por favor, instala Docker primero."
    exit 1
fi
 
generate_random_name() {
    cat /proc/sys/kernel/random/uuid | cut -d'-' -f1
}

 
for i in $(seq 1 10)
do
    container_name=$(generate_random_name)
    echo "Creando contenedor con nombre: $container_name"
    docker run -d --name "$container_name" alpine
done

echo "10 contenedores han sido creados."

