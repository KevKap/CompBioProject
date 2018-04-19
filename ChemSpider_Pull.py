import pubchempy as pcp
from chemspipy import ChemSpider

cs = ChemSpider('Security Token')


# This uses pubchem, despite chemspipy functionality to make sure all websites retrieve exact same entry
def chemspider_puller(compound_name):
    """Pulls InChI from pubchem database"""
    result = pcp.get_compounds(compound_name, 'name')
    compound = result[0]
    return compound.inchi


def chemspider_csID_pull(compound_name):
    """Gets CSID from database using inchi"""
    # Get InChI
    inchi = chemspider_puller(compound_name)

    # Get CS ID from CS ID object
    csID_raw = cs.search(inchi)
    csID_object = csID_raw[0]
    csID = csID_object.csid

    return str(csID)


def chemspi_URL_generator(compound_name):
    """Generates ChemSpider URL from ChemSpider ID"""
    csID = chemspider_csID_pull(compound_name)

    # URL form = www.chemspider.com/Chemical-Structure.csID.html
    return 'https://www.chemspider.com/Chemical-Structure.' + str(csID) + '.html'


def chemspi_datasource_count(compound_name):
    """Gets number of data sources for compound
    Returns data as [datasource #, literature #]"""
    ID = chemspider_csID_pull(compound_name)

    # Gets a list of dictionary with compound data
    raw_data = cs.get_extended_mol_compound_info_list(ID, include_reference_counts=True)

    # Extracts Dictionary
    full_data = raw_data[0]

    # Gets values from the two desired keys
    return [full_data['datasource_count'], full_data['reference_count']]


def chemspi_datarank_vecotr(compound_name):
    """Returns vector associated with ChemSpider that will be used in the ranking method"""

    # Data Fields is always 11 (personal count of properties)
    data_fields = 11

    # Gets number of data sources and literature
    [data_sources, literature] = chemspi_datasource_count(compound_name)

    # Vector for ranking (all entries have fields in same positions)
    return [data_sources, literature, data_fields]

