"""CP1404 practical 8 - Walkthrough example: Modify existing GUI"""
from kivy.app import App
from kivy.lang import Builder


class BoxLayoutDemo(App):
    """Kivy App for greeting user based on text input."""
    def build(self):
        """Build the Kivy GUI."""
        self.title = "Box Layout Demo"
        self.root = Builder.load_file('box_layout.kv')
        return self.root

    def handle_greet(self):
        """Handle greet button press, display greeting with name from text input."""
        self.root.ids.output_label.text = f"Hello {self.root.ids.input_name.text}"

    def handle_clear(self):
        """Handle clear button press, clear text input and greeting."""
        self.root.ids.input_name.text = ''
        self.root.ids.output_label.text = ''


BoxLayoutDemo().run()
