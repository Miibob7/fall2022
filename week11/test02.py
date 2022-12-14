class Package:
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight
    def dropOff(self, driver): 
        print(f"Delivered {self.name} by {driver} weight {self.weight} pounds")
class AmazonTruck:
    packages = []
    driver = "nobody"

    def load(self, package):
        self.packages.append(package)  # add the package to the truck

    def deliver(self):
        for package in self.packages:
            package.dropOff(self.driver)

Phil = Package("Phil Swift", 200)
Jimmy = Package("Jimmy", -20)
flex = Package("FlexTape", 2)

truck = AmazonTruck()
truck.driver = "Jimmy"
truck.load(Phil)
truck.load(Jimmy)
truck.load(flex)

truck.deliver()