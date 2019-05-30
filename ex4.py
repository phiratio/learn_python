cars = 100
space_in_a_car = 4.0
drivers = 30
passengers = 90
cars_not_driven = cars - drivers #100 - 30
cars_driven = drivers #30
carpool_capacity = cars_driven * space_in_a_car # 30 * 4.0
average_passengers_per_car = passengers / cars_driven # 90 / 30

print 'cars',cars
print 'drivers',drivers
print 'cars_not_driven',cars_not_driven
print '120.0',carpool_capacity
print '90', passengers
print '3', average_passengers_per_car
