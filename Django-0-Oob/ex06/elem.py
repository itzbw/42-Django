#!/usr/bin/python3


class Text(str):  # handle HTML text content with special character escaping
    """
    A Text class to represent a text you could use with your HTML elements.

    Because directly using str class was too mainstream.
    """

    def __str__(self):
        """Returns the string with HTML special characters escaped and newlines converted."""

        text = super().__str__().replace("<", "&lt;").replace(">", "&gt;")
        if text == '"':
            text = text.replace('"', "&quot;")
        return text.replace("\n", "\n<br />\n")


class Elem:
    """Class to represent HTML elements with proper nesting and attributes."""

    class ValidationError(Exception):
        """Custom exception for content validation errors."""

        def __init__(self, message="It's neither a Text nor an Elem"):
            super().__init__(message)

    def __init__(
        self, tag="div", attr=None, content=None, tag_type="double"
    ):  # Constructor
        """Initialize an HTML element with given tag, attributes, content and type."""
        self.tag = tag
        self.attr = attr or {}  # Dictionary of HTML attributes (defaults to None)
        self.content = []  # Element content (can be Text, Elem, or list of both)
        self.tag_type = (
            tag_type  # "double" for normal tags, "simple" for self-closing tags
        )

        if content is not None:
            self.add_content(content)

    def __str__(self):
        """Return the HTML string representation of the element."""
        if self.tag_type == "simple":
            return f"<{self.tag}{self.__make_attr()} />"

        return f"<{self.tag}{self.__make_attr()}>{self.__make_content()}</{self.tag}>"

    def __make_attr(self):
        """Generate the HTML attribute string."""
        if not self.attr:
            return ""

        return "".join(f' {key}="{value}"' for key, value in sorted(self.attr.items()))

    def __make_content(self):
        """Generate the HTML content string with proper indentation."""
        if not self.content:
            return ""

        result = ["\n"]
        for elem in self.content:
            result.append("  " + str(elem).replace("\n", "\n  ") + "\n")
        return "".join(result)

    def add_content(self, content):
        """Add content to the element after validation."""
        if not self.check_type(content):
            raise self.ValidationError()

        if isinstance(content, list):
            # Filter out empty Text instances while adding
            self.content.extend(elem for elem in content if elem != Text(""))
        elif content != Text(""):
            self.content.append(content)

    @staticmethod
    def check_type(content):
        """Validate if content is a valid HTML element or text."""
        if isinstance(content, (Elem, Text)):
            return True

        if isinstance(content, list):
            return all(isinstance(elem, (Elem, Text)) for elem in content)

        return False


if __name__ == "__main__":
    try:
        html = Elem(
            tag="html",
            content=[
                Elem(
                    tag="head",
                    content=Elem(tag="title", content=Text('"Hello ground!"')),
                ),
                Elem(
                    tag="body",
                    content=[
                        Elem(tag="h1", content=Text('"Oh no, not again!"')),
                        Elem(
                            tag="img",
                            tag_type="simple",
                            attr={"src": "http://i.imgur.com/pfp3T.jpg"},
                        ),
                    ],
                ),
            ],
        )
        print(html)
    except Exception as e:
        print(e)
