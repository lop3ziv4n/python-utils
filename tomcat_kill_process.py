import os

import psutil as ps


def find_process(name, cpu, memory):
    return [(p.pid, p.info['name'], p.info['memory_info'].rss, p.cpu_percent(interval=None), p.info['cwd'])
            for p in ps.process_iter(attrs=['name', 'memory_info', 'cpu_percent', 'cwd']) if name in p.info['name']
            and (0 < memory <= p.info['memory_info'].rss or 0.0 < cpu <= p.cpu_percent(interval=None))]


def shutdown(pid):
    print(pid)
    if ps.pid_exists(pid) and pid != os.getpid():
        process = ps.Process(pid)
        process.kill()
        process.wait()


def startup(shell):
    print(shell)
    os.system('"' + shell + '"')


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Kill process by cpu or memory")
    parser.add_argument("-m", "--memory",
                        help="Memory limit in bytes to restart java service, example 15028224", default=0)
    parser.add_argument("-c", "--cpu",
                        help="CPU Usage limit to restart java service, example 0.5",
                        default=0.0)

    # parse arguments
    args = parser.parse_args()
    cpu = float(args.cpu)
    memory = int(args.memory)

    for p in find_process('java', cpu, memory):
        shutdown(p[0])
        if ps.LINUX:
            startup(p[4] + '/startup.sh')
        if ps.WINDOWS:
            startup(p[4] + '\\startup.bat')
