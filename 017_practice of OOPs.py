class Server:

    def __init__(self,server_name,ip,environment):
        self.NAME = server_name
        self.IP = ip
        self.ENVIRONMENT = environment

    def show_details(self):
        print (f"SERVER: {self.NAME} | IP :{self.IP} | ENV :{self.ENVIRONMENT}")

server1 = Server("web-prod-01", "10.0.0.1", "Production")

server2 = Server("db-stage-01", "10.0.0.2", "Staging")

server3 = Server("app-prod-02", "10.0.0.3", "Production")

inventory = [server1,server2,server3]

print ("---DEV OPS SERVER INVENTORY---")

for server in inventory:
    server.show_details()