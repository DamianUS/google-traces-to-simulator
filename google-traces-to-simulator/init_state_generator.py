import csv
import random
from random import randint

init_state_file = open('/Users/dfernandez/IdeaProjects/efficiency-cluster-scheduler-simulator/traces/initial-traces/example-init-cluster-state.log', 'wb')
init_state_file_writer = csv.writer(init_state_file, delimiter=' ', quotechar='"', quoting=csv.QUOTE_NONE)

cpus_per_machine = 3.9
mem_per_machine = 7.9
batch_avg_tasks = 180.0
batch_avg_cpus_per_task = 0.3
batch_avg_mem_per_task = 0.5
service_avg_tasks = 30.0
service_avg_cpus_per_task = 0.9
service_avg_mem_per_task = 1.3
#80% jobs batch
batch_service_relation = 0.9

def random_with_N_digits(n):
    range_start = 10**(n-1)
    range_end = (10**n)-1
    return randint(range_start, range_end)

for x in range(0, 10000):
    random_numb = random.random()
    init_row = list()
    init_row.append(11)
    init_row.append(0.0000)
    init_row.append(random_with_N_digits(18))
    if random_numb > batch_service_relation:
        init_row.append(1)
        init_row.append(3)
        num_tasks = 0.0
        while num_tasks <= 0.0:
            num_tasks = random.expovariate(1.0/service_avg_tasks)
            #num_tasks = random.gauss(service_avg_tasks, service_avg_tasks)
        num_cpu_job = 0.0
        while num_cpu_job <= 0.0:
            #num_cpu_job = num_tasks * random.gauss(service_avg_cpus_per_task, service_avg_cpus_per_task*0.7)
            num_cpu_job = num_tasks * service_avg_cpus_per_task
        num_mem_job = 0.0
        while num_mem_job <= 0.0:
            #num_mem_job = num_tasks * random.gauss(service_avg_mem_per_task, service_avg_mem_per_task*0.7)
            num_mem_job = num_tasks * service_avg_mem_per_task
        init_row.append(int(num_tasks))
        init_row.append(num_cpu_job)
        init_row.append(num_mem_job*1024*1024*1024)
        init_state_file_writer.writerow(init_row)
    else:
        init_row.append(0)
        init_row.append(0)
        num_tasks = 0.0
        while num_tasks <= 0.0:
           num_tasks = random.expovariate(1.0/batch_avg_tasks)
           #num_tasks = random.gauss(batch_avg_tasks, batch_avg_tasks*5)
        num_cpu_job = 0.0
        while num_cpu_job <= num_tasks * 0.01:
            #num_cpu_job = num_tasks * random.gauss(batch_avg_cpus_per_task, batch_avg_cpus_per_task*0.8)
            num_cpu_job = num_tasks * batch_avg_cpus_per_task
        num_mem_job = 0.0
        while num_mem_job <= num_tasks * 0.01:
            #num_mem_job = num_tasks * random.gauss(batch_avg_mem_per_task, batch_avg_mem_per_task*0.8)
            num_mem_job = num_tasks * batch_avg_mem_per_task
        init_row.append(int(num_tasks))
        init_row.append(num_cpu_job)
        init_row.append(num_mem_job*1024*1024*1024)
        init_state_file_writer.writerow(init_row)
init_state_file.close()



