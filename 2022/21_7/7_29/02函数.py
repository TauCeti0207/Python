# 开发时间:  2021/7/29 8:25
def greet_user():
    print('hello!')


greet_user()


def get_formatted_name(first_name, last_name, middle_name=''):
    if middle_name:
        full_name = f"{first_name} {middle_name} {last_name}"
    else:
        full_name = f"{first_name} {last_name}"
    return full_name.title()


musician = get_formatted_name('jimi', 'hendrix')
print(musician)


unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
completed_models = []


def print_models(unprinted_designs, completed_models):
    while unprinted_designs:
        currnt_design = unprinted_designs.pop()
        print(f"{currnt_design}")
    completed_models.append(currnt_design)


def show_completed_models(completed_models):
    for completed_model in completed_models:
        print(completed_model)


print_models(unprinted_designs, completed_models)


