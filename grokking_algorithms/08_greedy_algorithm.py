
#   传入一个数组，并转化为一集合
states_needed = set(["mt", "wa", "or", "id", "nv", "ut", "ca", "az"])

stations = {}
stations['kone']  = set(["id", "nv", "ut"])
stations["ktwo"] = set(["wa", "id", "mt"])
stations["kthree"] = set(["or", "nv", "ca"])
stations["kfour"] = set(["nv", "ut"])
stations["kfive"] = set(["ca", "az"])

final_stations = set()

while states_needed:
    best_station  = None
    state_covered = set()
    for station, states in stations.items():
        covered = states_needed & states
        # print(covered)

        if len(covered) > len(state_covered):
            best_station = station
            state_covered = covered
    print(best_station)


    states_needed -= state_covered
    final_stations.add(best_station)
# print(final_stations)
