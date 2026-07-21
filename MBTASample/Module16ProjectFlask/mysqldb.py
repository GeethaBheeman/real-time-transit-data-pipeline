import os
import mysql.connector

def insertMBTARecord(mbtaList):
    mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password=os.getenv("MYSQL_PASSWORD", "YOUR_MYSQL_PASSWORD"),
    database="MBTAdb",
    port=3307
    )

    mycursor = mydb.cursor()
    #complete the following line to add all the fields from the table
    #sql = "insert into mbta_buses ( id, longitude, latitude) values (%s, %s,%s)"
    sql = """
    INSERT INTO mbta_buses (
        id,
        label,
        latitude,
        longitude,
        bearing,
        direction_id,
        current_status,
        occupancy_status,
        stop_id,
        trip_id,
        current_stop_sequence,
        updated_at
    )
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    """

    for mbtaDict in mbtaList:
        latitude = mbtaDict.get("latitude")
        longitude = mbtaDict.get("longitude")

        if latitude is None or longitude is None:
            continue

        val = (
            mbtaDict.get("id"),
            mbtaDict.get("label"),
            latitude,
            longitude,
            mbtaDict.get("bearing"),
            mbtaDict.get("direction_id"),
            mbtaDict.get("current_status"),
            mbtaDict.get("occupancy_status"),
            mbtaDict.get("stop_id"),
            mbtaDict.get("trip_id"),
            mbtaDict.get("current_stop_sequence"),
            mbtaDict.get("updated_at")
            )
        mycursor.execute(sql, val)

    mydb.commit()
    mydb.close()
    