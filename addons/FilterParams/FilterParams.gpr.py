#
# "FilterParams" tool, a modular plugin for Gramps 
# (Gramps - the genealogy software suite built on GTK+/GNOME) 
#
# Copyright (C) 2021-2022      Gramps developers, Kari Kujansuu
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.
#
# To contact the Isotammi Project members, visit the Taapeli GitHub repository:
# https://github.com/Taapeli/isotammi-addons
#

"""
Gramps registration file
"""
from gramps.gui import plug
from gramps.version import major_version
MODULE_VERSION = "5.2"

plug.tool.tool_categories["Isotammi"] = ("Isotammi", _("Isotammi tools"))

#------------------------------------------------------------------------
#
# FilterParams
#
#------------------------------------------------------------------------

register(
    TOOL,
    id="FilterParams",
    name=_("FilterParams"),
    description=_("Display custom filters and allow changing their parameters"),
    version="1.1.6",
    gramps_target_version=MODULE_VERSION,
    status=EXPERIMENTAL,
    audience=EXPERT,
    maintainers=["Kari Kujansuu"],
    maintainers_email=["kari.kujansuu@gmail.com"],
    fname="FilterParams.py",
    authors=["Kari Kujansuu"],
    category="Isotammi",
    help_url="https://github.com/emyoulation/kari/tree/maintenance/gramps52/addons/FilterParams",
    toolclass="Tool",
    optionclass="Options",
    tool_modes=[TOOL_MODE_GUI],
)
