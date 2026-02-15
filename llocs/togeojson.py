#!/usr/bin/env python

import json
import sqlite3

conn = sqlite3.connect('llocs.db')

llocs = {
    "type": "FeatureCollection",
    "features": []
}

c = conn.cursor()

for row in c.execute('SELECT * FROM llocs').fetchall():
    lloc_id = row[0]
    name = row[1]
    latitude, longitude = row[6], row[5]
    description = row[2]
    actesq = f"SELECT * FROM ACTES WHERE lloc_id={lloc_id}"
    actes = []
    for act in c.execute(actesq):
        actes.append({"date": f"{act[1]}-{act[2]}-{act[3]}"})
    lloc = {
        "type": "Feature",
        "geometry": {
            "type": "Point",
            "coordinates": [latitude, longitude]
        },
        "properties": {
            "name": name,
            "description": description,
            "acts": actes
        }
    }
    llocs["features"].append(lloc)

print(json.dumps(llocs))
