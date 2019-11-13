from Chapter3.c3_22_house import House
from Chapter3.c3_23_purchase_and_rental import Rental


class HouseRental(Rental, House):
    def prompt_init():
        init = House.prompt_init()
        init.update(Rental.prompt_init())
        return init

    prompt_init = staticmethod(prompt_init)
