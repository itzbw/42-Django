import os
import sys
import re
import settings

#https://stackoverflow.com/questions/2146618/raising-an-exception-vs-printing
def process_template(template_path):
    if not template_path.endswith(".template"):
        raise ValueError("Wrong extension, required: .template")

    if not os.path.isfile(template_path):
        raise FileNotFoundError(f"File does not exist: {template_path}")

    with open(template_path, "r") as f:
        template = f.read()

    formatted_content = template.format(
        name=settings.name,
        surname=settings.surname,
        title=settings.title,
        age=settings.age,
        profession=settings.profession,
    )

    output_path = re.sub(r"\.template$", ".html", template_path)
    with open(output_path, "w") as f:
        f.write(formatted_content)

    print(f"Successfully processed {template_path} to {output_path}")


def main():
    if len(sys.argv) != 2:
        print("Usage: script.py <template_file>")
        sys.exit(1)

    try:
        process_template(sys.argv[1])
    except (ValueError, FileNotFoundError) as e:
        print(f"Error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
