# -*- coding: utf-8 -*-
#  Copyright © 2020 StarrFox
#
#  ArcanumBot is free software: you can redistribute it and/or modify
#  it under the terms of the GNU Affero General Public License as published
#  by the Free Software Foundation, either version 3 of the License, or
#  (at your option) any later version.
#
#  ArcanumBot is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU Affero General Public License for more details.
#
#  You should have received a copy of the GNU Affero General Public License
#  along with ArcanumBot.  If not, see <https://www.gnu.org/licenses/>.

import aiosqlite


def get_database() -> aiosqlite.Connection:
    """
    Gets the arcanumbot database
    :return: The db context manager
    """

    def adapt_set(_set):
        return ",".join(map(str, _set))

    def convert_set(s):
        return {i.decode() for i in s.split(b",")}

    import sqlite3

    sqlite3.register_adapter(set, adapt_set)

    sqlite3.register_converter("pyset", convert_set)

    return aiosqlite.connect("arcanumbot.db", detect_types=sqlite3.PARSE_DECLTYPES)
