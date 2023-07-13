# window.py
#
# Copyright 2023 Walter
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# SPDX-License-Identifier: GPL-3.0-or-later

import os

from gi.repository import Adw
from gi.repository import Gtk, GLib, Gio

from .places import MemoradoPlaces


import inspect

@Gtk.Template(resource_path='/im/bernard/Memorado/window.ui')
class MemoradoWindow(Adw.ApplicationWindow):
    __gtype_name__ = 'MemoradoWindow'

    places_box = Gtk.Template.Child()
    places_inner_box = Gtk.Template.Child()
    neue_kartei = Gtk.Template.Child()

    #kartenbox = Gtk.Template.Child()



    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self._setup()


    def _setup(self):
        places = MemoradoPlaces()
        self.places_inner_box.append(places)

        #places.connect("updated", self._on_places_updated)

        self.neue_kartei.connect("clicked", self.auf_neue_kartei)



    def auf_neue_kartei(self, w):
        print('neue Kartei wird erstellt')

    def _on_places_updated(self, button, path):
        #self._reset_to_path(path)
        self._go_to_files_view(duration=0)

    def _go_to_files_view(self, duration):
        self.content_deck.set_visible_child(self.files_stack)
        self.files_stack.props.transition_duration = duration
        self.files_stack.set_visible_child(self.files_box)



    
