Zoneify is a Python-based desktop application that enables users to create and visualize geofences on a map. Using PyQt5 for the graphical user interface, folium for map rendering, and geopy for geocoding, Zoneify allows users to specify a place and a radius to create a geofence, which is then displayed in a web browser.

Features
User-Friendly Interface: Built with PyQt5, the application provides a simple and intuitive interface for entering location details and radius.
Dynamic Map Creation: Utilizes folium to create and display maps with geofences.
Geocoding: Employs geopy to convert place names into geographic coordinates.
Interactive Visualization: Opens the generated map with the geofence in a web browser.
Requirements
Python 3.7 or higher
PyQt5
folium
geopy
webbrowser (built-in library)
Installation
To install the required libraries, run the following command:
pip install pyqt5 folium geopy




Enter a place name in the "Enter a place name:" field.
Enter the radius in kilometers in the "Enter the radius (in kilometers):" field.
Create Geofence:

Click on "Create Fence" to generate and display the geofence on the map in a web browser.
Clear Fields:

Click on "Clear Fence" to reset the input fields.
Code Structure
main.py: The main script that contains the GeofencingApplication class and the entry point for the application.
Contact
For any questions or suggestions, please open an issue or contact me at [rpoojitha2003@gmail.com].

