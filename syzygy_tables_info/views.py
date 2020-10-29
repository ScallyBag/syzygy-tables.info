# This file is part of the syzygy-tables.info tablebase probing website.
# Copyright (C) 2015-2020 Niklas Fiekas <niklas.fiekas@backscattering.de>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.


import os
import textwrap

from tinyhtml import Frag, html, h, frag, raw
from typing import Optional


def asset_url(path: str) -> str:
    return "/static/{}?mtime={}".format(path, os.path.getmtime(os.path.join(os.path.dirname(__file__), "..", "static", path)))


def kib(num: float) -> str:
    for unit in ["KiB", "MiB", "GiB", "TiB", "PiB", "EiB", "ZiB"]:
        if abs(num) < 1024:
            return "%3.1f %s" % (num, unit)
        num /= 1024
    return "%.1f %s" % (num, "Yi")


def layout(*, title: str, development: bool, left: Optional[Frag] = None, right: Optional[Frag] = None, head: Optional[Frag] = None, scripts: Optional[Frag] = None) -> Frag:
    return html(lang="en")(
        raw("<!-- https://github.com/niklasf/syzygy-tables.info -->"),
        h("head")(
            h("meta", charset="utf-8"),
            h("link", rel="preload", href="/static/fonts/fontello.woff2", as_="font", type="font/woff2", crossorigin=True),
            h("link", rel="stylesheet", href=asset_url("css/style.min.css")),
            head,
            h("title")(title, " – Syzygy endgame tablebases"),
            h("meta", name="viewport", content="width=device-width,initial-scale=1.0,user-scalable=yes"),
            h("meta", name="keywords", content="Syzygy,chess,endgame,tablebase"),
            h("meta", name="author", content="Niklas Fiekas"),
            h("link", rel="author", title="Legal", href="/legal"),
            h("link", rel="icon", href="/static/favicon.32.png", type="image/png", sizes="32x32"),
            h("link", rel="icon", href="/static/favicon.96.png", type="image/png", sizes="96x96"),
            h("link", rel="sitemap", href="/sitemap.txt", type="text/plain"),
        ),
        h("body")(
            h("div", style="background:#c00;color:#fff;text-align:center;font-weight:bold;position:fixed;z-index:1;width:100%;top:0;")("Careful, this is an unreliable development version") if development else None,
            h("div", klass="left-side")(
                h("div", klass="inner")(left),
            ),
            h("div", klass="right-side")(
                h("div", klass="inner")(right),
            ),
            h("footer")(
                h("div", klass="inner")(
                    h("p")(
                        "Powered by Ronald de Man's ",
                        h("a", href="https://github.com/syzygy1/tb")("Syzygy endgame tablebases"), ", ",
                        "7-piece tables generated by Bojun Guo and a ",
                        h("a", href="https://github.com/niklasf/lila-tablebase#http-api")("public API"), " ",
                        "hosted by ",
                        h("a", href="https://tablebase.lichess.ovh")("lichess.org"), ".",
                    ),
                    h("p")(
                        h("a", href="/endgames")("Endgames"), ". ",
                        h("a", href="/metrics")("Metrics"), ". ",
                        h("a", href="/legal", data_jslicense=1)("Legal"), ". ",
                        h("a", href="https://github.com/niklasf/syzygy-tables.info")("GitHub"), ".",
                    ),
                ),
            ),
            scripts,
        ),
    )


def back_to_board() -> Frag:
    return h("nav")(
        h("div", klass="reload")(
            h("a", klass="btn btn-default", href="/")("Back to board"),
        ),
    )


