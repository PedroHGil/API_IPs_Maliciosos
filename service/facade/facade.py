from service import abuse_ip
from service import virus_total
from service import criminal_ip

class Facade:

    
    def __init__(self, request_body):
        self.scan = request_body.scan
        self.abuse_ip_service = abuse_ip.AbuseIP_API()
        self.criminal_ip_service = criminal_ip.CriminalIP_API()
        self.virus_total_service = virus_total.VirusTotal_API()

    def generate_report(self):
        json = {}
        
        json.update(self.abuse_ip_service.get_report(self.scan))
        json.update(self.virus_total_service.get_report_ip(self.scan))
        json.update(self.criminal_ip_service.get_report(self.scan))

        return json
    
    def generate_report_url(self):
        json = {}
        
        json.update(self.virus_total_service.get_report_url(self.scan))
        json.update(self.criminal_ip_service.get_report_url(self.scan))
        
        return json
        
        

        
