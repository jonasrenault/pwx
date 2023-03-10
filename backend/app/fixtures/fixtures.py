from ..models import Wall
from ..schemas import Area, Rect, Path


def create_la_plaine():
    petit_devers_gauche = Area(
        name="petit devers gauche",
        paths=[
            Rect(
                type="rect",
                x=20,
                y=45,
                w=43,
                h=135,
                color="#FFA500",
            ),
            Rect(
                type="rect",
                x=52,
                y=45,
                w=11,
                h=97,
                color="rgb(219, 233, 224)",
            ),
            Path(
                type="fill",
                points=[
                    [42, 45],
                    [52, 140],
                    [52, 45],
                    [42, 45],
                ],
                color="rgb(167, 181, 161)",
            ),
        ],
        border=[
            [20, 45],
            [63, 45],
            [63, 180],
            [20, 180],
        ],
    )

    cirque_gauche = Area(
        name="cirque gauche",
        paths=[
            Path(
                type="fill",
                points=[
                    [63, 45],
                    [68, 45],
                    [93, 142],
                    [63, 142],
                ],
                color="rgb(219, 233, 224)",
            ),
            Path(
                type="fill",
                points=[
                    [68, 45],
                    [74, 45],
                    [100, 77],
                    [93, 142],
                ],
                color="rgb(238, 238, 167)",
            ),
            Path(
                type="fill",
                points=[
                    [74, 45],
                    [100, 77],
                    [100, 24],
                ],
                color="rgb(167, 181, 161)",
            ),
            Rect(
                type="rect",
                x=63,
                y=143,
                w=30,
                h=37,
                color="#FFA500",
            ),
        ],
        border=[
            [63, 45],
            [74, 45],
            [100, 24],
            [100, 77],
            [93, 180],
            [63, 180],
        ],
    )
    proue = Area(
        name="proue",
        paths=[
            Path(
                type="fill",
                points=[
                    [100, 24],
                    [112, 14],
                    [117, 39],
                ],
                color="rgb(219, 233, 224)",
            ),
            Path(
                type="fill",
                points=[
                    [100, 24],
                    [100, 77],
                    [129, 77],
                ],
                color="rgb(227, 220, 128)",
            ),
            Path(
                type="fill",
                points=[
                    [100, 24],
                    [117, 39],
                    [129, 77],
                ],
                color="rgb(238, 238, 167)",
            ),
            Path(
                type="fill",
                points=[
                    [100, 77],
                    [100, 82],
                    [132, 82],
                    [129, 77],
                ],
                color="rgb(92, 45, 45)",
            ),
            Path(
                type="fill",
                points=[
                    [100, 82],
                    [93, 142],
                    [112, 106],
                    [132, 82],
                ],
                color="rgb(227, 220, 128)",
            ),
            Path(
                type="fill",
                points=[
                    [93, 142],
                    [112, 106],
                    [132, 82],
                    [132, 87],
                ],
                color="rgb(92, 45, 45)",
            ),
            Path(
                type="fill",
                points=[
                    [112, 14],
                    [117, 39],
                    [161, 45],
                    [161, 14],
                ],
                color="rgb(219, 233, 224)",
            ),
            Path(
                type="fill",
                points=[
                    [117, 39],
                    [161, 45],
                    [129, 77],
                ],
                color="rgb(227, 220, 128)",
            ),
            Path(
                type="fill",
                points=[
                    [129, 77],
                    [161, 45],
                    [161, 74],
                ],
                color="rgb(238, 238, 167)",
            ),
            Path(
                type="fill",
                points=[
                    [129, 77],
                    [132, 82],
                    [132, 87],
                    [161, 82],
                    [161, 74],
                ],
                color="rgb(92, 45, 45)",
            ),
            Path(
                type="fill",
                points=[
                    [93, 142],
                    [132, 87],
                    [161, 82],
                    [161, 110],
                ],
                color="rgb(219, 233, 224)",
            ),
            Path(
                type="fill",
                points=[
                    [93, 142],
                    [161, 110],
                    [161, 143],
                ],
                color="rgb(238, 238, 167)",
            ),
            Rect(type="rect", x=93, y=143, w=68, h=37, color="#FFA500"),
        ],
        border=[
            [100, 24],
            [112, 14],
            [161, 14],
            [161, 180],
            [93, 180],
            [100, 77],
        ],
    )

    cirque_droit = Area(
        name="cirque droit",
        paths=[
            Path(
                type="fill",
                points=[
                    [161, 14],
                    [161, 45],
                    [183, 73],
                    [187, 30],
                ],
                color="rgb(167, 181, 161)",
            ),
            Path(
                type="fill",
                points=[
                    [187, 30],
                    [183, 73],
                    [216, 65],
                    [203, 40],
                ],
                color="rgb(219, 233, 224)",
            ),
            Path(
                type="fill",
                points=[
                    [161, 45],
                    [161, 74],
                    [183, 73],
                ],
                color="rgb(238, 238, 167)",
            ),
            Path(
                type="fill",
                points=[
                    [161, 74],
                    [161, 82],
                    [216, 74],
                    [216, 65],
                    [183, 73],
                ],
                color="rgb(92, 45, 45)",
            ),
            Path(
                type="fill",
                points=[
                    [161, 82],
                    [161, 110],
                    [216, 124],
                    [216, 74],
                ],
                color="rgb(219, 233, 224)",
            ),
            Path(
                type="fill",
                points=[
                    [161, 110],
                    [161, 143],
                    [216, 143],
                    [216, 124],
                ],
                color="rgb(238, 238, 167)",
            ),
            Rect(type="rect", x=161, y=143, w=55, h=37, color="#FFA500"),
        ],
        border=[
            [161, 14],
            [203, 40],
            [216, 65],
            [216, 180],
            [161, 180],
        ],
    )

    petit_toit = Area(
        name="petit toit",
        paths=[
            Path(
                type="fill",
                points=[
                    [203, 40],
                    [224, 45],
                    [216, 65],
                ],
                color="rgb(167, 181, 161)",
            ),
            Path(
                type="fill",
                points=[
                    [224, 45],
                    [216, 65],
                    [251, 85],
                ],
                color="rgb(219, 233, 224)",
            ),
            Path(
                type="fill",
                points=[
                    [224, 45],
                    [251, 85],
                    [266, 101],
                    [266, 45],
                ],
                color="rgb(238, 238, 167)",
            ),
            Path(
                type="fill",
                points=[
                    [216, 65],
                    [216, 74],
                    [266, 111],
                    [266, 101],
                    [251, 85],
                ],
                color="rgb(92, 45, 45)",
            ),
            Path(
                type="fill",
                points=[
                    [216, 74],
                    [216, 124],
                    [246, 143],
                    [266, 153],
                    [266, 111],
                ],
                color="rgb(219, 233, 224)",
            ),
            Path(
                type="fill",
                points=[
                    [216, 124],
                    [216, 143],
                    [246, 143],
                ],
                color="rgb(238, 238, 167)",
            ),
            Path(
                type="fill",
                points=[
                    [216, 143],
                    [216, 180],
                    [266, 180],
                    [266, 153],
                    [246, 143],
                ],
                color="#FFA500",
            ),
        ],
        border=[
            [203, 40],
            [224, 45],
            [266, 45],
            [266, 180],
            [216, 180],
            [216, 65],
        ],
    )

    petit_devers_droit = Area(
        name="petit devers gauche",
        paths=[
            Path(
                type="fill",
                points=[
                    [266, 45],
                    [295, 45],
                    [295, 143],
                ],
                color="rgb(219, 233, 224)",
            ),
            Path(
                type="fill",
                points=[
                    [266, 45],
                    [266, 101],
                    [295, 143],
                ],
                color="rgb(238, 238, 167)",
            ),
            Path(
                type="fill",
                points=[
                    [266, 101],
                    [266, 111],
                    [295, 143],
                ],
                color="rgb(92, 45, 45)",
            ),
            Path(
                type="fill",
                points=[
                    [266, 111],
                    [266, 153],
                    [295, 180],
                    [295, 143],
                ],
                color="rgb(219, 233, 224)",
            ),
            Path(
                type="fill",
                points=[
                    [266, 153],
                    [266, 180],
                    [295, 180],
                ],
                color="#FFA500",
            ),
            Rect(type="rect", x=295, y=45, w=35, h=135, color="#FFA500"),
        ],
        border=[
            [266, 45],
            [330, 45],
            [330, 180],
            [266, 180],
        ],
    )

    la_plaine = Wall(
        key="laplaine",
        name="La Plaine",
        city="Paris XVe",
        areas=[
            petit_devers_gauche,
            cirque_gauche,
            proue,
            cirque_droit,
            petit_toit,
            petit_devers_droit,
        ],
    )

    return la_plaine


