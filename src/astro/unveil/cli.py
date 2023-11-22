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


# current command thoughts:
#   unveil --verbosely \
#          [dng|jpg|arw|arw2|tiff|jpeg|bmp|raw|png]
#          files --like 'darks/timelapse_[#index].dng' \
#                --recursively-in my/astro/raws/2023/11/19/ \
#                --from-index 22 \
#                --to-index 56 \
#                --no-casing \
#          by [renaming|appending|filling|linking|saving] \
#             --as 'dark.#sensor.#resolution.#iso.#shutter.#index.dng' \
#             --into 'my/astro/masters/darks/#sensor/#resolution/#iso/#shutter/' \
#             --[skip-existing|replace-existing|append-existing] \
#             --from-index 1

DEFAULT_FILE_TYPES = ("dng", "jpg", "arw", "arw2","tiff", "jpeg", "bmp", "raw", "png")

@click.group("unveil", chain=True)
@click.option(
    "--verbosely", count=True
    , help="Increases verbosity level by one each time option is used")
@click.argument("file-types", type=str)
@click.pass_context
def unveil_grp(ctx, *args, **options) -> None:
    """Renames image stacks based on file metadata"""
    verbosely = options.get('verbosely', 0)

    file_types = DEFAULT_FILE_TYPES \
        if (opt_value := options.get('file_types', "").lower()) == "all" \
        else tuple(opt_value.split(','))

    ctx.obj = {
        'verbosely': verbosely
        , 'file-types': file_types
        , }

    if verbosely:
        click.echo(f"unveil_grp: {ctx.obj=}")


@unveil_grp.command("files")
@click.option(
    "--like", type=str
    , metavar="'PATH/FILNAME_TEMPLATE'"
    , help="Template describing filenames to unveil. PATH is the tail of the search path directories to "
           "include when locating image files to unveil. FILENAME_TEMPLATE is one, or more, string literals "
           "and/or meta tokens describing the file basenames to unveil. Each meta token is of form "
           "[#meta-token-name] and all other text not within a meta token's square brackets are treated as "
           "literals or globs (in the case of '*' and '?') in the filenames. All supported tokens are available "
           "via 'unveil list --meta-tokens'." )
@click.pass_obj
def unveil_files_cmd(obj, *args, **options) -> None:
    """Defines the nature of the stack files to unveil."""
    click.echo(f"unveil files.{options=}")


if __name__ == "__main__":
    unveil_grp()