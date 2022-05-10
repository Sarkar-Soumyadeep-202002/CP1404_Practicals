"""
CP1404 Practicals
Soumyadeep Sarkar
Build a Kivy app using dynamic widgets
"""

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.label import Label


class DynamicWidgets(App):
    """Program to create an app with dynamic widgets"""

    def __init__(self, **kwargs):
        """Construct main app."""
        super().__init__(**kwargs)
        self.names = ["Bob Brown", "Cat Cyan", "Oren Ochre", "Tony Stark",]

    def build(self):
        """Build the Kivy app"""
        self.title = "Dynamic Widgets"
        self.root = Builder.load_file("dynamic_labels.kv")
        self.create_widgets()
        return self.root

    def create_widgets(self):
        """Create labels from the list and add them to the app"""
        for name in self.names:
            temp_label = Label(text=name)
            self.root.ids.input_labels.add_widget(temp_label)


DynamicWidgets().run()
