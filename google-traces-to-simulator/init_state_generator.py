import csv
import random
from random import randint

init_state_file = open('/Users/dfernandez/IdeaProjects/efficiency-cluster-scheduler-simulator/traces/example-init-cluster-state-generado.log', 'wb')
init_state = csv.writer(init_state_file, delimiter=' ', quotechar='', quoting=csv.QUOTE_NONE)

def random_with_N_digits(n):
    range_start = 10**(n-1)
    range_end = (10**n)-1
    return randint(range_start, range_end)

for x in range(0, 1000):
    random_numb = random.random()
    init_row = list()
    init_row.append(11)
    init_row.append(0.0000)
    init_row.append(random_with_N_digits(18))
    if random_numb > 0.8:
        init_row.append(1)
        init_row.append(3)
        random.expovariate
        num_tasks = 0.0
        while num_tasks <= 0.0:
            num_tasks = random.gauss(20.00, 40.00)
        num_cpu_job = 0.0
        while num_cpu_job <= 0.0:
            num_cpu_job = num_tasks * random.gauss(2.000, 1.5)
        num_mem_job = 0.0
        while num_mem_job <= 0.0:
            num_mem_job = num_tasks * random.gauss(4.000, 3.5)
        init_row.append(num_tasks)
        init_row.append(num_cpu_job)
        init_row.append(num_mem_job*1024*1024*1024)
        init_state.writerow(init_row)
    else:
        init_row.append(0)
        init_row.append(0)
        num_tasks = 0.0
        while num_tasks <= 0.0:
            num_tasks = random.gauss(200.00, 500.00)
        num_cpu_job = 0.0
        while num_cpu_job <= num_tasks * 0.01:
            num_cpu_job = num_tasks * random.gauss(0.5, 0.6)
        num_mem_job = 0.0
        while num_mem_job <= num_tasks * 0.01:
            num_mem_job = num_tasks * random.gauss(1.000, 0.8)
        init_row.append(num_tasks)
        init_row.append(num_cpu_job)
        init_row.append(num_mem_job*1024*1024*1024)
        init_state.writerow(init_row)



