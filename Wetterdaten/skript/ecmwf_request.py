
from ecmwfapi import ECMWFDataServer

# select server
server = ECMWFDataServer()


def retrieve_tigge_data():
    # select the dates
    dates = [
        "2019-01-01", "2019-01-07", "2019-01-13", "2019-01-19", "2019-01-25", "2019-01-31",
        "2019-02-06", "2019-02-12", "2019-02-18", "2019-02-24",
        "2019-03-02", "2019-03-08", "2019-03-14", "2019-03-20", "2019-03-26",
        "2019-04-01", "2019-04-07", "2019-04-13", "2019-04-19", "2019-04-25",
        "2019-05-01", "2019-05-07", "2019-05-13", "2019-05-19", "2019-05-25", "2019-05-31",
        "2019-06-06", "2019-06-12", "2019-06-18", "2019-06-24", "2019-06-30"
        ]
    
    dates_2 = [
        "2019-07-06", "2019-07-12", "2019-07-18", "2019-07-24", "2019-07-30",
        "2019-08-05", "2019-08-11", "2019-08-17", "2019-08-23", "2019-08-29",
        "2019-09-04", "2019-09-10", "2019-09-16", "2019-09-22", "2019-09-28",
        "2019-10-04", "2019-10-10", "2019-10-16", "2019-10-22", "2019-10-28",
        "2019-11-03", "2019-11-09", "2019-11-15", "2019-11-21", "2019-11-27",
        "2019-12-03", "2019-12-09", "2019-12-15", "2019-12-21", "2019-12-27"
        ]
    # select the times
    times = ['00']

    # single request for every date/time
    for date in dates_2:
         for time in times:
             target = '/Users/mick/Documents/GitHub/masterthesis-mick/Wetterdaten/ECWMF_Data/ecmwf_sfc_%s.grb' % (date)
             tigge_pf_sfc_request(date, time, target)
 
 
def tigge_pf_sfc_request(date, time, target):
    '''
       A TIGGE request for perturbed forecast, sfc, ECMWF Center.
       Please note that a subset of the available data is requested below.
       Change the keywords below to adapt it to your needs. (ie to add more parameters, or numbers etc)
    '''
    # selected parameters
    server.retrieve({
        "class": "ti",
        "dataset": "tigge",
        "date": date,
        "expver": "prod",
        "grid": "2.0/2.0",
        "number": "1/to/50",
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
    # run the script automatically
    retrieve_tigge_data()

