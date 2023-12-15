import ujson
import random
import ubinascii
import machine
from micropython import const


class LoraPkg:
    def __init__(self):
        self.name = None
        self.uid = None
        self.value = None
        self.rssi = None
        self.lastTs = None
        self.batteryLevel = None
        self.humidity = None


class SensorPkg:
    def __init__(self):
        self.type = None
        self.uuid = None
        self.value = None
        self.lastTs = None


class OutputPkg:
    def __init__(self):
        self.name = None
        self.id = None
        self.uuidWirelessSensor = None
        self.value = None
        self.lastTs = None
        self.schedule = {'startTs' : None, 'endTs' : None}


class MasterDevice:
    def __init__(self):
        self.uuid = ubinascii.hexlify(machine.unique_id()).decode('utf-8')
        self.lastTs = None
        self.req = False
        self.push = False
        self.save = False
        
        self.rssi = None
        self.humidity = None
        self.temperature = None
        
        self.lora1 = LoraPkg()
        self.lora2 = LoraPkg()
        self.lora3 = LoraPkg()
        self.lora4 = LoraPkg()
        
        self.sensor1 = SensorPkg()
        self.sensor2 = SensorPkg()
        self.sensor3 = SensorPkg()
        self.sensor4 = SensorPkg()
        
        self.output1 = OutputPkg()
        self.output2 = OutputPkg()
        self.output3 = OutputPkg()
        self.output4 = OutputPkg()
        
        self.default_pkg = { "rssi": None, "humidity": None, "temperature": None,
                        "sensors": [{ "type": None, "uuid": None, "value": None, "lastTs": None }],
                        "outputs": [{ "name": None, "value": None, "lastTs": None, "id": None, "uuidWirelessSensor": None,
                                      "schedule": { "startTs": None, "endTs": None }}],
                        "wirelessSensors": [{ "rssi": None, "name": None, "lastTs": None, "uid": None, "batteryLevel": None, "humidity": None }]}
        
        self.check_last()


    def update_last(self, data):
        self.rssi = data.get("rssi")
        self.humidity = data.get("humidity")
        self.temperature = data.get("temperature")
        
        temp = data.get("wirelessSensors")
        if temp != None:
            try:
                lora = temp[0]
                self.lora1.name = lora.get("name")
                self.lora1.uid = lora.get("uid")
                self.lora1.value = lora.get("value")
                self.lora1.rssi = lora.get("rssi")
                self.lora1.lastTs = lora.get("lastTs")
                self.lora1.batteryLevel = lora.get("batteryLevel")
                self.lora1.humidity = lora.get("humidity")
            except:
                self.lora1 = LoraPkg()
            try:
                lora = temp[1]
                self.lora2.name = lora.get("name")
                self.lora2.uid = lora.get("uid")
                self.lora2.value = lora.get("value")
                self.lora2.rssi = lora.get("rssi")
                self.lora2.lastTs = lora.get("lastTs")
                self.lora2.batteryLevel = lora.get("batteryLevel")
                self.lora2.humidity = lora.get("humidity")
            except:
                self.lora2 = LoraPkg()
            try:
                lora = temp[2]
                self.lora3.name = lora.get("name")
                self.lora3.uid = lora.get("uid")
                self.lora3.value = lora.get("value")
                self.lora3.rssi = lora.get("rssi")
                self.lora3.lastTs = lora.get("lastTs")
                self.lora3.batteryLevel = lora.get("batteryLevel")
                self.lora3.humidity = lora.get("humidity")
            except:
                self.lora3 = LoraPkg()
            try:
                lora = temp[3]
                self.lora4.name = lora.get("name")
                self.lora4.uid = lora.get("uid")
                self.lora4.value = lora.get("value")
                self.lora4.rssi = lora.get("rssi")
                self.lora4.lastTs = lora.get("lastTs")
                self.lora4.batteryLevel = lora.get("batteryLevel")
                self.lora4.humidity = lora.get("humidity")
            except:
                self.lora4 = LoraPkg()
            
        temp = data.get("outputs")
        if temp != None:
            try:
                output = temp[0]
                self.output1.name = output.get("name")
                self.output1.id = output.get("id")
                self.output1.uuidWirelessSensor = output.get("uuidWirelessSensor")
                self.output1.value = output.get("value")
                self.output1.lastTs = output.get("lastTs")
                self.output1.schedule = output.get("schedule")
            except:
                self.output1 = OutputPkg()
            try:
                output = temp[1]
                self.output2.name = output.get("name")
                self.output2.id = output.get("id")
                self.output2.uuidWirelessSensor = output.get("uuidWirelessSensor")
                self.output2.value = output.get("value")
                self.output2.lastTs = output.get("lastTs")
                self.output2.schedule = output.get("schedule")
            except:
                self.output2 = OutputPkg()
            try:
                output = temp[2]
                self.output3.name = output.get("name")
                self.output3.id = output.get("id")
                self.output3.uuidWirelessSensor = output.get("uuidWirelessSensor")
                self.output3.value = output.get("value")
                self.output3.lastTs = output.get("lastTs")
                self.output3.schedule = output.get("schedule")
            except:
                self.output3 = OutputPkg()
            try:
                output = temp[3]
                self.output4.name = output.get("name")
                self.output4.id = output.get("id")
                self.output4.uuidWirelessSensor = output.get("uuidWirelessSensor")
                self.output4.value = output.get("value")
                self.output4.lastTs = output.get("lastTs")
                self.output4.schedule = output.get("schedule")
            except:
                self.output4 = OutputPkg()
                
        temp = data.get("sensors")
        if temp != None:
            try:
                sensor = temp[0]
                self.sensor1.type = sensor.get("type")
                self.sensor1.uuid = sensor.get("uuid")
                self.sensor1.value = sensor.get("value")
                self.sensor1.lastTs = sensor.get("lastTs")
            except:
                self.sensor1 = SensorPkg()
            try:
                sensor = temp[1]
                self.sensor2.type = sensor.get("type")
                self.sensor2.uuid = sensor.get("uuid")
                self.sensor2.value = sensor.get("value")
                self.sensor2.lastTs = sensor.get("lastTs")
            except:
                self.sensor2 = SensorPkg()
            try:
                sensor = temp[2]
                self.sensor3.type = sensor.get("type")
                self.sensor3.uuid = sensor.get("uuid")
                self.sensor3.value = sensor.get("value")
                self.sensor3.lastTs = sensor.get("lastTs")
            except:
                self.sensor3 = SensorPkg()
            try:
                sensor = temp[3]
                self.sensor4.type = sensor.get("type")
                self.sensor4.uuid = sensor.get("uuid")
                self.sensor4.value = sensor.get("value")
                self.sensor4.lastTs = sensor.get("lastTs")
            except:
                self.sensor4 = SensorPkg()


    def check_last(self):
        try:
            with open("data.json", "r", encoding='utf-8') as f:
                data = f.read()
                self.update_last(ujson.loads(data))
        except:
            with open("data.json", "w", encoding='utf-8') as f:
                ujson.dump(self.default_pkg, f)
            
            
    def add_lora(self, name, uid):
        if self.lora1.uid == None:
            self.lora1.name = name
            self.lora1.uid = uid
        elif self.lora2.uid == None:
            self.lora2.name = name
            self.lora2.uid = uid
        elif self.lora3.uid == None:
            self.lora3.name = name
            self.lora3.uid = uid
        elif self.lora4.uid == None:
            self.lora4.name = name
            self.lora4.uid = uid
        self.convert_to_pkg()
    
    def delete_lora(self, uid):
        if uid == self.lora1.uid:
            self.lora1 = LoraPkg()
        elif uid == self.lora2.uid:
            self.lora2 = LoraPkg()
        elif uid == self.lora3.uid:
            self.lora3 = LoraPkg()
        elif uid == self.lora4.uid:
            self.lora4 = LoraPkg()
        self.convert_to_pkg()

    def update(self, data):
        temp = data.get("wirelessSensors")
        if temp != None:
            for each in temp:
                uid = each.get("uid")
                if uid == self.lora1.uid:
                    self.lora1.name = each.get("name")
                elif uid == self.lora2.uid:
                    self.lora2.name = each.get("name")
                elif uid == self.lora3.uid:
                    self.lora3.name = each.get("name")
                elif uid == self.lora4.uid:
                    self.lora4.name = each.get("name")
                
        temp = data.get("outputs")
        if temp != None:
            for each in temp:
                id = each.get("id")
                if id == self.output1.id:
                    self.output1.name = each.get("name")
                    self.output1.uuidWirelessSensor = each.get("uuidWirelessSensor")
                    self.output1.schedule = each.get("schedule")
                elif id == self.output2.id:
                    self.output2.name = each.get("name")
                    self.output2.uuidWirelessSensor = each.get("uuidWirelessSensor")
                    self.output2.schedule = each.get("schedule")
                elif id == self.output3.id:
                    self.output3.name = each.get("name")
                    self.output3.uuidWirelessSensor = each.get("uuidWirelessSensor")
                    self.output3.schedule = each.get("schedule")
                elif id == self.output4.id:
                    self.output4.name = each.get("name")
                    self.output4.uuidWirelessSensor = each.get("uuidWirelessSensor")
                    self.output4.schedule = each.get("schedule")
        
        #!FIXME types? sensors?
