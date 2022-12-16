class Package:
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight
    def dropOff(self, driver,truckNumber): 
        print(f"Delivered {self.name} weighting {self.weight} pounds by {driver} of truck {truckNumber}")
class AmazonTruck:
    packages = []
    driver = "nobody"
    truckNumber = "of truck"
    def load(self, package):
        self.packages.append(package)  # add the package to the truck

    def deliver(self):
        for package in self.packages:
            package.dropOff(self.driver,self.truckNumber)

Phil = Package("Phil Swift", 200)
Jimmy = Package("Jimmy", -20)
flex = Package("FlexTape", 2)

truck = AmazonTruck()
truck.driver = "Jimmy"
truck.truckNumber = "248-349-9101"
truck.load(Phil)
truck.load(Jimmy)
truck.load(flex)

truck.deliver()

