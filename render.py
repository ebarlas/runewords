import json
import jinja2


def main():
    with open('runewords.json', 'r') as f:
        rws = json.load(f)

    print(rws)

    env = jinja2.Environment(loader=jinja2.FileSystemLoader('templates'), trim_blocks=True)
    template = env.get_template('runewords.html')
    rendered = template.render(runewords=rws['runewords'])

    with open('runewords.html', 'w') as f:
        f.write(rendered)


if __name__ == '__main__':
    main()
