# places.py
#
import os

from gi.repository import Adw
from gi.repository import Gtk
import sqlite3

from gi.repository import GLib, Gtk, GObject
from .place import MemoradoPlace

import inspect

class MemoradoPlaces(Gtk.Stack):
    __gtype_name__ = "MemoradoPlaces"

    def __init__(self, **kargs):
        super().__init__(**kargs)
        self._setup()

    def _setup(self):

        # begin UI structure
        self._groups_box = Gtk.Box()
        #self._groups_box.props.expand = True
        self._groups_box.props.visible = True
        self._groups_box.props.orientation = Gtk.Orientation.VERTICAL

        self._places_group = Adw.PreferencesGroup()
        self._places_group.props.title = _("Kartaro")
        self._places_group.props.visible = True

        self.kart_grupo = Adw.PreferencesGroup()
        self.kart_grupo.props.title = _("Karto")
        self.kart_grupo.props.visible = True

        db_name = 'karteibox.db'
        os.getcwd() #return the current working directory
        print(os.getcwd())

        if os.path.isfile(os.getcwd() + '/karteibox.db'):  # wenn es eine Datenbank für die Karteibox gibt wird sie aufgerufen
            self.db_nutzen("select rowid, kartei from karteibox")
            liste = self.c.fetchall()
            self.alle_karteien = []
            for zeile in liste:
                if not list(zeile)[1] in self.alle_karteien: # nur neue Karteien kommen auf die Liste
                    self.alle_karteien.append(list(zeile)[1])
            print (self.alle_karteien)

            for kartei in self.alle_karteien:

                self._add_place(
                self._places_group,
                "folder-documents-symbolic",
                kartei)

            self.conn.close()   # Verbindung schließen

        else:
            self.db_nutzen("""CREATE TABLE if not exists karteibox (
            kartei TEXT, karte_vorn TEXT, karte_hinten TEXT)""")

        self._groups_box.append(self._places_group)

        self.add_named(self._groups_box, "groups")

    def db_nutzen(self, befehl):
        self.conn = sqlite3.connect('karteibox.db')
        self.c = self.conn.cursor() # eine cursor instanz erstellen
        self.c.execute(befehl) # befehl wird ausgeführt

    def _add_place(self, group, icon, name):
        place = MemoradoPlace()
        place.set_icon_name(icon)
        place.set_title(name)
        place.set_subtitle('Saluton')
        #place.path = path
        place.props.activatable = True
        place.connect("activated", self.auf_kartei_geklickt)
        group.add(place)

        return place

    def auf_kartei_geklickt(self, place):
        print('auf kartei ',place.get_title())
        name = place.get_title()
        print(name)
        self.conn = sqlite3.connect('karteibox.db')
        self.c = self.conn.cursor() # eine cursor instanz erstellen
        self.c.execute("select * from karteibox where kartei=:c", {"c": name}) # befehl wird ausgeführt
        liste = self.c.fetchall()
        self.alle_karten = []
        for zeile in liste:
            if list(zeile)[1] != ' ':  # ergibt Liste aller Karten mit Namen
                self.alle_karten.append(list(zeile)[1])
        print (self.alle_karten)

        for karte in self.alle_karten:

            self._add_karte(
            self.kart_grupo,
            "folder-documents-symbolic",
            karte)

        self.conn.close()

        self._groups_box.append(self.kart_grupo)

        self.add_named(self._groups_box, "groups")


    def _add_karte(self, group, icon, name):
        karto = MemoradoPlace()
        karto.set_icon_name(icon)
        karto.set_title(name)
        karto.set_subtitle('karoto')
        #place.path = path
        karto.props.activatable = True
        karto.connect("activated", self.auf_kartei_geklickt)
        group.add(karto)

        #print (karto)

        return karto


        
