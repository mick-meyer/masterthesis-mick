
from ecmwfapi import ECMWFDataServer
server = ECMWFDataServer()
    
def retrieve_tigge_data():
    dates = ['2019-01-01', '2019-01-07', '2019-01-14', '2019-01-21', '2019-01-28']
    times = ['00']
    for date in dates:
         for time in times:
             target = 'ecmwf_sfc_%s_%s.grb' % (date, time)
             tigge_pf_sfc_request(date, time, target)
 
 
def tigge_pf_sfc_request(date, time, target):
    '''
       A TIGGE request for perturbed forecast, sfc, ECMWF Center.
       Please note that a subset of the available data is requested below.
       Change the keywords below to adapt it to your needs. (ie to add more parameters, or numbers etc)
    '''
    server.retrieve({
        "class": "ti",
        "dataset": "tigge",
        "date": date,
        "expver": "prod",
        "grid": "2.0/2.0",
        "number": "1/to/10",
        "area": "55/06/47/15",
        "levtype": "sfc",
        "origin": "ecmf",
        "param": "165/166/167/176",
        "step": "0/6/12/18/24/30/36/42/48/54/60/66/72/78/84/90/96/102/108/114/120/126/132/138/144",
        "time": "00:00:00",
        "type": "pf",
        "target": target
    })
 
if __name__ == '__main__':
    retrieve_tigge_data()

