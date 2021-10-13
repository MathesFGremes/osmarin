import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

window = Gtk.Window()

label = Gtk.Label()
label.set_label("OMG, that is amazing. Don't you agree?")
label.set_angle(45)
label.set_halign(Gtk.Align.END)

label2 = Gtk.Label()
label2.set_label("WOOOWWWWW, its so cool")
label2.set_angle(90)
label2.set_halign(Gtk.Align.END)

#window.add(label)
window.add(label2)

print(label.get_properties("angle"))

window.connect("delete-event", Gtk.main_quit)
window.show_all()
Gtk.main()