""" 
This file contains parameters that are common for all models. E.g
milage, readout date, carcom version etc.
"""

metadata = {'readout_id':'id',
            'readoutMeta':
            {
                'mileage': 'diagnosticReadoutEvent.odometer',
                'vin':'vehicle.vin',
                'readout_date_time': 'diagnosticReadoutEvent.utcReadOutDatetime',
                'carcomDBversion':'diagnosticReadoutEvent.carcomDbVersion',
                'global_time':'diagnosticReadoutEvent.vehicleGlobalTime',
                },
            
}

dcl_lvl = {'dcl_lvl1':'diagnosticData',
    'dcl_lvl2': 'decodedResponse',
    'dcl_lvl3': 'name',
    'dcl_lvl4': 'value',
}
