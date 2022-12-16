class Package:
    def __init__(self, name):
        self.name = name
    def dropOff(self, driver): 
        print(f"Delivered {self.name} by {driver}")
class AmazonTruck:
    packages = []
    driver = "nobody"

    def load(self, package):
        self.packages.append(package)  # add the package to the truck

    def deliver(self):
        for package in self.packages:
            package.dropOff(self.driver)

Phil = Package("Phil Swift weighing 9 lbs")
Jimmy = Package("Jimmy weighing 9 lbs")
flex = Package("FlexTape weighing 9 lbs")

truck = AmazonTruck()
truck.driver = "Jimmy of truck 589"
truck.load(Phil)
truck.load(Jimmy)
truck.load(flex)

truck.deliver()