def legal(*, development: bool = True) -> Frag:
    return layout(
        development=development,
        title="Legal",
        left=frag(
            h("h1")("Legal"),
            h("p")("The tablebase lookup is provided on a best-effort basis, without guarantees of correctness or availability. Feedback or questions are welcome."),
            h("p")("There are standard server logs kept no longer than 48 hours."),
            back_to_board(),
        ),
        right=frag(
            h("section", id="contact")(
                h("h2")("Contact"),
                h("p")(
                    h("a", href="mailto:niklas.fiekas@backscattering.de")("niklas.fiekas@backscattering.de"), " ",
                    "(", h("a", href="https://pgp.mit.edu/pks/lookup?op=get&search=0x2ECA66C65B255138")("pgp"), ")",
                ),
            ),
            h("section", id="imprint")(
                h("h2")("Imprint"),
                h("p")(
                    "Niklas Fiekas",
                    h("br"), "Tannenhöhe 16",
                    h("br"), "38678 Clausthal-Zellerfeld",
                    h("br"), "Germany",
                ),
            ),
            h("section", id="thanks")(
                h("h2")("Software licenses"),
                h("p")(
                    "The ",
                    h("a", href="https://github.com/niklasf/syzygy-tables.info")("code for the website itself"),
                    " is ",
                    h("a", href="https://github.com/niklasf/syzygy-tables.info/blob/master/LICENSE")("licensed under the AGPL-3.0+"),
                    ".",
                ),
                h("table", id="jslicense-labels1")(
                    h("thead")(
                        h("tr")(
                            h("th")("Script"),
                            h("th")("License"),
                            h("th")("Source"),
                        ),
                    ),
                    h("tbody")(
                        h("tr")(
                            h("td")(
                                h("a", href=asset_url("js/client.min.js"))("client.min.js"),
                            ),
                            h("td")(
                                h("a", href="https://www.gnu.org/licenses/agpl-3.0.en.html")("AGPL-3.0+"),
                            ),
                            h("td")(
                                h("a", href="https://github.com/niklasf/syzygy-tables.info/blob/master/src/client.ts")("client.ts"),
                            ),
                        ),
                    ),
                ),
                h("p")("It also uses the following software/artwork:"),
                h("ul")(
                    h("li")(
                        h("a", href="https://github.com/ornicar/chessground")("chessground"),
                        " (GPL-3.0+)",
                    ),
                    h("li")(
                        h("a", href="https://github.com/niklasf/chessops")("chessops"),
                        " (GPL-3.0+)",
                    ),
                    h("li")(
                        h("a", href="https://github.com/niklasf/python-chess")("python-chess"),
                        " (GPL-3.0+)",
                    ),
                    h("li")(
                        h("a", href="https://github.com/niklasf/python-tinyhtml")("tinyhtml"),
                        " (MIT/Apache-2.0)",
                    ),
                    h("li")(
                        h("a", href="http://aiohttp.readthedocs.org/en/stable/")("aiohttp"),
                        " (Apache-2.0)",
                    ),
                    h("li")(
                        "Selected icons from ",
                        h("a", href="https://fontawesome.com/")("Font Awesome"),
                        " (SIL)",
                    ),
                    h("li")(
                        "A few styles from ",
                        h("a", href="https://getbootstrap.com/")("Bootstrap"),
                        " (MIT)",
                    ),
                ),
            ),
        ),
    )


def metrics(*, development: bool) -> Frag:
    wdl50 = frag("WDL", h("sub")(50))
    dtz50_pp = frag("DTZ", h("sub")(50), "′′")
    n = h("var")("n")
    example1 = "1kb5/8/1KN5/3N4/8/8/8/8 b - -"
    example2 = "8/8/2N5/8/3k4/7N/p2K4/8 b - -"

    def example_board(epd: str, check: str) -> Frag:
        board_fen = epd.split(" ")[0]
        return h("a", href=f"/?fen={epd.replace(' ', '_')}_0_1")(
            h("img", width=300, height=300, alt=epd, src=f"https://backscattering.de/web-boardimage/board.svg?fen={board_fen}&check={check}"),
        )

    def example_link(epd: str) -> Frag:
        return h("a", href=f"/?fen={epd.replace(' ', '_')}_0_1")(epd)

    return layout(
        development=development,
        title="Metrics",
        left=frag(
            h("h1")("Metrics"),
            h("p")("Information stored in Syzygy tablebases"),
            back_to_board(),
        ),
        right=frag(
            h("section", id="wdl")(
                h("h2")(wdl50),
                h("p")(
                    "5-valued ",
                    h("em")("Win/Draw/Loss"),
                    " information can be used to decide which positions to aim for.",
                ),
                h("div", klass="list-group stats")(
                    h("div", klass="list-group-item white-win")("Win (+2)"),
                    h("div", klass="list-group-item white-win frustrated")("Win prevented by 50-move rule (+1)"),
                    h("div", klass="list-group-item draws")("Drawn (0)"),
                    h("div", klass="list-group-item black-win frustrated")("Loss saved by 50-move rule (-1)"),
                    h("div", klass="list-group-item black-win")("Loss (-2)"),
                ),
            ),
            h("section", id="dtz")(
                h("h2")(dtz50_pp, " with rounding"),
                h("p")(
                    "Once a tablebase position has been reached, the ",
                    h("em")("Distance To Zeroing"), " ",
                    "(of the fifty-move counter by a capture or pawn move) ",
                    "can be used to reliably make progress in favorable positions and stall ",
                    "in unfavorable positions.",
                ),
                h("p")("The precise meanings are as follows:"),
                h("p")(
                    "A DTZ value ", n, " with 100 ≥ ", n, " ≥ 1 means the position is winning, ",
                    "and a zeroing move or checkmate can be forced in ", n, " or ", n, " + 1 half-moves.",
                ),
                example_board(example1, "b8"),
                h("p")(
                    "For an example of this ambiguity, see how the DTZ repeats after the only-move Ka8 in ",
                    example_link(example1), ". ",
                    "This is due to the fact that some Syzygy tables store rounded moves ",
                    "instead of half-moves, to save space. This implies some primary tablebase lines ",
                    "may waste up to 1 ply. Rounding is never used for endgame phases where it would ",
                    "change the game theoretical outcome (", wdl50, ").",
                ),
                h("p")(
                    "Users need to be careful in positions ",
                    "that are nearly drawn under ",
                    "the 50-move rule! Carelessly wasting 1 more ply ",
                    "by not following the tablebase recommendation, for a total of 2 wasted plies, ",
                    "may change the outcome of the game.",
                ),
                h("p")(
                    "A DTZ value ", n, " > 100 means the position is winning, but drawn under the 50-move rule. ",
                    "A zeroing move or checkmate can be forced in ", n, " or ", n, " + 1 half-moves, ",
                    "or in ", n, " - 100 or ", n, " + 1 - 100 half-moves ",
                    "if a later phase is responsible for the draw.",
                ),
                example_board("8/8/2N5/8/3k4/7N/p2K4/8 b - -", "d4"),
                h("p")(
                    "For example, in ", example_link(example2), " ",
                    "black promotes the pawn in 7 ply, but the DTZ is 107, ",
                    "indicating that white can hold a draw under the 50-move rule ",
                    "in a later phase of the endgame.",
                ),
                h("p")(
                    "An in-depth discussion of rounding can be found in ",
                    h("a", href="http://www.talkchess.com/forum3/viewtopic.php?f=7&t=58488#p651293")("this thread"), ".",
                ),
            ),
        ),
    )


