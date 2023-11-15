"""CP1404 practical 8 - Do-from-scratch 2: Dynamic Kivy Widgets"""
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.label import Label


class DynamicLabelsApp(App):
    """Main program - Kivy app to dynamically create labels from a list."""

    def __init__(self, **kwargs):
        """Construct main app."""
        super().__init__(**kwargs)
        self.names = ['Alice', 'Bob', 'Claire', 'Danny']

    def build(self):
        """Build the Kivy GUI."""
        self.title = "Dynamic Labels"
        self.root = Builder.load_file('dynamic_labels.kv')
        self.create_labels()
        return self.root

    def create_labels(self):
        """Create a label for each name in a list of names."""
        for name in self.names:
            temp_label = Label(text=name)
            self.root.ids.entries_box.add_widget(temp_label)


DynamicLabelsApp().run()