#         temp = data.get("sensors")
#         if temp != None:
#             for each in temp:
#                 uuid = each.get("uuid")
#                 if uuid == self.sensor1.uuid:
#                     self.sensor1.type = each.get("type")
#                 elif uuid == self.sensor2.uuid:
#                     self.sensor2.type = each.get("type")
#                 elif uuid == self.sensor3.uuid:
#                     self.sensor3.type = each.get("type")
#                 elif uuid == self.sensor4.uuid:
#                     self.sensor4.type = each.get("type")
        self.convert_to_pkg()


    def convert_to_pkg(self):
        jsonpkg = {}
        jsonpkg["rssi"] = self.rssi
        jsonpkg["humidity"] = self.humidity
        jsonpkg["temperature"] = self.temperature
        
        loras = []
        if self.lora1.uid != None:
            lora1 = { "rssi": self.lora1.rssi, "name": self.lora1.name, "lastTs": self.lora1.lastTs,
                      "uid": self.lora1.uid, "batteryLevel": self.lora1.batteryLevel, "humidity": self.lora1.humidity }
            loras.append(lora1)
        if self.lora2.uid != None:
            lora2 = { "rssi": self.lora2.rssi, "name": self.lora2.name, "lastTs": self.lora2.lastTs,
                      "uid": self.lora2.uid, "batteryLevel": self.lora2.batteryLevel, "humidity": self.lora2.humidity }
            loras.append(lora2)
        if self.lora3.uid != None:
            lora3 = { "rssi": self.lora3.rssi, "name": self.lora3.name, "lastTs": self.lora3.lastTs,
                      "uid": self.lora3.uid, "batteryLevel": self.lora3.batteryLevel, "humidity": self.lora3.humidity }
            loras.append(lora3)
        if self.lora4.uid != None:
            lora4 = { "rssi": self.lora4.rssi, "name": self.lora4.name, "lastTs": self.lora4.lastTs,
                      "uid": self.lora4.uid, "batteryLevel": self.lora4.batteryLevel, "humidity": self.lora4.humidity }
            loras.append(lora4)
        jsonpkg["wirelessSensors"] = loras
        
        sensors = []
        if self.sensor1.type != None:
            sensor1 = { "type": self.sensor1.type, "uuid": self.sensor1.uuid, "value": self.sensor1.value, "lastTs": self.sensor1.lastTs }
            sensors.append(sensor1)
        if self.sensor2.type != None:
            sensor2 = { "type": self.sensor2.type, "uuid": self.sensor2.uuid, "value": self.sensor2.value, "lastTs": self.sensor2.lastTs }
            sensors.append(sensor2)
        if self.sensor3.type != None:
            sensor3 = { "type": self.sensor3.type, "uuid": self.sensor3.uuid, "value": self.sensor3.value, "lastTs": self.sensor3.lastTs }
            sensors.append(sensor3)
        if self.sensor4.type != None:
            sensor4 = { "type": self.sensor4.type, "uuid": self.sensor4.uuid, "value": self.sensor4.value, "lastTs": self.sensor4.lastTs }
            sensors.append(sensor4)
        jsonpkg["sensors"] = sensors
        
        outputs = []
        if self.output1.name != None:
            output1 = { "name": self.output1.name, "value": self.output1.value, "lastTs": self.output1.lastTs, "id": self.output1.id,
                        "uuidWirelessSensor": self.output1.uuidWirelessSensor, "schedule": self.output1.schedule }
            outputs.append(output1)
        if self.output2.name != None:
            output2 = { "name": self.output2.name, "value": self.output2.value, "lastTs": self.output2.lastTs, "id": self.output2.id,
                        "uuidWirelessSensor": self.output2.uuidWirelessSensor, "schedule": self.output2.schedule }
            outputs.append(output2)
        if self.output3.name != None:
            output3 = { "name": self.output3.name, "value": self.output3.value, "lastTs": self.output3.lastTs, "id": self.output3.id,
                        "uuidWirelessSensor": self.output3.uuidWirelessSensor, "schedule": self.output3.schedule }
            outputs.append(output3)
        if self.output4.name != None:
            output4 = { "name": self.output4.name, "value": self.output4.value, "lastTs": self.output4.lastTs, "id": self.output4.id,
                        "uuidWirelessSensor": self.output4.uuidWirelessSensor, "schedule": self.output4.schedule }
            outputs.append(output4)
        jsonpkg["outputs"] = outputs
        #save_to_file(jsonpkg)
        return(ujson.dumps(jsonpkg))
        
    def save_to_file(data):
        with open("data.json", "w", encoding='utf-8') as f:
            ujson.dump(data, f)   

