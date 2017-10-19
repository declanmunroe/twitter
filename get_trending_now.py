from auth import get_api

api = get_api()


GLA_WOE_ID = 21125
LON_WOE_ID = 44418

gla_trends = api.trends_place(GLA_WOE_ID)
lon_trends = api.trends_place(LON_WOE_ID)

gla_trends_set = set([trend['name']
    for trend in gla_trends[0]['trends']])
 
lon_trends_set = set([trend['name']
    for trend in lon_trends[0]['trends']])
    
common_trends = set.intersection(gla_trends_set, lon_trends_set)

print(common_trends)