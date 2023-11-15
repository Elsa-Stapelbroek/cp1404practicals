"""
CP1404 practical 8 - Do-from-scratch 1: Miles to Kilometres Converter
"""
from kivy.app import App
from kivy.lang import Builder
from kivy.properties import StringProperty

MILES_TO_KM_FACTOR = 1.609344


class MilesConversionApp(App):
    """Kivy App for converting miles to kilometres."""
    result = StringProperty()

    def build(self):
        """Build the Kivy GUI from the kv file."""
        self.title = "Convert Miles to Kilometres"
        self.root = Builder.load_file('convert_miles_km.kv')
        self.result = 'Enter the number of miles to convert'
        return self.root

    def handle_convert(self):
        """Convert miles from input field to kilometres."""
        try:
            self.result = str(float(self.root.ids.input_number.text) * MILES_TO_KM_FACTOR)
        except ValueError:
            self.result = str(0.0)

    def handle_increment(self, user_input, increment):
        """Update value in text input and call conversion function."""
        try:
            self.root.ids.input_number.text = str(float(user_input) + increment)
        except ValueError:
            self.root.ids.input_number.text = str(0 + increment)
        self.handle_convert()


MilesConversionApp().run()
