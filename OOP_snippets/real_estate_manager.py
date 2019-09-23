def get_valid_input(input_string, valid_options):
    input_string += "({})".format(", ".join(valid_options))
    response = input(input_string)
    while response.lower() not in valid_options:
        response = input(input_string)
    return response


class Property:
    def __init__(self, square_feet='', beds='', baths='', **kwargs):
        super().__init__(**kwargs)
        self.square_feet = square_feet
        self.num_bedrooms = beds
        self.num_baths = baths

    def display(self):
        print(f'''
Property details
----------------
square footage: {self.square_feet}
bedrooms: {self.num_bedrooms}
bathrooms: {self.num_baths}
''')

    @staticmethod
    def prompt_init():
        return dict(square_feet=input('Enter the square feet: '),
                    beds=input('Enter number of bedrooms:'),
                    baths=input('Enter number of baths'))


class Apartment(Property):
    valid_laundries = ('coin', 'ensuite', 'none')
    valid_balconies = ('yes', 'no', 'laundry')

    def __init__(self, balcony='', laundry='', **kwargs):
        super().__init__(**kwargs)
        self.balcony = balcony
        self.laundry = laundry

    def display(self):
        super.display()
        print(f'''
APARTMENT DETAILS
-----------------
laundry: {self.laundry}
has balcony: {self.balcony}
''')

    @staticmethod
    def prompt_init():
        parent_init = Property.prompt_init()
        laundry = get_valid_input('What laundry facilities does the property have?', Apartment.valid_laundries)
        balcony = get_valid_input('Does the property have a balcony?', Apartment.valid_balconies)
        parent_init.update({
            'laundry': laundry,
            'balcony': balcony
        })
        return parent_init


class House(Property):
    valid_garage = ('attached', 'detached', 'none')
    valid_fenced = ('yes', 'no')

    def __init__(self, num_stories='', garage='', fenced='', **kwargs):
        super().__init__(**kwargs)
        self.garage = garage
        self.fenced = fenced
        self.num_stories = num_stories

    def display(self):
        super.display()
        print(f'''
HOUSE DETAILS
-------------
# of stories: {self.num_stories}
garage: {self.garage}
fenced yard: {self.fenced}
''')

    @staticmethod
    def prompt_init():
        parent_init = Property.prompt_init()
        fenced = get_valid_input('Is te yard fenced', House.valid_fenced)
        garage = get_valid_input('Is there a garage?', House.valid_garage)
        num_stories: input('How many stories: ')
        parent_init.update({
            'fenced': fenced,
            'garage': garage,
            'num_stories': num_stories
        })
        return parent_init


class Purchase:
    def __index__(self, price='', taxes='', **kwargs):
        super().__init__(**kwargs)
        self.price = price
        self.taxes = taxes

    def display(self):
        super().display()
        print(f'''
PURCHASE DETAILS
selling price: {self.price}
estimated taxes: {self.taxes}
''')

    @staticmethod
    def prompt_init():
        return dict(
            price=input('What is the selling price?'),
            taxes=input('What are the estimated taxes?')
        )


class Rental:
    def __init__(self, furnished='', utilities='', rent='', **kwargs):
        super().__init__(**kwargs)
        self.furnished = furnished
        self.rent = rent
        self.utilities = utilities

    def display(self):
        super().display()
        print(f'''
RENTAL DETAILS
rent: {self.rent}
estimated utilities cost: {self.utilities}
furnished: {self.furnished}
''')

    @staticmethod
    def prompt_init():
        return dict(
            rent=input('What is the monthly rent?'),
            utilities=input('What are the estimated utilities?'),
            furnished=get_valid_input('Is the property furnished', ('yes', 'no'))
        )


class HouseRental(Rental, House):  # order is important
    @staticmethod
    def prompt_init():
        init = House.prompt_init()
        init.update(Rental.prompt_init())
        return init


class ApartmentRental(Rental, Apartment):
    @staticmethod
    def prompt_init():
        init = Apartment.prompt_init()
        init.update(Rental.prompt_init())
        return init


class ApartmentPurchase(Purchase, Apartment):
    @staticmethod
    def prompt_init():
        init = Apartment.prompt_init()
        init.update(Purchase.prompt_init())
        return init


class HousePurchase(Purchase, House):
    @staticmethod
    def prompt_init():
        init = House.prompt_init()
        init.update(Purchase.prompt_init())
        return init


class Agent:
    def __init__(self):
        self.property_list = []

    def display_properties(self):
        for propertyx in self.property_list:
            propertyx.display()

    type_map = {
        ('house', 'rental'): HouseRental,
        ('house', 'purchase'): HousePurchase,
        ('apartment', 'rental'): ApartmentRental,
        ('apartment', 'purchase'): ApartmentPurchase,
    }

    def add_property(self):
        property_type = get_valid_input('What type of property', ('house', 'apartment')).lower()
        payment_type = get_valid_input('What type of payment', ('purchase', 'rental')).lower()

        PropertyClass = self.type_map[(property_type, payment_type)]
        init_args = PropertyClass.prompt_init()
        self.property_list.append(PropertyClass(**init_args))
