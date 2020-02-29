from operator import itemgetter

from utils.format_data import get_bytes_size

import psutil


def get_process_by_cpu_percent(sort_by_cpu_percent=True):
    processes = []
    for proc in psutil.process_iter(
        ["pid", "cpu_percent", "memory_percent", "name", "username"]
    ):
        processes.append(proc.info)

    return sorted(processes, key=itemgetter("cpu_percent"), reverse=sort_by_cpu_percent)


def get_process_by_memory_percent(sort_by_memory_percent=True):
    processes = []
    for proc in psutil.process_iter(
        ["pid", "cpu_percent", "memory_percent", "name", "username"]
    ):
        processes.append(proc.info)

    return sorted(
        processes, key=itemgetter("memory_percent"), reverse=sort_by_memory_percent
    )


def get_total_memory():
    memory = psutil.virtual_memory()
    total_memory = get_bytes_size(memory.total)
    return total_memory


def get_available_memory():
    memory = psutil.virtual_memory()
    available_memory = get_bytes_size(memory.available)
    return available_memory


def get_used_memory():
    memory = psutil.virtual_memory()
    used_memory = get_bytes_size(memory.used)
    return used_memory


def get_used_memory_percentage():
    memory = psutil.virtual_memory()
    return memory.percent

