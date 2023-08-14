import subprocess
import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

class WarningWindow(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="Предупреждение")
        self.set_border_width(20)

        vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10)
        self.add(vbox)

        label = Gtk.Label()
        label.set_text("ВНИМАНИЕ! Соблюдайте правила безопасности при отправке писем на сторонние домены!")
        vbox.pack_start(label, True, True, 0)

        button_box = Gtk.Box(spacing=6)
        vbox.pack_start(button_box, True, True, 0)

        ok_button = Gtk.Button.new_with_label("ОК")
        ok_button.connect("clicked", self.on_ok_clicked)
        button_box.pack_start(ok_button, True, True, 0)

        self.set_decorated(False)  # Убрать заголовок окна
        self.set_skip_taskbar_hint(True)  # Убрать окно из панели задач
        self.set_keep_above(True)  # Установить окно поверх других окон

    def on_ok_clicked(self, widget):
        self.start_evolution()

    def start_evolution(self):
        self.destroy()
        subprocess.Popen(["evolution"], close_fds=True)

win = WarningWindow()
win.connect("destroy", Gtk.main_quit)
win.show_all()
Gtk.main()
