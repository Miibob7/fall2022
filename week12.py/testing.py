if prefix in item:
    yield item
    change this with
    it item.startwith(prefix):



    #other notes
    def petgenerator():
    yield "fluff"
    yield "mom"
    yield "amongus"
for pet in petgenerator():
    print(pet)