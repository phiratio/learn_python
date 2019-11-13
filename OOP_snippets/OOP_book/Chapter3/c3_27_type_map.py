from Chapter3.c3_24_house_rental import HouseRental
from Chapter3.c3_25_remaining_subclasses import HousePurchase, ApartmentRental, ApartmentPurchase


class Agent:
    type_map = {
        ("house", "rental"): HouseRental,
        ("house", "purchase"): HousePurchase,
        ("apartment", "rental"): ApartmentRental,
        ("apartment", "purchase"): ApartmentPurchase
    }

    def __init__(self):
        self.property_list = []

    def display_properties(self):
        for property in self.property_list:
            property.display()
