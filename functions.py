import pandas as pd
import numpy as np
import reverse_geocoder as rg

def get_countries(homes):
    right_way = [(row[1], row[0]) for row in homes.values]
    results = rg.search(right_way)
    print(results)
    return [row["cc"] for row in results]


def load_data(social_network="Gowalla"):

    names_edges = ["from_id", "to_id"]
    names_checkins = ["user_id", "checkin_time", "latitude",
                        "longitude", "location_id"]

    # load them into dfs
    edges = pd.read_table(social_network + "_edges.txt",
        names=names_edges).dropna()
    checkins = pd.read_table(social_network + "_totalCheckins.txt",
        names=names_checkins).dropna()

    return checkins, edges

def discretize_checkins(checkins, km_to_degrees=.22522522522):
    checkins[["disc_tuple"]] = ((checkins[["latitude", "longitude"]] / km_to_degrees).astype('int') * km_to_degrees).apply(tuple, axis=1)
    return checkins

def get_home_locations(checkins):
    most_frequent_cell_by_user = checkins.groupby("user_id")[["disc_tuple"]].agg(lambda x:x.value_counts().index[0])

    home_checkins = pd.merge(checkins, most_frequent_cell_by_user, how='inner', on=['user_id', 'disc_tuple'])

    return home_checkins.groupby("user_id")[["longitude", "latitude"]].agg([np.mean])
