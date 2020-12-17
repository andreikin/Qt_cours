import yaml

data = {}
data["fild size"] = [
            ["small", 10, 10],
            ["medium", 30, 30],
            ["large", 100, 200],
            ["super large", 500, 1000]
            ]

# data = [data, 5, 8, 6, 3]


# stream = file('configuration.yaml', 'w')
# yaml.dump(data, stream)



with open('configuration.yaml', 'w') as file:
    yaml.dump(data, file)
#     raw_data = file.read()

print (yaml.dump({'name': 'Silenthand Olleander', 'race': 'Human', 'traits': ['ONE_HAND', 'ONE_EYE']}))