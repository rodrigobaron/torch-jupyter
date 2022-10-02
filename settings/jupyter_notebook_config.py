import os

size_in_GB = int(os.getenv('SYS_MEM_LIMIT', 16))
number_of_cpus = int(os.getenv('SYS_CPU_LIMIT', 8))

c = get_config()

# memory
c.ResourceUseDisplay.mem_limit = size_in_GB *1024*1024*1024

# cpu
c.ResourceUseDisplay.track_cpu_percent = True
c.ResourceUseDisplay.cpu_limit = number_of_cpus