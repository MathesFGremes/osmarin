import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

class MainWindow(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="Cheeseburger Machine")
        self.set_border_width(10)
        listbox = Gtk.ListBox()
        listbox.set_selection_mode(Gtk.SelectionMode.NONE)
        self.add(listbox)

        # checkbox
        row_1 = Gtk.ListBoxRow()
        box_1 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=100)
        row_1.add(box_1)
        label1 = Gtk.Label("check if you love cheeseburgers:")
        check = Gtk.CheckButton()
        box_1.pack_start(label1, True, True, 0)
        box_1.pack_start(check, True, True, 0)
        listbox.add(row_1)

        # Toggle Switch
        row_2 = Gtk.ListBoxRow()
        box_2 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=100)
        row_2.add(box_2)
        label2 = Gtk.Label("Burger making machine:")
        switch = Gtk.Switch()
        box_2.pack_start(label2, True, True, 0)
        box_2.pack_start(check, True, True, 0)
        listbox.add(row_2)
        


window = MainWindow()
window.connect("delete-event", Gtk.main_quit)
window.show_all()
Gtk.main()