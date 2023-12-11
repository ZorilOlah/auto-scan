# %%
import requests
from selenium import webdriver
from deepdiff import DeepDiff
from typing import List

class VehicleStock:
    def __init__(self):
        self.brands_overview_api = "https://auto-abonnement.centraalbeheer.nl/api/v1/VehicleCluster?Filters.Segment=Cars&Filters.IncludeTaxInPrices=false&Filters.MaxPricePerMonth=1200&Filters.NumberOfKmPerMonth=1000&Filters.IncludeMileageCostsInPricing=true&Filters.IncludeFuelCostsInPricing=false"
        
        self.vehicles = None
        self.stock_changes = None

        self.initiate_stock()

    def get_vehicle_stock(self) -> dict:
        response = requests.get(self.brands_overview_api)
        if response.status_code == 200:
            return response.json()
            # Now you can process the data as needed
        else:
            return print("Failed to retrieve data:", response.status_code)

    def extract_modelmake_from_raw_vehicle_stock(self) -> List:
        raw_vehicles_data = self.get_vehicle_stock()
        vehicles = [{'brand': vehicle['make'], 'model' : vehicle['model']} for vehicle in raw_vehicles_data]
        return vehicles
    
    def check_changes_stock(self):
        vehicles = self.extract_modelmake_from_raw_vehicle_stock()
        differences = DeepDiff(vehicles, self.vehicles)
        if differences == {}:
            return 'No Changes In Stock'
        else:
            self.vehicles = vehicles
            return differences

    def initiate_stock(self):
        self.vehicles = self.extract_modelmake_from_raw_vehicle_stock()
        print(f'Stock iniated with : {self.vehicles}')

    def update_stock(self):
        stock_state = self.check_changes_stock()
        print(stock_state)

vehicles = VehicleStock()

vehicles.update_stock()

# %%
