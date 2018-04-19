import Bio.KEGG.REST

def compound_ID_pull(compound_name):
    """Gets KEGG compound ID from compound name"""
    # Compound name needs to be in title case (Aaaaa Aaaa) (only if not all uppercase such as ATP)
    if not(compound_name.isupper()):
        compound_name_update = compound_name.lower().capitalize()
    else:
        compound_name_update = compound_name

    # Returns text object of all compounds that are related
    raw_data = Bio.KEGG.REST.kegg_find('compound', compound_name_update)

    # Looks for entry where it is compound_name; as formatted in the returned raw_data
    full_data = raw_data.readlines()
    for line in full_data:
        if compound_name_update + ';' in line:
            entry = line
            break

    # Finds the first instance of colon after cpd and '  ' after the number
    try:
        colon = entry.find(':')
        space = entry.find('	')

        return entry[colon + 1:space]

    except:
        return '\nThis compound is not in the KEGG database. Please set isBiological to False.\n'


def kegg_URL_generator(compound_name):
    """Generates KEGG database URL"""
    # Gets KEGG ID
    ID = compound_ID_pull(compound_name)

    # General URL template
    URL_temp = 'https://www.genome.jp/dbget-bin/www_bget?'

    return URL_temp + ID


def KEGG_databse_number(compound_name):
    """Returns the database link number from the compound page"""

    # Gets raw data
    raw_data = Bio.KEGG.REST.kegg_get(compound_ID_pull(compound_name))

    # Runs through the lines, searching for other DB links
    record = False
    database_reference_number = 0
    for line in raw_data.readlines():
        if line[:7] == 'DBLINKS':
            # If line starts with DBLINKS, it counts new lines
            record = True
        if line[:4] == 'ATOM':
            record = False
        if record:
            database_reference_number += 1

    # Returns number of outside database links
    return database_reference_number


def KEGG_data_fields(compound_name):
    """Returns the number of data fields for a compound"""

    # Gets raw data
    raw_data = Bio.KEGG.REST.kegg_get(compound_ID_pull(compound_name))

    # Runs through lines, recording when there is a new data field (one deemed worthy (listed in approved_list))
    approved_list = ['NAME', 'FORMULA', 'EXACT_MASS', 'MOL_WEIGHT', 'REACTION', 'PATHWAY', 'MODULE', 'ENZYME', 'BRITE',
                     'DBLINKS']

    # Initializes data_field_number
    data_field_number = 0

    # Goes through all the lines and checks to see if fields are there
    for line in raw_data.readlines():
        split_line = line.split()
        if split_line[0] in approved_list:
            data_field_number += 1

    return data_field_number


def KEGG_datarank_vecotr(compound_name):
    """Returns vector associated with KEGG that will be used in the ranking method"""

    # Data fields function
    data_fields = KEGG_data_fields(compound_name)

    # Gets number of data sources and literature
    data_sources = KEGG_databse_number(compound_name)

    # Literature will be set to 0, but will be assigned minimal value of literature citations (as other lowest source)
    # since KEGG self references

    # Vector for ranking (all entries have fields in same positions)
    return [data_sources, 0, data_fields]
