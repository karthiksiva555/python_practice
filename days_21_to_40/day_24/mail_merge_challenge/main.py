INVITED_NAMES_PATH = './input/names/invited_names.txt'
LETTER_TEMPLATE_PATH = './input/letters/letter_template.txt'
READY_TO_SEND_PATH = './output/ready_to_send'

def get_invitees_list():
    """Returns invited members list from the file invited_names.txt"""
    with open(INVITED_NAMES_PATH) as file:
        names = file.read().splitlines()
        return names

def get_letter_template():
    """Returns the base letter template from the letter_template.ext file"""
    with open(LETTER_TEMPLATE_PATH) as file:
        return file.read()

def write_to_file(file_name, content):
    """Creates a new file and writes content into it

    The files are generated in /output/ready_to_send directory
    """
    file_path = f"{READY_TO_SEND_PATH}/{file_name}"
    with open(file_path, mode="w") as file:
        file.write(content)

def generate_letter(invitee_name, base_letter):
    content = get_letter_content_for(invitee_name, base_letter)
    file_name = f"letter_for_{invitee_name}"
    write_to_file(file_name, content)

def get_letter_content_for(invitee_name: str, base_letter: str):
    letter_content = base_letter.replace("[name]", invitee_name)
    return letter_content

invitees = get_invitees_list()
letter_template = get_letter_template()

for invitee in invitees:
    generate_letter(invitee, letter_template)

print(f"letter generation completed for all invitees!")
