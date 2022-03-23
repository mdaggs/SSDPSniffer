from ssdpy import SSDPClient

client = SSDPClient()
devices = client.m_search("ssdp:all")

helenZaas = '192.168.0.13'

for value in devices:
    print(value,'\n')
    
print('Completed')



	