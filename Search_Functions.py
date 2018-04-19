from Pubchem_Pull import *
from KEGG_Pull import *
from ChemSpider_Pull import *


def database_search(compound_name, isBiological = True):
    """Searches the databases and returns them in a list in
    the order PubChem, NIST, KEGG (Kegg is only returned if isBiological
    is set to True"""
    try:
        # If compound is not biological, make argument false
        compound_name_reformat = compound_name.lower().title()
        pc = pubchem_URL_generator(compound_name_reformat)
        chemspi = chemspi_URL_generator(compound_name_reformat)

        if isBiological:
            kegg = kegg_URL_generator(compound_name_reformat)
            websites = [pc, chemspi, kegg]
        else:
            websites = [pc, chemspi]

        return websites
    except:
        return '\nCompound not found in databases. Check spelling or try using an alternative name.'


def rank_data(compound_name, isBiological):
    """Ranks data from given data vecotrs (vecotrs are in the form [data sources, literature, data fields]
    Uses metric 0.5*literature + 0.3*data_sources + 0.2*data_fields"""
    if isBiological:

        # Returns KEGG data rank vector
        kegg = KEGG_datarank_vecotr(compound_name)

        # Returns ChemSpider data rank vector
        chemspider = chemspi_datarank_vecotr(compound_name)

        # Returns PubChem data rank vector
        pubchem = pubchem_datarank_vector(compound_name)

        # Adjusts Kegg literature to be the minimum from PubChem and ChemSpider
        kegg[1] = min(pubchem[1], chemspider[1])

        # Ranks in a dictionary to allow easier sorting
        ranking_dictionary = {'kegg': 0.5*kegg[1] + 0.3*kegg[0] + 0.2*kegg[2],
        'chemspider': 0.5*chemspider[1] + 0.3*chemspider[0] + 0.2*chemspider[2],
        'pubchem':  0.5*pubchem[1] + 0.3*pubchem[0] + 0.2*pubchem[2]}

        return sorted(ranking_dictionary.items(), key=lambda x: x[1])

    else:
        # Returns ChemSpider data rank vector
        chemspider = chemspi_datarank_vecotr(compound_name)

        # Returns PubChem data rank vector
        pubchem = pubchem_datarank_vector(compound_name)

        # Ranks in a dictionary to allow easier sorting
        ranking_dictionary = {'chemspider': 0.5 * chemspider[1] + 0.3 * chemspider[0] + 0.2 * chemspider[2],
        'pubchem': 0.5 * pubchem[1] + 0.3 * pubchem[0] + 0.2 * pubchem[2]}

        return sorted(ranking_dictionary.items(), key=lambda x: x[1])


def main_search(compound_name, isBiological = True):
    """"This function will eventually use results of the ranking algorithm to determine return order"""


    # Websites returned in [pc, chemspi, kegg] or [pc, chemspi]
    website_dictionary = {'pubchem': 0, 'chemspider': 1, 'kegg': 2}

    URLS = database_search(compound_name, isBiological)

    if isBiological:
        # Ranking is a list of tuples sorted by lowest rank to highest
        #  Where the first entry in each tuple is the source
        ranking = rank_data(compound_name, isBiological)

        # Determines the ranking order
        last = ranking[0]
        middle = ranking[1]
        first = ranking[2]

        # Uses the website dictionary to sort the URLs and prints them out in the proper oder
        print('\n' + URLS[website_dictionary[first[0]]])
        print('\n' + URLS[website_dictionary[middle[0]]])
        print('\n' + URLS[website_dictionary[last[0]]])

    else:
        # Ranking is a list of tuples sorted by lowest rank to highest
        #  Where the first entry in each tuple is the source
        ranking = rank_data(compound_name, isBiological)

        # Determines the ranking order
        last = ranking[0]
        first = ranking[1]

        # Uses the website dictionary to sort the URLs and prints them out in the proper order
        print('\n' + URLS[website_dictionary[first[0]]])
        print('\n' + URLS[website_dictionary[last[0]]])


