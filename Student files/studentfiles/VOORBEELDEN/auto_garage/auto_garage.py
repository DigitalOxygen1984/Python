class Garage():
    def bepaalOnderhoud(self, auto):
        if auto.kilometerstand > 60000:
            print('grote beurt nodig')    
        else:
            print('geen beurt nodig')        