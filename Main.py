from Search_Functions import main_search

print('\nAcetone Trial: ')
main_search('acetone', isBiological = True)

print('\nAcetic Acid Trial: ')
main_search('acetic acid', isBiological=True)

print('\nMethane Trial: ')
main_search('methane', isBiological=False)

print('\nAcetylene Trial: ')
main_search('acetylene', isBiological=False)

print('\nMorphine Trial: ')
main_search('morphine', isBiological=False)

print('\nChloroform Trial: ')
main_search('chloroform', isBiological=False)

print('\nGuanine Trial: ')
main_search('guanine', isBiological=True)

print('\nBenzene: ')
main_search('benzene', isBiological=False)
