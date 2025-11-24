# DICTIONARY OPERATIONS AND METHODS: ACCESSING, UPDATING, .GET(), .KEYS(), AND .VALUES()

# ASSIGNMENT AND COPYING

# Creating a dictionary
model_params = {'layers': 24, 'units': 512, 'activation': 'relu'}

# Assigning the same dictionary reference to another variable (not a copy)
shared_params = model_params    # Both variables point to the same dictionary

model_params['activation'] = 'gelu'
# print(model_params)
# print(shared_params)

# model_params.clear()
# print(model_params)
# print(shared_params)

safe_params = model_params.copy()
print(model_params)
print(safe_params)

model_params.clear()
print(model_params)
print(safe_params)

# MERGING DICTIONARIES WITH update()
base_config = {'batch_size': 32, 'epochs': 10}
version_config = {'learning_rate': 0.001, 'units': 128, 'epochs': 20}
base_config.update(version_config)

print(base_config)
print(version_config)

# DICTIONARY VIEWS WITH .keys(), .values(), AND .items()

# Get all keys from base_config
print(base_config.keys())

# Get all values from base_config
print(base_config.values())

print(base_config.items())

# ITERATING OVER KEYS, VALUES, AND ITEMS

for key in base_config.keys():
    print(f'key => {key}')

for value in base_config.values():
    print(f'Value => {value}')

for dict_key, dict_value in base_config.items():
    print(f'{dict_key} => {dict_value}')

# TESTING MEMBERSHIP USING in

print('batch_size' in base_config.keys())
print(32 in base_config.values())
print(('batch_size', 32) in base_config.items())





