import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

class MainWindow(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="Um bom titulo")

        # Box
        self.box = Gtk.Box(spacing=10)
        self.add(self.box)

        # Bacon button
        self.bacon_button = Gtk.Button(label="Bacon")
        self.bacon_button.connect("clicked", self.bacon_clicked)
        self.box.pack_start(self.bacon_button, True, True, 0)

        # Tuna button
        self.tuna_button = Gtk.Button(label="Tuna")
        self.tuna_button.connect("clicked", self.tuna_clicked)
        self.box.pack_start(self.tuna_button, True, True, 0)

    def bacon_clicked(self, Widget):
        print("You clicked Bacon")
    
    def tuna_clicked(self, Widget):
        print("You clicked Tuna")



window = MainWindow()
window.connect("delete-event", Gtk.main_quit)
window.show_all()
Gtk.main()