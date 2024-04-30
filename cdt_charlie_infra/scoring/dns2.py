import dns.resolver

def send_dns_req():
    resolver = dns.resolver.Resolver()
    resolver.nameservers = ['192.168.2.1']
    answer = resolver.query('command.team2.deathstar')
    return str(answer[0]) == '192.168.2.1'

def main():
    print(send_dns_req())

main()
