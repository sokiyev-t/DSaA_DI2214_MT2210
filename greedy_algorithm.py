states_needed =set( [ "mt", "wa", "or", "id", "nv", "ut", "са", "az"] )
stations = {}
stations["kone"]= set(["id", "nv", "ut"])
stations["ktwo"] =set(["wa", "id", "mt"])
stations["kthree"] = set(["or", "nv", "са"])
stations["kfour"] =set(["nv", "ut"])
stations["kfive"] = set(["ca", "az"])

final_stations=set()

while states_needed:
    best_station = None
    states_covered = set()
    for station, states in stations.items():
        covered = states_needed &states
        if len(covered) > len(states_covered):
            best_station = station
            states_covered = covered
    states_needed -= states_covered
    final_stations.add(best_station)
    stations.pop(best_station)

print(final_stations)

# arr=[4,5,6,78,1,89,0,12]
# m=arr[0]
# ind=0
# for i in range(len(arr)):
#     if arr[i]>m:
#         ind=i
#         m=arr[i]
# print(m, ind)