def stats(*, development: bool) -> Frag:
    return layout(
        development=development,
        title="Machine readable endgame statistics",
        left=frag(
            h("h1")("Machine readable endgame statistics"),
            back_to_board(),
        ),
        right=frag(
            h("section", id="api")(
                h("h2")("API"),
                h("div", klass="panel panel-default")(
                    h("div", klass="panel-heading")(
                        "GET ", h("a", href="/stats.json")("/stats.json"),
                    ),
                    h("div", klass="panel-body")(
                        "All endgame stats with keys such as ", h("code")("KRNvKNN"), ".",
                    ),
                ),
                h("div", klass="panel panel-default")(
                    h("div", klass="panel-heading")(
                        "GET ", h("a", href="/stats/KRNvKNN.json")("/stats/KRNvKNN.json"),
                    ),
                    h("div", klass="panel-body")(
                        "Endgame stats for a specific endgame, e.g., ", h("code")("KRNvKNN"), ". ",
                        "Redirects to normalized endgame names.",
                    ),
                ),
            ),
            h("section", id="example")(
                h("h2")("Example (KRNvKNN)"),
                h("pre")(
                    h("code")(textwrap.dedent("""\
                        {
                          "rtbw": {
                            "bytes": 290002640, // file size
                            "tbcheck": "a320ac...", // internal checksum
                            "md5": "6ee435...",
                            "sha1": "07a0e4...",
                            "sha256": "f3386d...",
                            "sha512": "c4bf73...",
                            "b2": "b970e0...", // blake 2
                            "ipfs": "QmXW4S..."
                          },
                          "rtbz": {
                            // ...
                          },
                          "longest": [
                            // longest winning endgames for black/white
                            // with/without 50-move rule
                            {
                              "epd": "3n1n2/8/8/8/4R3/8/8/NK1k4 b - -",
                              "ply": 100,
                              "wdl": -2
                            },
                            {
                              "epd": "6k1/5n2/8/8/8/5n2/1RK5/1N6 w - -",
                              "ply": 485,
                              "wdl": 1
                            },
                            {
                              "epd": "8/8/8/8/8/8/N1nk4/RKn5 b - -",
                              "ply": 7,
                              "wdl": 2
                            }
                          ],
                          "histogram": {
                            "white": { // white to move
                              "win": [
                                0,
                                1924310948,
                                35087,
                                363845772,
                                37120,
                                138550471,
                                // ...
                              ]
                              "loss": [
                                98698, // # of positions losing in 0
                                144, // # of positions losing in 1
                                3810, // # of positions losing in 2
                                0, // 3
                                596, // 4
                                0, // 5
                                58 // 6
                              ],
                              "wdl": { // # of positions with each wdl
                                "-2": 0,
                                "-1": 103306,
                                "0": 1333429189,
                                "1": 162344388,
                                "2": 2959977091
                              }
                            },
                            "b": { // black to move
                              // ...
                            },
                          }
                        }"""
                    )),
                ),
            ),
        ),
    )


def endgames(*, development: bool) -> Frag:
    return layout(
        development=development,
        title="Endgames",
        left=frag(
            h("h1")("Endgames"),
            h("p")("These are the longest endgames (maximum DTZ) for each material configuration."),
            h("p")(
                h("a", href="/endgames.pgn")(
                    h("span", klass="icon icon-download")(), " endgames.pgn",
                ),
                " (", kib(4396), ")",
            ),
            back_to_board(),
        ),
    )
