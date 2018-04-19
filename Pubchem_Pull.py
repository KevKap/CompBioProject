import pubchempy as pcp
import requests

def CID_puller(compound_name):
    """Returns compound ID from PubChem Database"""
    # Gets CID from compound name and returns the value as an str
    result = pcp.get_compounds(compound_name, 'name')
    compound = result[0]
    CID = compound.cid
    return str(CID)


def pubchem_URL_generator(compound_name):
    """Returns PubChem URL"""
    # Gets compound CID
    compound_CID = CID_puller(compound_name)

    # URL template to return clickable link
    URL_template = 'https://pubchem.ncbi.nlm.nih.gov/compound/'

    # Final URL for compound
    pubchem_URL = URL_template + compound_CID

    return pubchem_URL


def pubmed_article_IDs(compound_name):
    """Returns PubMed article IDs"""
    # Get the compound CID for insertion into URL
    compound_CID = CID_puller(compound_name)

    # Generic URL to access PubMed ID
    pubmed_articles_url = 'https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/cid/' + compound_CID + '/xrefs/PubMedID/TXT'

    # Uses requests to get all PubMed IDs
    website_data_raw = requests.get(pubmed_articles_url)

    # Extracts all IDs and puts them in a list
    website_data = website_data_raw.text
    PubMedID_list = website_data.split('\n')

    # Get number of PubMed articles
    return len(PubMedID_list)


def data_source_number(compound_name):
    """Returns the number of sources used (number of substance IDs for compound)"""
    # Get CID for compound
    cid = CID_puller(compound_name)

    # Substance information (Gets returned as a list of a dictionary)
    substance_info = pcp.get_sids(cid)

    # Isolates dictionary out
    substance_record = substance_info[0]

    # Value for the 'SID' is returned as a list of all the SID entries
    # Length of this list is the number of sources
    data_sources = len(substance_record['SID'])

    return data_sources


def pubchem_datarank_vector(compound_name):
    """Returns vector associated with PubChem for ranking method"""
    # Data source number
    data_sources = data_source_number(compound_name)

    # Data field number (decided on 24 from https://pubchempy.readthedocs.io/en/latest/guide/properties.html)
    data_fields = 24

    # Literature reference count (This is just the total number of PubMed articles)
    # Decided to halve the number to account for the fact that some just the compound and are not focused
    # on the compound
    literature = pubmed_article_IDs(compound_name) / 2

    return [data_sources, literature, data_fields]

