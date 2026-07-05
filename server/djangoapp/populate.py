from .models import CarMake, CarModel


def initiate():
    car_make_data = [
        {"name": "NISSAN", "description": "Great cars. Japanese technology"},
        {"name": "Mercedes", "description": "Great cars. German technology"},
        {"name": "Audi", "description": "Great cars. German technology"},
        {"name": "Kia", "description": "Great cars. Korean technology"},
        {"name": "Toyota", "description": "Great cars. Japanese technology"},
    ]

    car_make_instances = []
    for data in car_make_data:
        car_make_instances.append(
            CarMake.objects.create(
                name=data["name"],
                description=data["description"],
            )
        )

    # Create CarModel instances with the corresponding CarMake instances
    car_model_data = [
        ("Pathfinder", "SUV", 0),
        ("Qashqai", "SUV", 0),
        ("XTRAIL", "SUV", 0),
        ("A-Class", "SUV", 1),
        ("C-Class", "SUV", 1),
        ("E-Class", "SUV", 1),
        ("A4", "SUV", 2),
        ("A5", "SUV", 2),
        ("A6", "SUV", 2),
        ("Sorrento", "SUV", 3),
        ("Carnival", "SUV", 3),
        ("Cerato", "Sedan", 3),
        ("Corolla", "Sedan", 4),
        ("Camry", "Sedan", 4),
        ("Kluger", "SUV", 4),
        # Add more CarModel instances as needed
    ]

    for name, car_type, car_make_index in car_model_data:
        CarModel.objects.create(
            name=name,
            car_make=car_make_instances[car_make_index],
            type=car_type,
            year=2023,
        )
