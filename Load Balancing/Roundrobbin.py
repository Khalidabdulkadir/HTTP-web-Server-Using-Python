import itertools

servers = ['Server A', 'Server B', 'Server C']

server_cycle = itertools.cycle(servers)

def handle_req(req_id):
    server = next(server_cycle)
    print(f"Request {req_id} is handled by {server}")

for i in range(10):
    handle_req(i)