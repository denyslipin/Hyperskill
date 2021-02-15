import json
import re

class EasyRiderBusCompany:
    def __init__(self):
        self.errors1 = {"bus_id": 0, "stop_id": 0, "stop_name": 0, 
                        "next_stop": 0, "stop_type": 0, "a_time": 0}
        self.errors2 = {"stop_name": 0, "stop_type": 0, "a_time": 0}
        self.errors3 = {}
        self.errors4 = {}
        self.stops = {}
        self.all_stops = {}
        self.bus_stops = {"start": [], "transfer": [], "finish": []}
    
    def stage1(self, bus_info_list):
        for bus_info in bus_info_list:
            if not isinstance(bus_info["bus_id"], int):
                self.errors1["bus_id"] += 1
            if not isinstance(bus_info["stop_id"], int):
                self.errors1["stop_id"] += 1   
            if not isinstance(bus_info["stop_name"], str) or bus_info["stop_name"] == "":
                self.errors1["stop_name"] += 1
            if not isinstance(bus_info["next_stop"], int) or bus_info["next_stop"] == "":
                self.errors1["next_stop"] += 1
            if not isinstance(bus_info["stop_type"], str) or len(bus_info["stop_type"]) > 1:
                self.errors1["stop_type"] += 1
            if not isinstance(bus_info["a_time"], str) or bus_info["a_time"] == "":
                self.errors1["a_time"] += 1
        print(f"Type and required field validation: {sum(self.errors.values())} errors")
        for k, v in self.errors1.items():
            print(k, v, sep=": ")

    def stage2(self, bus_info_list):
        for bus_info in bus_info_list: 
            if not re.match(r"^[A-Z].* [SABR][otv][urea][lend][eu]?[vte]?[a]?[r]?[d]??$", 
                            bus_info["stop_name"]):
                self.errors2["stop_name"] += 1
            if len(bus_info["stop_type"]) != 0 and not re.match(r"^[SOF]$", bus_info["stop_type"]):
                self.errors2["stop_type"] += 1
            if not re.match(r"[0-2][0-9]:[0-5][0-9]$", bus_info["a_time"]):
                self.errors2["a_time"] += 1
        print(f"Format validation: {sum(self.errors2.values())} errors")
        for k, v in self.errors2.items():
            print(k, v, sep=": ")
        
    def stage3(self, bus_info_list):
        for bus_info in bus_info_list:
            self.errors3[bus_info["bus_id"]] = self.errors3.get(bus_info["bus_id"], 0) + 1
        print("Line names and number of stops:")
        for k, v in self.errors3.items():
            print(f"bus_id: {k}, stops: {v}")
    
    def stage4(self, bus_info_list):
        for bus_info in bus_info_list:
            self.stops[bus_info["bus_id"]] = self.stops.get(bus_info["bus_id"], "") + bus_info["stop_type"]
        for k, v in self.stops.items():
            if "S" not in v or "F" not in v:
                print(f"There is no start or end stop for the line: {k}.")
        else:
            for bus_info in bus_info_list:
                if bus_info["stop_type"] == "S":
                    if bus_info["stop_name"] not in self.bus_stops["start"]:
                        self.bus_stops["start"].append(bus_info["stop_name"])
                if bus_info["stop_type"] == "F":
                    if bus_info["stop_name"] not in self.bus_stops["finish"]:
                        self.bus_stops["finish"].append(bus_info["stop_name"])
                self.all_stops[bus_info["stop_name"]] = self.all_stops.get(bus_info["stop_name"], 0) + 1
            for k, v in self.all_stops.items():
                if v > 1:
                    self.bus_stops["transfer"].append(k)
            s = sorted(self.bus_stops["start"])
            t = sorted(self.bus_stops["transfer"])
            f = sorted(self.bus_stops["finish"])
            print(f"Start stops: {len(s)} {s}")
            print(f"Transfer stops: {len(t)} {t}")
            print(f"Finish stops: {len(f)} {f}")
     
    def stage5(self, bus_info_list):
        for i in range(len(bus_info_list) - 1):
            if bus_info_list[i]["bus_id"] == bus_info_list[i + 1]["bus_id"]:
                if bus_info_list[i]["a_time"] > bus_info_list[i + 1]["a_time"]:
                    if bus_info_list[i + 1]["bus_id"] not in self.errors4:
                        self.errors4[bus_info_list[i + 1]["bus_id"]] = bus_info_list[i + 1]["stop_name"]
        print("Arrival time test:")
        if len(self.errors4) == 0:
            print("OK")
        else:
            for k, v in self.errors4.items():
                print(f"bus_id line {k}: wrong time on station {v}")
                
    def stage6(self, bus_info_list):
        bus_stops = []
        for bus_info in bus_info_list:
            if bus_info["stop_type"] == "S" or bus_info["stop_type"] == "F":
                if bus_info["stop_name"] not in bus_stops:
                    bus_stops.append(bus_info["stop_name"])
            self.all_stops[bus_info["stop_name"]] = self.all_stops.get(bus_info["stop_name"], 0) + 1
        for k, v in self.all_stops.items():
            if v > 1:
                bus_stops.append(k)
        print("On demand stops test:")
        demand_stops = []
        for bus_info in bus_info_list:
            if bus_info["stop_type"] == "O":
                if bus_info["stop_name"] in bus_stops:
                    demand_stops.append(bus_info["stop_name"])
        if len(demand_stops) == 0:
            print("OK")
        else:
            print(f"Wrong stop type: {sorted(demand_stops)}")
                    
bus = EasyRiderBusCompany()
bus.stage6(json.loads(input()))
