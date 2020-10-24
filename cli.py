import json
import random
import click

def load_file(path):
    with open(path) as file:
        data = json.load(file)
    return data

def filter_json(json, id):
    filtered = list(filter(lambda e: e.get('id') == id, json))
    return filtered

def random_select(data):
    random_id = random.choice(data)
    return random_id
    
@click.command()
@click.option('--file', required=True, type=str)
@click.option('--id', type=int)
def main(file, id):
    data = load_file(file)
    if not id:
        print("You didn't provide an ID, so we picked one at random:")
        random_element = random_select(data)
        print(random_element)
    else:
        print(f"You selected the following ID: ({id}).")
        select_element = list(filter_json(data, id))
        print(select_element)

if __name__ == '__main__':
    main()