def create_croix_nivert():
    bloc = Area(
        name="bloc",
        paths=[
            Path(
                type="fill",
                points=[
                    [6, 71],
                    [62, 80],
                    [12, 130],
                    [42, 150],
                    [6, 150],
                ],
                color="rgb(120, 100, 100)",
            ),
            Path(
                type="fill",
                points=[
                    [62, 80],
                    [12, 130],
                    [42, 150],
                    [90, 122],
                ],
                color="#FFA500",
            ),
            Path(
                type="fill",
                points=[
                    [42, 150],
                    [90, 122],
                    [130, 122],
                    [191, 144],
                    [193, 150],
                ],
                color="rgb(120, 100, 100)",
            ),
            Path(
                type="fill",
                points=[
                    [62, 80],
                    [99, 76],
                    [90, 122],
                ],
                color="rgb(32, 74, 117)",
            ),
            Path(
                type="fill",
                points=[
                    [99, 76],
                    [122, 76],
                    [130, 122],
                    [90, 122],
                ],
                color="rgb(18, 43, 73)",
            ),
            Path(
                type="fill",
                points=[
                    [122, 76],
                    [130, 122],
                    [153, 81],
                ],
                color="rgb(32, 74, 117)",
            ),
            Path(
                type="fill",
                points=[
                    [153, 81],
                    [130, 122],
                    [191, 92],
                ],
                color="#FFA500",
            ),
            Path(
                type="fill",
                points=[
                    [153, 81],
                    [193, 81],
                    [191, 92],
                ],
                color="rgb(32, 74, 117)",
            ),
            Path(
                type="fill",
                points=[
                    [130, 122],
                    [191, 92],
                    [191, 144],
                ],
                color="rgb(32, 74, 117)",
            ),
            Path(
                type="fill",
                points=[
                    [193, 81],
                    [191, 92],
                    [202, 99],
                ],
                color="rgb(18, 43, 73)",
            ),
            Path(
                type="fill",
                points=[
                    [191, 92],
                    [202, 99],
                    [191, 144],
                ],
                color="rgb(18, 43, 73)",
            ),
        ],
        border=[
            [6, 71],
            [6, 150],
            [193, 150],
            [191, 144],
            [202, 99],
            [193, 81],
            [153, 81],
            [122, 76],
            [99, 76],
            [62, 80],
        ],
    )

    cirque_gauche = Area(
        name="cirque gauche",
        paths=[
            Path(
                type="fill",
                points=[
                    [193, 54],
                    [214, 54],
                    [240, 135],
                    [240, 150],
                    [193, 150],
                    [191, 144],
                    [202, 99],
                    [193, 81],
                ],
                color="rgb(167, 153, 131)",
            ),
            Path(
                type="fill",
                points=[
                    [214, 54],
                    [240, 45],
                    [240, 135],
                ],
                color="rgb(18, 43, 73)",
            ),
        ],
        border=[
            [193, 54],
            [214, 54],
            [240, 45],
            [240, 150],
            [193, 150],
            [191, 144],
            [202, 99],
            [193, 81],
        ],
    )

    proue = Area(
        name="proue",
        paths=[
            Path(
                type="fill",
                points=[
                    [240, 45],
                    [286, 45],
                    [285, 88],
                    [240, 135],
                ],
                color="rgb(32, 74, 117)",
            ),
            Path(
                type="fill",
                points=[
                    [240, 135],
                    [285, 88],
                    [285, 95],
                ],
                color="#FFA500",
            ),
            Path(
                type="fill",
                points=[
                    [240, 135],
                    [285, 95],
                    [285, 150],
                    [240, 150],
                ],
                color="rgb(120, 100, 100)",
            ),
        ],
        border=[
            [240, 45],
            [286, 45],
            [285, 88],
            [285, 150],
            [240, 150],
        ],
    )

    cirque_droit = Area(
        name="cirque droit",
        paths=[
            Path(
                type="fill",
                points=[
                    [286, 45],
                    [309, 54],
                    [303, 78],
                    [285, 95],
                    [285, 88],
                ],
                color="#FFA500",
            ),
            Path(
                type="fill",
                points=[
                    [309, 54],
                    [329, 54],
                    [329, 150],
                    [285, 150],
                    [285, 95],
                    [303, 78],
                ],
                color="rgb(120, 100, 100)",
            ),
        ],
        border=[
            [286, 45],
            [309, 54],
            [329, 54],
            [329, 150],
            [285, 150],
            [285, 88],
        ],
    )

    dalle = Area(
        name="dalle",
        paths=[
            Path(
                type="fill",
                points=[
                    [329, 54],
                    [335, 54],
                    [329, 150],
                ],
                color="rgb(120, 100, 100)",
            ),
            Path(
                type="fill",
                points=[
                    [335, 54],
                    [329, 150],
                    [344, 150],
                ],
                color="rgb(18, 43, 73)",
            ),
            Path(
                type="fill",
                points=[
                    [335, 54],
                    [385, 54],
                    [344, 150],
                ],
                color="rgb(32, 74, 117)",
            ),
            Path(
                type="fill",
                points=[
                    [385, 54],
                    [344, 150],
                    [400, 150],
                ],
                color="#FFA500",
            ),
            Path(
                type="fill",
                points=[
                    [385, 54],
                    [400, 150],
                    [404, 150],
                ],
                color="rgb(200, 109, 47)",
            ),
        ],
        border=[
            [329, 54],
            [385, 54],
            [404, 150],
            [329, 150],
        ],
    )

    vertical_droit = Area(
        name="vertical droit",
        paths=[
            Path(
                type="fill",
                points=[
                    [385, 54],
                    [436, 54],
                    [436, 150],
                    [404, 150],
                ],
                color="rgb(120, 100, 100)",
            )
        ],
        border=[
            [385, 54],
            [436, 54],
            [436, 150],
            [404, 150],
        ],
    )

    croixNivert = Wall(
        key="croixniv",
        name="Croix Nivert",
        city="Paris XVe",
        areas=[bloc, cirque_gauche, proue, cirque_droit, dalle, vertical_droit],
    )

    return croixNivert
