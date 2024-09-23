# Define the base class called Technology 
class Technology:
    brand = ''
    model = ''
    price = 10000
    color = 'black'

# Define the first child class called Phone, inheriting from Technology 
class Phone (Technology):
    camera_pixels = 'mb'
    serial_number = ''
    battery = 5000

# Define the second child class called Computer, inheriting from Technology 
class Computer (Technology):
    processor = '13th Gen Intel(R) Core(TM) i9'
    ram = 32
    system_type = '64-bit'


