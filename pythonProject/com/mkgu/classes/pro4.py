class Showroom:
    company = 'Maruti Suzuki'
    location = 'Bengaluru'

    def car_attributes(self, carmodel, carcolor, carprice, carvariant):
        self.carmodel = carmodel
        self.carcolor = carcolor
        self.carprice = carprice
        self.carvariant = carvariant

    def car_details(self):
        print('Company : ',self.company)
        print('Location : ',self.location)
        print('Car model : ', self.carmodel)
        print('Car price : ', self.carprice)
        print('Car variant : ', self.carvariant)
        return 'Car color : {}'.format(self.carcolor)

carmodel=input('Enter the car model : ')
carprice=input('Enter the car price : ')
carvariant=input('Enter the car variant : ')
carcolor=input('Enter the car color : ')

showroom_obj = Showroom()
showroom_obj.car_attributes(carmodel, carcolor, carprice, carvariant)
print('The Car details are : ')
print(showroom_obj.car_details())