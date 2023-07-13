# place.py

from gi.repository import Adw
from gi.repository import Gtk


@Gtk.Template(resource_path='/im/bernard/Memorado/place.ui')
class MemoradoPlace(Adw.ActionRow):
    __gtype_name__ = "MemoradoPlace"

    #eject = Gtk.Template.Child()
    mount = None
    path = ""
    uuid = ""
    encrypted = None
    device = None
