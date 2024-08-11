obj-m += informacion.o # obj-m es una variable que contiene el nombre del modulo a compilar

all:
	make -C /lib/modules/$(shell uname -r)/build M=$(PWD) modules

clean:
	make -C /lib/modules/$(shell uname -r)/build M=$(PWD) clean
