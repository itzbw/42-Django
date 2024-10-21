def parse_line(line: str):
    el = line.split("=")
    result = {
        key.strip(): value.strip()
        for key, value in (item.split(":") for item in el[1].split(", "))
    }
    result["name"] = el[0].strip()
    return result


def main():
    HTML = """
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Periodic table</title>
  <style>
    table {{
      border-collapse: collapse;
    }}
    h4 {{
      text-align: center;
    }}
    ul {{
      list-style:none;
      padding-left:0px;
    }}
  </style>
</head>
<body>
  <table>
    {body}
  </table>
</body>
</html>
"""

    TEMPLATE = """
      <td style="border: 1px solid black; padding:10px">
        <h4>{name}</h4>
        <ul>
          <li>No {number}</li>
          <li>{small}</li>
          <li>{molar}</li>
          <li>{electron} electron</li>
        </ul>
      </td>
"""

    body = []
    with open("periodic_table.txt", "r") as f:
        periodic_table = [parse_line(line) for line in f.readlines()]

    position = 0
    body.append("<tr>")  # Start the first row
    for element in periodic_table:
        element_position = int(element["position"])

        if position >= element_position:  # Close the previous row and start a new one
            body.append("</tr>\n<tr>")
            position = 0  # Reset position for the new row

        # Add empty cells if needed
        body.extend(["<td></td>\n"] * (element_position - position - 1))

        # Add the element's cell
        body.append(
            TEMPLATE.format(
                name=element["name"],
                number=element["number"],
                small=element["small"],
                molar=element["molar"],
                electron=element["electron"],
            )
        )

        position = element_position  # Update the current position

    body.append("</tr>\n")  # Close the last row

    # Write the HTML output
    with open("periodic_table.html", "w") as f:
        f.write(HTML.format(body="".join(body)))


if __name__ == "__main__":
    main()
