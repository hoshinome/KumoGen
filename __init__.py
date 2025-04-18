"""
This program is free software; you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation; either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful, but
WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTIBILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program. If not, see <http://www.gnu.org/licenses/>.
"""

# oooooooooo.  oooo      o8o               .o88o.
# `888'   `Y8b `888      `"'               888 `"
#  888     888  888     oooo  ooo. .oo.   o888oo   .ooooo.
#  888oooo888'  888     `888  `888P"Y88b   888    d88' `88b
#  888    `88b  888      888   888   888   888    888   888
#  888    .88P  888      888   888   888   888    888   888
# o888bood8P'  o888o    o888o o888o o888o o888o   `Y8bod8P'   

bl_info = {
	"name"           : "KumoGen",
    "description"    : "KumoGen 2.4.3 for Blender 3.6+",
    "version"        : (2, 4, 3),
    "blender"        : (3, 6, 0),
    "author"         : "hoshinome",
	"support"        : "COMMUNITY",
	"location"       : "N-Panel > KumoGen > KumoGen",
    "doc_url"        : "https://maasu.booth.pm/items/6720921",
    "tracker_url"    : "",
    "category"       : "",
}

version = f"{bl_info['version'][0]}.{bl_info['version'][1]}.{bl_info['version'][2]}"
panel_label = "KumoGen"

print("".center(100, "-"))
print(".-. .-')              _   .-')                               ('-.       .-') _  ")
print("\  ( OO )            ( '.( OO )_                           _(  OO)     ( OO ) ) ")
print(",--. ,--. ,--. ,--.   ,--.   ,--.).-'),-----.   ,----.    (,------.,--./ ,--,'  ")
print("|  .'   / |  | |  |   |   `.'   |( OO'  .-.  ' '  .-./-')  |  .---'|   \ |  |\  ")
print("|      /, |  | | .-') |         |/   |  | |  | |  |_( O- ) |  |    |    \|  | ) ")
print("|     ' _)|  |_|( OO )|  |'.'|  |\_) |  |\|  | |  | .--, \(|  '--. |  .     |/  ")
print("|  .   \  |  | | `-' /|  |   |  |  \ |  | |  |(|  | '. (_/ |  .--' |  |\    |   ")
print("|  |\   \('  '-'(_.-' |  |   |  |   `'  '-'  ' |  '--'  |  |  `---.|  | \   |   ")
print("`--' '--'  `-----'    `--'   `--'     `-----'   `------'   `------'`--'  `--'   ")
print("".center(100, "-"))

from . import addon, addon_updater_ops
addon_updater_ops.check_for_update_background()

# ooooooooo.                         o8o               .
# `888   `Y88.                       `"'             .o8
#  888   .d88'  .ooooo.   .oooooooo oooo   .oooo.o .o888oo  .ooooo.  oooo d8b
#  888ooo88P'  d88' `88b 888' `88b  `888  d88(  "8   888   d88' `88b `888""8P
#  888`88b.    888ooo888 888   888   888  `"Y88b.    888   888ooo888  888
#  888  `88b.  888    .o `88bod8P'   888  o.  )88b   888 . 888    .o  888
# o888o  o888o `Y8bod8P' `8oooooo.  o888o 8""888P'   "888" `Y8bod8P' d888b
#                        d"     YD
#                        "Y88888P'

def register():
	addon.register()
	addon_updater_ops.register(bl_info)

def unregister():
	addon.unregister()
	addon_updater_ops.unregister()
