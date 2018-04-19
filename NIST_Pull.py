# To generate URL, need to use IUPAC Standard InChI string, going to use pubchempy
import pubchempy as pcp

def inchi_puller(compound_name):
    # Pulls InChI from pubchem databse
    result = pcp.get_compounds(compound_name, 'name')
    compound = result[0]
    return compound.inchi

def nist_URL_generator(compound_name):
    # Gets InChI
    inchi = inchi_puller(compound_name)

    # Returns URL
    return 'https://webbook.nist.gov/cgi/inchi/' + inchi


