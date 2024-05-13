import pprint


def add_person(
        contact_list=None, first_name=None, last_name=None, email=None, **additional_details
):
    if contact_list is None:
        contact_list = []
    # Create the dictionary with the keys that will always be present, even if their
    # value can be None
    data = {"First Name": first_name, "Last Name": last_name, "Email": email}
    # Iterate through the dictionary additional_details and add these attributes to data
    for key, value in additional_details.items():
        data[key] = value
    # Append the dictionary data to the contact list
    contact_list.append(data)

    return contact_list


# Call function without the contact_list argument, which means a new list is created
scientists = add_person(
    first_name="Rosalind",
    last_name="Franklin",
    subject="Chemistry",
    colleagues=["James Watson", "Francis Crick"],
)

# Function is now called with the keyword argument contact_list=scientists
scientists = add_person(
    contact_list=scientists,
    first_name="Grace",
    last_name="Hopper",
    subject="Computer Programming",
    firsts="Use of the term 'bug'",
)

scientists = add_person(
    contact_list=scientists,
    first_name="Marie",
    last_name="Curie",
    honours=["Nobel Prize in Chemistry", "Nobel Prize in Physics"],
)

pprint.pprint(scientists)
