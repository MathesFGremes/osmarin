import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

class MainWindow(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title = 'title of the window')

        # Button
        self.button = Gtk.Button(label="click here!")
        self.button.connect("clicked", self.button_clicked)
        self.add(self.button)
    
    # User clicks button
    def button_clicked(self, widget):
        print("something")


window = MainWindow()
#window = Gtk.Window()
window.connect("delete-event", Gtk.main_quit)
window.show_all()
Gtk.main()