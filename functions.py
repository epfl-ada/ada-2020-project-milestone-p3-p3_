import pandas as pd
import numpy as np
import reverse_geocoder as rg
from obspy.geodetics import degrees2kilometers
from geopy.distance import distance

def get_countries(homes):
    right_way = [(row[1], row[0]) for row in homes.values]
    results = rg.search(right_way)
    print(results)
    return [row["cc"] for row in results]


def load_data(social_network="Gowalla"):

    names_edges = ["from_id", "to_id"]
    names_checkins = ["user_id", "checkin_time", "latitude",
                        "longitude", "location_id"]

    if social_network == "Brightkite":
        
        # load them into dfs
        edges = pd.read_table("./data/loc-brightkite_edges.txt.gz",
            names=names_edges).dropna()
        checkins = pd.read_table("./data/loc-brightkite_totalCheckins.txt.gz",
            names=names_checkins).dropna()
    if social_network == "Gowalla":
        edges = pd.read_table("./data/loc-gowalla_edges.txt.gz",
            names=names_edges).dropna()
        checkins = pd.read_table("./data/loc-gowalla_totalCheckins.txt.gz",
            names=names_checkins).dropna()
        
    # preprocess the data
    checkins = checkins[(checkins.latitude < 90) & (checkins.latitude > -90)]
    checkins = checkins.loc[~((checkins['latitude'] == 0) & (checkins['longitude'] == 0))]
        
    return checkins, edges

def discretize_checkins(checkins, km_to_degrees=.22522522522):
    checkins["disc_tuple"] = ((checkins[["latitude", "longitude"]] / km_to_degrees).astype('int') * km_to_degrees).apply(tuple, axis=1)
    return checkins

def get_home_locations(checkins):
    most_frequent_cell_by_user = checkins.groupby("user_id")[["disc_tuple"]].agg(lambda x:x.value_counts().index[0])

    home_checkins = pd.merge(checkins, most_frequent_cell_by_user, how='inner', on=['user_id', 'disc_tuple'])

    return home_checkins.groupby("user_id")[["longitude", "latitude"]].agg([np.mean])


def discretize_world(check_ins, km = 25):
    km_25 = km / degrees2kilometers(1)

    check_ins[['check_in_lat', 'check_in_long']] = check_ins.loc[:, ["latitude", "longitude"]].div(km_25, axis=1).astype('int').mul(km_25)
    check_ins['cell'] = check_ins.apply(lambda x: (x['check_in_lat'], x['check_in_long']), axis = 1)
    
    return check_ins

def home_locations(check_ins):
    loc_count = check_ins.groupby(by = ['user_id', 'cell'], as_index = False).count()
    most_checked_in_locations = loc_count.sort_values('latitude', ascending=False).drop_duplicates(['user_id']).sort_values('user_id').set_index('user_id')['cell']


    checkins_temp = check_ins.copy().set_index('user_id')
    home_locs = checkins_temp.merge(most_checked_in_locations, left_index = True, right_index = True)
    home_locs = home_locs[home_locs.cell_x == home_locs.cell_y].groupby('user_id')[['latitude','longitude']].agg('mean')
    home_locs['location'] = list(zip(home_locs.latitude, home_locs.longitude))
    
    return home_locs

def lives_in_city(homes, cities):
    # Create a huge dataframe with all cities per country to then check if a home location is close to a city
    merge = homes.merge(cities, left_on = 'country', right_on = 'iso2')
    merge['distance_to_city'] = merge.apply(lambda row: distance((row['latitude'], row['longitude']), (row['lat'],row['lng']) ).km, axis = 1)
    lives_urban = merge.groupby("user_id").apply(lambda x: (x['distance_to_city'] < x['radius']).any()).to_frame()
    lives_urban = lives_urban.rename(columns = {0:'lives_urban'})
    # Integrate the 'lives_urban' variable into the home location datasets
    homes = homes.merge(lives_urban, left_on = 'user_id', right_index = True)
    
    return homes



