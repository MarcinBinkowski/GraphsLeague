from jinja2 import Environment, FileSystemLoader

def generate_raport(name):
    file_loader = FileSystemLoader("src/templates")
    env = Environment(loader=file_loader)
    template = env.get_template("template.html")
    output_from_parsed_template = template.render(summoner=name)
    print(output_from_parsed_template)

    # to save the results
    with open("my_new_file.html", "w") as f:
        f.write(output_from_parsed_template)

if __name__ == "__main__":
    generate_raport("binq661")