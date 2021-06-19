#Question: Easy
"""
Design a parking system for a parking lot. The parking lot has three kinds of parking spaces: big, medium, and small, with a fixed number of slots for each size.

Implement the ParkingSystem class:

ParkingSystem(int big, int medium, int small) Initializes object of the ParkingSystem class. The number of slots for each parking space are given as part of the constructor.
bool addCar(int carType) Checks whether there is a parking space of carType for the car that wants to get into the parking lot. carType can be of three kinds: big, medium, or small, which are represented by 1, 2, and 3 respectively. A car can only park in a parking space of its carType. If there is no space available, return false, else park the car in that size space and return true.
"""
import logging
class ParkingSystem:
    def __init__(self, big: int, medium: int, small: int):
        self.big_space = big
        self.medium_space = medium
        self.small_space = small

    @property
    def big(self):
        if self.big_space > 0:
            self.big_space -= 1
        return bool(self.big_space)

    @property
    def medium(self):
        if self.medium_space > 0:
            self.medium_space -=1
        return bool(self.medium_space)

    @property
    def small(self):
        if self.small_space >0:
            self.small_space -=1
        return bool(self.small_space)

    def __bool__(self, value):
        '''
        Args:
            value (int):

        Returns:
            (bool): True if >=0 else False
        '''
        if value >= 0:
            return True
        else:
            return False

    def addCar(self, carType: int) -> bool:
        """
        Implement switch case in python
        Args:
            carType (int): type of car

        Returns:
            (bool): True is there is a slot else False
        """
        # def big():
        #     self.big -=1
        #     return bool(self.big)
        #
        # def medium():
        #     self.medium -=1
        #     return self.__bool__(self.medium)
        #
        # def small():
        #     self.small -=1
        #     return self.__bool__(self.small)

        car_type ={
            1: self.big,
            2: self.medium,
            3: self.small
        }

        return car_type.get(carType, 'Invalid')


# Your ParkingSystem object will be instantiated and called as such:
# obj = ParkingSystem(big, medium, small)
# param_1 = obj.addCar(carType)



if __name__ == '__main__':
    format = '%(asctime)s: %(message)s'
    logging.basicConfig(format=format, level=logging.INFO, datefmt='%H:%M:%S')
    #logging.getLogger().setLevel(logging.DEBUG)
    parking= ParkingSystem(big=1, medium=1, small=0)
    logging.info(f'{parking.addCar(1)}')
    logging.info(f'{parking.addCar(2)}')
    logging.info(f'{parking.addCar(3)}')
    logging.info(f'{parking.addCar(1)}')