# master = MasterDevice()
# print(master.convert_to_pkg())



# def jsonpkg(time_utc):
#     #return ujson.dumps(         
#     return (
time_utc = 123
test = {
  "rssi": random.randint(0,100),
  "humidity": random.randint(0,100),
  "temperature": random.randint(0,100),
  "sensors": [
    {
      "type": "sensor1",
      "uuid": "d1baf02e-82dc-11ee-8aa5-00155d2572d2",
      "value": random.randint(0,100),
      "lastTs": time_utc
    },
    {
      "type": "sensor2",
      "uuid": "d1bah02e-82dc-11ee-8aa5-00155d2572d2",
      "value": random.randint(0,100),
      "lastTs": time_utc
    }
  ],
  
  "outputs": [
    {
      "name": "output1",
      "value": True,
      "lastTs": time_utc,
      "id": 2,
      "uuidWirelessSensor": "dc75f108-82dc-11ee-8911-00155d2572d2",
      "schedule": {
        "startTs": 45345345,
        "endTs": 654645646
      }
    }, 
    {
      "name": "output2",
      "value": False,
      "lastTs": time_utc,
      "id": 1,
      "uuidWirelessSensor": "dc75f108-82dc-11ee-8911-00155d2572d2",
      "schedule": {
        "startTs": 45345345,
        "endTs": 654645646
      }    
    }
  ],
  
  "wirelessSensors": [
    {
      "rssi": random.randint(-100,100),
      "name": "lora1",
      "lastTs": time_utc,
      "uid": "dc75f108-82dc-11ee-8911-00155d2572d2",
      "batteryLevel": random.randint(0,100),
      "humidity": random.randint(0,100)
    },
    
    {
      "rssi": random.randint(-100,100),
      "name": "lora2",
      "lastTs": time_utc,
      "uid": "dc75f108-82dc-11ee-8911-00155d2572d3",
      "batteryLevel": random.randint(0,100),
      "humidity": random.randint(0,100)
    }
  ]
}
        
# with open("data.json", "w", encoding='utf-8') as f:
#     ujson.dump(test, f)        
# )