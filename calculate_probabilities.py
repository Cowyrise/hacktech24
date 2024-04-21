from data_processing import *

data_extract()

female_genes_list = [] # inputted from the user
male_genes_list = [] # inputted from the user
viewed = []
probabilities = {}
def calculate_probability(mother_disorders, father_disorders):
    female_genes_list = mother_disorders
    male_genes_list = father_disorders
    for gene in female_genes_list:
        if disorder_gene[gene] == 'D' or disorder_gene[gene] == 'dominant':
            if gene in male_genes_list and gene not in viewed:
                #print(f"Probability of the offspring having {gene} is 93.75%")
                viewed.append(gene)
                probabilities[gene] = "93.75%"
            elif gene not in male_genes_list and gene not in viewed:
                print(f"Probability of the offspring having {gene} is 75%")
                viewed.append(gene)
                probabilities[gene] = "75%"
            else:
                pass
        if disorder_gene[gene] == 'recessive':
            if gene in male_genes_list and gene not in viewed:
                print(f"Probability of the offspring having {gene} is 100%")
                viewed.append(gene)
                probabilities[gene] = "100%"
            elif gene not in male_genes_list and gene not in viewed:
                print(f"Probability of the offspring {gene} disorder is 25%")
                viewed.append(gene)
                probabilities[gene] = "25%"
            else:
                pass
    for gene in male_genes_list:
        if gene not in viewed:
            viewed.append(gene)
            if disorder_gene[gene] == 'D' or disorder_gene[gene] == 'dominant':
                print(f"Probability of the offspring having {gene} is 75%")
                probabilities[gene] = "75%"
            elif disorder_gene[gene] == 'recessive':
                print(f"Probability of the offspring {gene} disorder is 25%")
                probabilities[gene] = "25%"
            else:
                pass
    return probabilities
calculate_probability(female_genes_list,male_genes_list)