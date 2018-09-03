from sispag_boleto.boletos import data
from bson import ObjectId
from sispag_boleto.sispag_service import SispagService

serv = SispagService(None)
query = {'_id': {'$in': [ObjectId(boleto) for boleto in data]}}
boletos = list(serv.iptu_service.search(query))
serv.generate_sispag_iptu_report(boletos, '03091809')


# from reports.sispag_iptu_report import SispagIptuReportService

# rep = SispagIptuReportService(boletos, '03091807', '')
# rep.build_report()
