#!/usr/bin/python3

from elem import Elem, Text


def create_element_class(tag_name, tag_type="double"):
    """Factory function to create HTML element classes."""

    class NewElement(Elem):
        def __init__(self, content=None, attr: dict = {}):
            super().__init__(
                tag=tag_name if tag_name else None,
                attr=attr,
                content=content,
                tag_type=tag_type,
            )

    NewElement.__name__ = tag_name.capitalize() if tag_name else "Div"
    return NewElement


# Define HTML elements with their configurations
ELEMENT_CONFIGS = {
    # Double-tag elements
    "html": {},
    "head": {},
    "body": {},
    "title": {},
    "table": {},
    "th": {},
    "tr": {},
    "td": {},
    "ul": {},
    "ol": {},
    "li": {},
    "h1": {},
    "h2": {},
    "p": {},
    "span": {},
    "hr": {},
    "br": {},
    # Special case for div (no tag name)
    None: {"tag_type": "double"},
    # Simple-tag elements
    "meta": {"tag_type": "simple"},
    "img": {"tag_type": "simple"},
}

# Dynamically create all HTML element classes
globals().update(
    {
        (name.capitalize() if name else "Div"): create_element_class(
            name, config.get("tag_type", "double")
        )
        for name, config in ELEMENT_CONFIGS.items()
    }
)


def test():
    html = Html(
        [
            Head([Title(content=Text('"Hello ground!"'))]),
            Body(
                [
                    H1(content=Text('"Oh no, not again!"')),
                    Img(attr={"src": "http://i.imgur.com/pfp3T.jpg"}),
                ]
            ),
        ]
    )
    print(html)


if __name__ == "__main__":
    test()
