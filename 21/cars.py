cars = {
    'Ford': ['Falcon', 'Focus', 'Festiva', 'Fairlane'],
    'Holden': ['Commodore', 'Captiva', 'Barina', 'Trailblazer'],
    'Nissan': ['Maxima', 'Pulsar', '350Z', 'Navara'],
    'Honda': ['Civic', 'Accord', 'Odyssey', 'Jazz'],
    'Jeep': ['Grand Cherokee', 'Cherokee', 'Trailhawk', 'Trackhawk']
}


def get_all_jeeps(cars=cars):
    """return a comma  + space (', ') separated string of jeep models
       (original order)"""
    return ', '.join(cars['Jeep'])


def get_first_model_each_manufacturer(cars=cars):
    """return a list of matching models (original ordering)"""
    return [model[0] for car, model in cars.items()]


def get_all_matching_models(cars=cars, grep='trail'):
    """return a list of all models containing the case insensitive
       'grep' string which defaults to 'trail' for this exercise,
       sort the resulting sequence alphabetically"""
    lst = []
    for car, models in cars.items():
        for model in models:
            if grep.lower() in model.lower():
                lst.append(model)
    lst.sort()
    return lst


def sort_car_models(cars=cars):
    """return a copy of the cars dict with the car models (values)
       sorted alphabetically"""
    sorted_cars = cars.copy()

    for car in sorted_cars.keys():
        sorted_cars[car].sort()

    return sorted_cars
