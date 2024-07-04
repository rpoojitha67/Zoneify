import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QPushButton, QVBoxLayout, QWidget
import folium
import webbrowser
from geopy.geocoders import Nominatim

class GeofencingApplication(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Zoneify Application")

        self.label_place = QLabel(self)
        self.label_place.setText("Enter a place name:")
        self.place_input = QLineEdit(self)

        self.label_radius = QLabel(self)
        self.label_radius.setText("Enter the radius (in kilometers):")
        self.radius_input = QLineEdit(self)

        self.create_button = QPushButton("Create Fence", self)
        self.create_button.clicked.connect(self.create_geofence)

        self.clear_button = QPushButton("Clear Fence", self)
        self.clear_button.clicked.connect(self.clear_geofence)

        layout = QVBoxLayout()
        layout.addWidget(self.label_place)
        layout.addWidget(self.place_input)
        layout.addWidget(self.label_radius)
        layout.addWidget(self.radius_input)
        layout.addWidget(self.create_button)
        layout.addWidget(self.clear_button)

        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

    def create_geofence(self):
        place_name = self.place_input.text()
        radius_text = self.radius_input.text()

        if not place_name or not radius_text:
            return

        geolocator = Nominatim(user_agent="geofencing_app")
        location = geolocator.geocode(place_name)

        if not location:
            print("Could not find coordinates for the specified place.")
            return

        latitude, longitude = location.latitude, location.longitude
        radius_km = float(radius_text)
        radius_m = radius_km * 1000  # Convert the radius from km to meters

        map_center = latitude, longitude
        m = folium.Map(location=map_center, zoom_start=15)
        folium.Circle(location=map_center, radius=radius_m, color='blue', fill=True, fill_color='blue', fill_opacity=0.1).add_to(m)

        map_filename = "geofence_map.html"
        m.save(map_filename)

        webbrowser.open_new_tab(map_filename)

    def clear_geofence(self):
        self.place_input.clear()
        self.radius_input.clear()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    geofencing_app = GeofencingApplication()
    geofencing_app.show()
    sys.exit(app.exec_())
