# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTIBILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
# General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.
bl_info = {
    "name": "KumoGen",
    "author": "hoshinome",
    "description": "Add clouds.",
    "blender": (2, 80, 0),
    "version": (2, 3, 0),
    "location": "",
    "warning": "",
    "category": "Generic",
}
print(" KUMOGEN ".center(100, "-"))
from . import addon, addon_updater_ops

def register():
	addon.register()
	addon_updater_ops.register(bl_info)

def unregister():
	addon.unregister()
	addon_updater_ops.unregister()
