import urllib.request, json
import mysqldb

def callMBTAApi():
    mbtaDictList = []
    mbtaUrl = 'https://api-v3.mbta.com/vehicles?filter[route]=1&include=trip'
    with urllib.request.urlopen(mbtaUrl) as url:
        data = json.loads(url.read().decode())
        for bus in data['data']:
            busDict = dict()
            # complete the fields below based on the entries of your SQL table
            attributes = bus.get("attributes", {})
            relationships = bus.get("relationships", {})

            # -------------------------
            # BASIC IDENTIFIERS
            # -------------------------
            busDict['id'] = bus.get('id')
            busDict['label'] = attributes.get('label')

            # -------------------------
            # LOCATION DATA
            # -------------------------
            busDict['latitude'] = attributes.get('latitude')
            busDict['longitude'] = attributes.get('longitude')

            # -------------------------
            # MOVEMENT DATA
            # -------------------------
            busDict['bearing'] = attributes.get('bearing')
            busDict['direction_id'] = attributes.get('direction_id')
            busDict['current_status'] = attributes.get('current_status')

            # -------------------------
            # USAGE DATA
            # -------------------------
            busDict['occupancy_status'] = attributes.get('occupancy_status')

            # -------------------------
            # RELATIONSHIP DATA
            # -------------------------
            busDict['stop_id'] = relationships.get("stop", {}).get("data", {}).get("id")
            busDict['trip_id'] = relationships.get("trip", {}).get("data", {}).get("id")
            busDict['current_stop_sequence'] = attributes.get('current_stop_sequence')
            
            # -------------------------
            # TIMESTAMP
            # -------------------------
            busDict['updated_at'] = attributes.get('updated_at')
            mbtaDictList.append(busDict)
    mysqldb.insertMBTARecord(mbtaDictList) 

    return mbtaDictList  