# Monitor system resources, like cpu usage, memory usage, and network usage.
import psutil
import time

def get_cpu_usage():
    return psutil.cpu_percent(interval=1)

def get_memory_usage():
    return psutil.virtual_memory().percent

def get_disk_usage():
    return psutil.disk_usage('/').percent

def get_network_usage():
    net_io = psutil.net_io_counters()
    return net_io.bytes_sent, net_io.bytes_recv

# format bytes to human readable format
def format_bytes(bytes):
    if bytes < 1024:
        return "{:.2f} B".format(bytes)
    elif bytes < 1024**2:
        return "{:.2f} KB".format(bytes / 1024)
    elif bytes < 1024**3:
        return "{:.2f} MB".format(bytes / 1024**2)
    else:
        return "{:.2f} GB".format(bytes / 1024**3)

if __name__ == "__main__":
    prev_net = get_network_usage()
    while True:
        # Cache these before we wait, so we get the usage metrics to appear immediately
        # This can cause a slight inaccuracy in the metrics shown as they will be from the previous second
        # But this is not a big deal for this use case
        cpu = get_cpu_usage()
        memory = get_memory_usage()
        disk = get_disk_usage()
        curr_net = get_network_usage()

        # Since get_network_usage() returns the total bytes sent and received since the system booted,
        # we need to calculate the bytes sent and received per second by subtracting the previous value
        # from the current value to get the current network usage for that second
        net_sent_per_sec = curr_net[0] - prev_net[0]
        net_recv_per_sec = curr_net[1] - prev_net[1]
        prev_net = curr_net

        time.sleep(1)

        print("\033[H\033[J") # Clears output -- This how I make the numbers update in place
        print("CPU Usage: {}%".format(cpu))
        print("Memory Usage: {}%".format(memory))
        print("Disk Usage: {}%".format(disk))

        sent_str = format_bytes(net_sent_per_sec)
        recv_str = format_bytes(net_recv_per_sec)

        print("Network Usage: Sent: {}, Recv: {}".format(sent_str, recv_str))
