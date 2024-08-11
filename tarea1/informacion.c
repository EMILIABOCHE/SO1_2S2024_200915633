 #include <linux/module.h>
#include <linux/kernel.h>
#include <linux/init.h>
#include <linux/sched.h>
#include <linux/mm.h>
#include <linux/sysinfo.h>

MODULE_LICENSE("GPL");
MODULE_AUTHOR("Emilia Boche");
MODULE_DESCRIPTION("Un módulo del kernel para mostrar información detallada de uso de RAM e información de procesos");

static int __init informacion_init(void)
{
    struct sysinfo info;
    si_meminfo(&info);

    unsigned long total_ram = info.totalram * info.mem_unit;
    unsigned long free_ram = info.freeram * info.mem_unit;
    printk(KERN_INFO "Total RAM: %lu bytes\n", total_ram);
    printk(KERN_INFO "Free RAM: %lu bytes\n", free_ram);

    int parent_processes = 0;
    int child_processes = 0;

    printk(KERN_INFO "Procesos:\n");

    struct task_struct *task;
    struct list_head *list;
    for_each_process(task) {
        if (task->parent) {
            // Información del proceso padre
            if (task->parent == &init_task) {
                parent_processes++;
                printk(KERN_INFO "Proceso Padre - PID: %d, Nombre: %s\n", task->pid, task->comm);
            } else {
                // Información del proceso hijo
                child_processes++;
                printk(KERN_INFO "Proceso Hijo - PID: %d, Nombre: %s, PID Padre: %d\n", task->pid, task->comm, task->parent->pid);
            }
        }
    }

    printk(KERN_INFO "Número de Procesos Padre: %d\n", parent_processes);
    printk(KERN_INFO "Número de Procesos Hijo: %d\n", child_processes);

    return 0;
}

static void __exit informacion_exit(void)
{
    printk(KERN_INFO "Módulo del kernel desinstalado\n");
}

module_init(informacion_init);
module_exit(informacion_exit);

