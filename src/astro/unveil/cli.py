# cli.py is an astrophotography utility to rename image stacks based on file metadata.
# Copyright (C) 2023  Scott Barnett
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published
# by the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

import click


@click.group("unveil")
@click.option(
    "--verbose", "-v", "verbosity", count=True
    , help="Increases verbosity level by one each time option is used")
@click.pass_context
def unveil_grp(ctx, verbosity) -> None:
    """Renames image stacks based on file metadata"""

    ctx.obj = {
        'verbosity': verbosity
        , }


if __name__ == "__main__":
    unveil_grp()