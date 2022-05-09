"""
CP1404 Practicals
Soumyadeep Sarkar
Build Kivy App to Convert distance from miles to kilometers
"""

from kivy.app import App
from kivy.lang import Builder

MILES_TO_KM = 1.60934


class MilesToKmConverter(App):
    """MilesToKmConverter is a Kivy App to convert distance from miles to kilometer"""
    def build(self):
        """build the Kivy app from the convert_miles_kv file"""
        self.title = "Convert Miles to Km"
        self.root = Builder.load_file("convert_miles_km.kv")
        return self.root

    def handle_calculation(self):
        """Convert the input distance from miles to kilometer"""
        distance_miles = float(self.root.ids.input_distance_miles.text)
        self.root.ids.output_label.text = str(distance_miles * MILES_TO_KM)

    def handle_increment(self, increment_value):
        """Increment the distance according to the user's choice"""
        distance_miles = float(self.root.ids.input_distance_miles.text) + increment_value
        self.root.ids.input_distance_miles.text = str(distance_miles)


MilesToKmConverter().run()
