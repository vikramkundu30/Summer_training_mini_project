class Vehicle:
    def __init__(self, vehicle_id, vehicle_type, base_rent, extra_km_rate):
        self.vehicle_id = vehicle_id
        self.vehicle_type = vehicle_type
        self.base_rent = base_rent
        self.extra_km_rate = extra_km_rate
        self.base_km_limit = 250
    def calculate_daily_rent(self, km_driven):
        if km_driven <= self.base_km_limit:
            return self.base_rent
        else:
            extra_km = km_driven - self.base_km_limit
            return self.base_rent + (extra_km * self.extra_km_rate)
class RentalSystem:
    def __init__(self):
        self.rented_vehicles = []
    def rent_vehicle(self, vehicle_obj, km_driven):
        rent_cost = vehicle_obj.calculate_daily_rent(km_driven)
        self.rented_vehicles.append({
            "id": vehicle_obj.vehicle_id,
            "type": vehicle_obj.vehicle_type,
            "km": km_driven,
            "cost": rent_cost
        })
        return rent_cost
    def generate_daily_report(self):
        print("\n" + "="*45)
        print("          DAILY VEHICLE RENTAL REPORT        ")
        print("="*45)
        print(f"{'ID':<8}{'Type':<10}{'KM Driven':<12}{'Rent (RS)':<10}")
        print("-"*45)
        total_revenue = 0
        vehicle_counts = {}
        for item in self.rented_vehicles:
            print(f"{item['id']:<8}{item['type']:<10}{item['km']:<12}{item['cost']:<10}")
            total_revenue += item['cost']
            vehicle_counts[item['type']] = vehicle_counts.get(item['type'], 0) + 1
        print("-"*45)
        print("Vehicle Count Summary:")
        for v_type, count in vehicle_counts.items():
            print(f" - Total {v_type}s Rented: {count}")         
        print("-"*45)
        print(f"TOTAL REVENUE COLLECTED PER DAY: RS {total_revenue}")
        print("="*45)
if __name__ == "__main__":
    bike_profile = Vehicle("B001", "Bike", base_rent=2000, extra_km_rate=5)
    car_profile  = Vehicle("C001", "Car",  base_rent=5000, extra_km_rate=12)
    bus_profile  = Vehicle("BUS1", "Bus",  base_rent=7500, extra_km_rate=20)
    system = RentalSystem()
    system.rent_vehicle(bike_profile, km_driven=300)  
    system.rent_vehicle(car_profile, km_driven=240)  
    system.rent_vehicle(bus_profile, km_driven=280)  
    system.rent_vehicle(bike_profile, km_driven=250) 
    system.generate_daily_report()
