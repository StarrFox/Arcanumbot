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

from discord.ext import commands


def is_coin_mod_or_above():
    def pred(ctx: commands.Context):
        if not ctx.guild:
            return False

        coin_mod_role = ctx.guild.get_role(
            ctx.bot.config["general"].getint("coin_mod_role_id")
        )

        # Different guild
        if not coin_mod_role:
            return False

        if ctx.author.top_role >= coin_mod_role:
            return True

        return False

    return commands.check(pred)
