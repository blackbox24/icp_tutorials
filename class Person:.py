from datetime import datetime
class Person:
    _id:int
    addres:str
    name:str

    def __init__(self,address:str,name:str):
        self.address = address
        self.name = name

class Crop:
    _id:int
    name:str
    price:float
    amount:int
    owner:object
    createdAt:str
    updatedAt:str

    def __init__(self,_id:int,name:str,price:float,owner:object,amount:int=0,createdAt:str=datetime.now(),updatedAt:str=datetime.now()):
        self._id = id
        self.name = name
        self.price = price
        self.amount = amount
        self.owner = owner
        self.createdAt = createdAt
        self.updatedAt = updatedAt
    
    def save(self):
        pass
    

class Payment:
    _id:int
    _to:str
    _from:str
    amount:float
    quantity:int
    crop: object
    createdAt:str
    updatedAt:str

    def __init__(self,_id:int,_to:str,_from:str,amount:float,quantity:int,crop:object,createdAt:str=datetime.now(),updatedAt:str=datetime.now()):
        self._id = _id
        self._to = _to
        self._from = _from
        self.quantity = quantity
        self.crop = crop
        self.createdAt = createdAt
        self.updatedAt = updatedAt
    
    # validate payment

    def save(self):
        pass

crops = []
payments = []
persons = []
OWNER = ""

def auto_generate_id(model):
    n_obj = len(model())
    return n_obj 

def login(name,address):
    id = auto_generate_id()
    OWNER = Person(_id=id,address=address,name=name)
    return True

def lookup_id(_id,models):
    try:
        for model in models:
            if model._id == _id:
                return model
    except:
        print("Error error while searching for id")

    return [];

# CRUD FOR CROPS
def get_crop(_id):
    crop = lookup_id(_id,crops)
    if crop == []:
        return "No crops found"
    return crop

def all_crops():
    return crops

def add_crop(name,price,amount,owner):
    n_crops = len(all_crops())
    owner = Person()
    crop = Crop(
        _id=n_crops,
        name=name,
        price=price,
        amount=amount,
        owner=OWNER
    )

def update_crop(_id,name,price,amount):
    crop = lookup_id(_id,crops)
    crop.name = name
    crop.price = price
    crop.amount = amount
    return "Update Successful"

def delete(_id):
    crop = lookup_id(_id,crops)
    crops.remove(crop)
    return "Deletion Successful"

def pay_for_crop(_id,amount):
    crop = lookup_id(_id,crops)
    # person must be registered
    # check buyers token if it is enough