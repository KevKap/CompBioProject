# Weights are [data source, literature, data field] on a scale from 0 to 1 all summing up to 1

from Search_Functions import main_search
#
# print('\nAcetone Trial: ')
# main_search('acetone', isBiological = True)
#
# print('\nAcetic Acid Trial: ')
# main_search('acetic acid', isBiological=True)
#
# print('\nMethane Trial: ')
# main_search('methane', isBiological=False)
#
# print('\nAcetylene Trial: ')
# main_search('acetylene', isBiological=False)
#
# print('\nMorphine Trial: ')
# main_search('morphine', isBiological=False)
#
# print('\nChloroform Trial: ')
# main_search('chloroform', isBiological=False)
#
# print('\nGuanine Trial: ')
# main_search('guanine', isBiological=True)
#
# print('\nBenzene: ')
# main_search('benzene', isBiological=False)

from Enhanced_Search_Functions import enhanced_main_search

print('\nAcetone Trial (Regular): ')
main_search('acetone', isBiological = True)

print('\nAcetone Trial (Enhanced) [0.1, 0.8, 0.1] weights: ')
enhanced_main_search('acetone', [0.1, 0.8, 0.1], isBiological=True, )

print('\nAcetone Trial (Enhanced) [0.2, 0.2, 0.6] weights: ')
enhanced_main_search('acetone', [0.2, 0.2, 0.6], isBiological=True, )

print('\nMethane Trial (Regular): ')
main_search('methane', isBiological=False)

print('\nMethaneTrial (Enhanced) [0.1, 0.8, 0.1] weights: ')
enhanced_main_search('methane', [0.1, 0.8, 0.1], isBiological=False)

print('\nMethane (Enhanced) [0.2, 0.2, 0.6] weights: ')
enhanced_main_search('methane', [0.2, 0.2, 0.6], isBiological=False)

