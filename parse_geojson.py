import json
# file_path = './data/beijing_building.geojson'
file_path = './data/out.geojson'

def save_json_to_file(json_obj):
    json_str = json.dumps(json_obj)
    with open('./data/out.geojson', 'w') as f:
        f.write(json_str)

def regenerate_json_data(min_x, min_y, max_x, max_y, source_data):
    for item in source_data['features']:
        coordinates = item['geometry']['coordinates'][0][0]
        for coordinate in coordinates:
            coordinate[0] -= min_x
            coordinate[1] -= min_y
    save_json_to_file(source_data)

def parse_data(data):
    min_x = -1
    min_y = -1
    max_x = -1
    max_y = -1
    json_obj = json.loads(data)
    for item in json_obj['features']:
        coordinates = item['geometry']['coordinates'][0][0]
        # print(coordinates)
        for coordinate in coordinates:
            x = coordinate[0]
            y = coordinate[1]
            if (min_x < 0 or x < min_x): 
                min_x = x
            if (min_y < 0 or y < min_y): 
                min_y = y
            if (max_x < 0 or x > max_x): 
                max_x = x 
            if (max_y < 0 or y > max_y): 
                max_y = y
    x_diff = max_x - min_x
    y_diff = max_y - min_y
    print('min_x: ', min_x, 'min_y: ', min_y, 'max_x: ', max_x, 'max_y: ', max_y, 'x_diff: ', x_diff, 'y_diff: ', y_diff)
    # regenerate_json_data(min_x, min_y, max_x, min_y, json_obj)



with open (file_path) as f:
    data = f.read()
    parse_data(data)

