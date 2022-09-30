class Capitalize():
    def __init__(self, capThis:str):
        self.capThis = capThis
        self.capped = []
        
    def set(self):
        capThis = self.capThis
        return capThis
    
    def get(self):
        return self.capThis
    
    def update(self, newCap:str):
         self.capThis = newCap
         return self.capThis
    
    def make(self, content2Cap:str):
        split = content2Cap.lower().split()
        template = []
        for item in split:
            capped = item.replace(item[0], item[0].upper())
            template.append(capped)
        result = " ".join(template)
        output = self.capped.append(result)
        return output
    
    def display(self):
        displayThis = self.capped
        for cap in displayThis:
            print(f"🧢: {cap}")
        return 0
            
    def output(self):
        caps = self.capped
        with open("caps.txt", "w+") as file:
            for cap in caps:
                file.write(f"{cap}\n")
        return 0
    