class Vehicle:
    def __init__(self, brand, size, num_wheels):
        self.brand = brand
        self._size = size
        self._num_wheels = num_wheels

    def display_info(self):
        return f"{self.brand} adalah kendaraan dengan ukuran {self._size} dan memiliki {self._num_wheels} roda."

    def is_large(self):
        return self._size == "Besar"


class Car(Vehicle):
    def __init__(self, brand, size, num_wheels, fuel_type, top_speed):  # Tambahkan atribut top_speed
        super().__init__(brand, size, num_wheels)
        self._fuel_type = fuel_type
        self._top_speed = top_speed  # Tambah atribut top_speed

    def describe(self):
        return f"{self.brand} adalah mobil berbahan bakar {self._fuel_type} dengan ukuran {self._size} dan {self._num_wheels} roda."

    def start_engine(self):
        return f"{self.brand} memiliki mesin yang sudah dinyalakan."


class SportsCar(Car):
    def __init__(self, brand, size, num_wheels, fuel_type, top_speed):
        super().__init__(brand, size, num_wheels, fuel_type, top_speed)

    def describe(self):
        return f"{self.brand} adalah mobil balap dengan kecepatan maksimum {self._top_speed} km/jam."


class Motorcycle(Vehicle):
    def __init__(self, brand, size, num_wheels, has_sidecar):
        super().__init__(brand, size, num_wheels)
        self._has_sidecar = has_sidecar

    def describe(self):
        sidecar_info = "memiliki" if self._has_sidecar else "tidak memiliki"
        return f"{self.brand} adalah sepeda motor berukuran {self._size} dan memiliki {self._num_wheels} roda."

    def has_sidecar_and_large(self):
        return self._has_sidecar and self.is_large()


# Penggunaan kelas-kelas yang telah dibuat
car_1 = Car("Toyota", "Sedang", 4, "Bensin", 200)
car_2 = Car("Honda", "Kecil", 4, "Bensin", 180)
print()
sports_car_1 = SportsCar("Ferrari", "Sedang", 4, "Bensin", 350)
sports_car_2 = SportsCar("Lamborghini", "Sedang", 4, "Bensin", 380)
print()
motorcycle_1 = Motorcycle("Honda", "Kecil", 2, True)
motorcycle_2 = Motorcycle("Suzuki", "Sedang", 2, False)


vehicles = [car_1, car_2, sports_car_1, sports_car_2, motorcycle_1, motorcycle_2]  # List objek kendaraan

# Perulangan untuk mencetak deskripsi setiap kendaraan
for i, vehicle in enumerate(vehicles):
    print(f"Iterasi ke-{i+1}: {vehicle.describe()}")

# Bandingkan kecepatan antara dua mobil
if isinstance(vehicles[2], SportsCar) and isinstance(vehicles[3], SportsCar):
    speed_difference = vehicles[2]._top_speed - vehicles[3]._top_speed
    if speed_difference > 0:
        print(f"{vehicles[2].brand} lebih cepat dari {vehicles[3].brand} dengan perbedaan kecepatan {speed_difference} km/jam.")
    elif speed_difference < 0:
        print(f"{vehicles[3].brand} lebih cepat dari {vehicles[2].brand} dengan perbedaan kecepatan {abs(speed_difference)} km/jam.")
    else:
        print(f"{vehicles[2].brand} dan {vehicles[3].brand} memiliki kecepatan yang sama.")
else:
    print("Kedua kendaraan bukan SportsCar.")



