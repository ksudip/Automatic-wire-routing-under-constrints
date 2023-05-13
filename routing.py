global_grid=[]
class Signal:
    def __init__(self, source, target):
        self.source = source
        self.target = target
        self.path = []
        self.len=0
# coun=0
def route_signal(signal, congestion_limit, grid_size,wire_len):
    
    start_x, start_y = signal.source
    target_x, target_y = signal.target

    current_x, current_y = start_x, start_y
    signal.path.append((current_x, current_y))
    global_grid.append((current_x, current_y))
    
    while current_x != target_x or current_y != target_y:
        c_limit=congestion_limit
        if current_x < target_x and current_x<grid_size[0]:
            current_x += 1
        elif current_x > target_x and current_x>=0:
            current_x -= 1
        elif current_y < target_y and current_y<grid_size[1]:
            current_y += 1
        elif current_y > target_y and current_y>=0:
            current_y -= 1

        # if (current_x, current_y) in signal.path:
        if (current_x, current_y) in global_grid:
            # Path is blocked, increase congestion count
            c_limit -= 1

        signal.path.append((current_x, current_y))
        
        signal.len+=1

        if c_limit <= 0:
            # Congestion limit exceeded, exit routing
            signal.path = []  # Reset path to indicate failure
            break
        if wire_len<signal.len:
            signal.len=0
            break
        global_grid.append((current_x, current_y))
    return signal

# Example usage
congestion_limit = 2
grid_size = (301, 301)
n=int(input("please enter number of input u wish to give: "))
for i in range(0,n):
    wire_len=int(input("plese enter wire length: "))
    print("source_x & source_y")
    x, y = map(int, input().split())
    print("target_x & target_y")
    a, b = map(int, input().split())
    signal = Signal((x, y), (a, b))
    routed_signal = route_signal(signal, congestion_limit, grid_size, wire_len)

    if not routed_signal.path:
        print("Signal routing failed due to congestion limit.")
    elif not routed_signal.len:
        print("Signal routing failed due to wire limit.")
    else:
        print("Signal path length:", routed_signal.len)
        # global_grid.append(routed_signal.path)
        print("Signal path followed:", routed_signal.path)
