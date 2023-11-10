from kivy.app import App
from kivy.lang import Builder
from kivy.properties import StringProperty

CONVERSION_FACTOR = 1.609344


class ConvertMilesKm(App):
    """"""
    result = StringProperty()

    def build(self):
        """ build the Kivy app from the kv file """
        self.title = "Convert Miles to Kilometres"
        self.root = Builder.load_file('convert_miles_km.kv')
        self.result = ''
        return self.root

    def handle_convert(self):
        """Convert miles from input field to kilometres."""
        try:
            self.result = str(float(self.root.ids.input_number.text) * CONVERSION_FACTOR)
        except ValueError:
            self.result = str(0.0)

    def handle_increment(self, user_input, increment):
        try:
            self.root.ids.input_number.text = str(float(user_input) + increment)
        except ValueError:
            self.root.ids.input_number.text = str(0 + increment)
        # not sure if that's what we're supposed to do, but it works :)


ConvertMilesKm().run()
