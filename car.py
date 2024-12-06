class car:
    def __init__(self,model,color,company):
        self.model=model
        self.color = color
        self.company = company
    
    def dispaly_info(self):
        print(f"{self.model} {self.color} {self.company}")
    
my_car = car("i7","grey","BMW")
my_car.dispaly_info()