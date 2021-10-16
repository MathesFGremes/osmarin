import gi

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk, GLib


class CellRendererProgressWindow(Gtk.Window):
    def __init__(self):
        super().__init__(title="CellRendererProgress Example")
        self.Vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
        self.label = Gtk.Label(label = "Matheus colocou")
        
        self.set_default_size(200, 200)

        self.liststore = Gtk.ListStore(str, int, bool)
        self.current_iter = self.liststore.append(["Sabayon", 0, False])
        self.liststore.append(["Zenwalk", 0, False])
        self.liststore.append(["SimplyMepis", 0, False])

        treeview = Gtk.TreeView(model=self.liststore)

        renderer_text = Gtk.CellRendererText()
        column_text = Gtk.TreeViewColumn("Text", renderer_text, text=0)
        treeview.append_column(column_text)

        renderer_progress = Gtk.CellRendererProgress()
        column_progress = Gtk.TreeViewColumn(
            "Progress", renderer_progress, value=1, inverted=2
        )
        treeview.append_column(column_progress)

        renderer_toggle = Gtk.CellRendererToggle()
        renderer_toggle.connect("toggled", self.on_inverted_toggled)
        column_toggle = Gtk.TreeViewColumn("Inverted", renderer_toggle, active=2)
        treeview.append_column(column_toggle)

        #self.add(treeview)
        self.add(self.Vbox)
        self.Vbox.pack_start(self.label, True, True, 0)
        self.Vbox.pack_start(treeview, True, True, 0)

        self.timeout_id = GLib.timeout_add(20, self.on_timeout, None)

    def on_inverted_toggled(self, widget, path):
        self.liststore[path][2] = not self.liststore[path][2]

    def on_timeout(self, user_data):
        new_value = self.liststore[self.current_iter][1] + 1
        if new_value > 100:
            self.current_iter = self.liststore.iter_next(self.current_iter)
            if self.current_iter is None:
                self.reset_model()
            new_value = self.liststore[self.current_iter][1] + 1
            

        self.liststore[self.current_iter][1] = new_value
        return True

    def reset_model(self):
        for row in self.liststore:
            row[1] = 0
        self.current_iter = self.liststore.get_iter_first()


win = CellRendererProgressWindow()
win.connect("destroy", Gtk.main_quit)
win.show_all()
Gtk.main()