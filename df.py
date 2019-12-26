# inputs:
# sample traits (trait_df)
# SNP profiling (genotype:heter/homo) for all samples(sample_df)
# GWAS SNPs for obesity (gwas_df)

# output files:
# SNPs genotype table for case and ctrl (case_table, ctrl_table)
# count of heterozygous and homozygous SNPs (count_snp)
# SNP profiling (genotype) for all sample (new_sample_df)


genotype = {'AA':(1),
            'AC':(5, 8),
            'AG':(6, 11),
            'CC':(2),
            'CT':(10, 15),
            'GG':(3),
            'GT':(13, 16),
            'TT':(4),
            'AT':(7, 14),
            'CG':(9, 12)}

 N_genome = {'A':(1, 5, 6, 7, 8, 11, 14),
             'C':(2, 5, 8, 9, 10, 12,15),
             'T':(4, 7, 10, 13, 14, 15, 16),
             'G':(3, 6, 9, 11, 12, 13, 16)}


gwas_df = gwas_df["STRONGEST SNP-RISK ALLELE"]
gwas_df = list(set(gwas_df)) # get rid of the redundent risk snps in the database

# create a dictionary {snp_id: strongest snp-risk allele}
db = {}
for j in range(0, len(gwas_df)):
    risksnp_id = gwas_df[j].split("-")[0]
    risk_base = gwas_df[j].split("-")[1]
    if risk_base != "?":
       db[risksnp_id] = risk_base


# snp profling for case and control group
case_df = sample_df[trait_df[trait_df['GROUP'] == 'obese']['SAMPLE']]
ctrl_df = sample_df[trait_df[trait_df['GROUP'] == 'normal']['SAMPLE']]

# count the number of case and control for each SNP genotype
# case: (sample_df, path_output: case_df, /case_table)
# ctrl: (sample_df, path_output: ctrl_df, /ctrl_table)
def numberofsamples(sample_df, path_output):
    samplenames = list(sample_df)

    result = open(path_output, "w")
    # genotype(G:GG,AG,GT; A:AA,AG,AC; C:CC,CT,AC; T:TT,CT,GT)
    result.writelines('snp genotype count_homo count_heter1 count_heter2\n')

    for snp in sample_df['id']:
        count_homo = 0
        count_heter1 = 0
        count_heter2 = 0

        for item in samplenames:
            mn = sample_df[item][snp].str.split(':')
            # keep the snps which the genotype doesnt match the strongest snp-risk allele in the database
            if int(mn[0]) in N_genome[db[snp]]:
                while db[snp] == 'G':
                    if int(mn[0]) in genotype['GG']:
                       count_homo = count_homo + 1
                    if int(mn[0]) in genotype['AG']:
                       count__heter1 = count__heter1 + 1
                    if int(mn[0]) in genotype['GT']:
                       count_heter2 = count_heter2 + 1
                while db[snp] == 'A':
                    if int(mn[0]) in genotype['AA']:
                       count_homo = count_homo + 1
                    if int(mn[0]) in genotype['AG']:
                       count__heter1 = count__heter1 + 1
                    if int(mn[0]) in genotype['AC']:
                       count_heter2 = count_heter2 + 1
                while db[snp] == 'C':
                    if int(mn[0]) in genotype['CC']:
                       count_homo = count_homo + 1
                    if int(mn[0]) in genotype['CT']:
                       count__heter1 = count__heter1 + 1
                    if int(mn[0]) in genotype['AC']:
                       count_heter2 = count_heter2 + 1
                while db[snp] == 'T':
                    if int(mn[0]) in genotype['TT']:
                       count_homo = count_homo + 1
                    if int(mn[0]) in genotype['CT']:
                       count__heter1 = count__heter1 + 1
                    if int(mn[0]) in genotype['GT']:
                       count_heter2 = count_heter2 + 1
     result.writelines("%s %s %d %d %d\n"%(snp, db[snp], count_homo, count_heter1, count_heter2))
     result.close()


# split a column and return the df with multiple columns
def splitcolumn(coltobesplited, sep):
    splited_db = pd.DataFrame()
    splited = coltobesplited.str.split(sep)
    for n in range(0, len(splited[0])):
        a = []
        for i in range(0, len(coltobesplited)):
            a.append(splited[i][n])
        splited_db[n] = a
    return splited_db

# create the sample_df with only the genotype (new_sample_df)
new_samle_df <- pd.DataFrame(sample_df['id'],'snp')
for sample in list(sample_df) :
    splited_col = splitcolumn(sample_df[sample], ':')
    new_sample_df[sample] = splited_col


# get the number of heterozgyous and homozygous SNPs for every sample
# (sample_df, path_output: sample_df, count_snp)
def numberofsnps(sample_df, path_output):
    samplenames = list(sample_df)
    result = open(path_output, "w")
    result.writelines('samples heterozygous homozygous total\n')

    # count the number of number of heterozgyous and homozygous SNPs
    for item in samplenames:
        mn = splitcolumn(sample_df[item], ":")
        mn.index = sample_df.index
        heterozygous = 0
        homozygous = 0
        total = 0
        for snp in sample_df[id]:
            if snp in db.keys():
                before = mn.loc[snp][0]
                after = mn.loc[snp][1]
    # keep the snps which the genotype doesnt match the strongest snp-risk allele in the database
                if int(before) in N_genome[db[snp]]:
                    total = total+1
                    if int(after) == 2 or int(after) == 0:
                        homozygous = homozygous+1
                    else:
                        heterozygous = heterozygous+1
        if total != 0:
            result.writelines("%s %d %d %d\n"%(item, heterozygous, homozygous, total))
    result.close()
