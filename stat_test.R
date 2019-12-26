# input: SNPs genotype table for case and ctrl (case_table, ctrl_table)

# fisher extac test: figure out the association of genotype and clinical traits of each SNPs
# check out the genotype of those SNPs

# output:
# table of fisher exact test p value for all SNPs
# table of SNP genotype significantly occurred in case group

names(sample_df)[colnames(sample_df) =='id'] <- 'snp'

case <- read.csv2('/case_table', sep = '/t')
ctrl <- read.csv2('/ctrl_table', sep = '/t')

# create contingency table for each SNP
# figure out in which SNP, the SNP genotype is associated with the clinical traits
# output: snp_list
p_value <- c()
for (snp in case['snp']) {
    case <- case[case['snp' == snp], ]
    ctrl <- ctrl[ctrl['snp' == snp], ]
    df <- matrix(c(case['count_homo'], case['count_heter1'], case['count_heter2'],
                   ctrl['count_homo'], ctrl['count_heter1'], ctrl['count_heter2']),
                   ncol = 2)
    snp_list <- c()
    test <- fisher.test(df)
    p_value <- c(p_value, test$p.value)
    if (test$p.value < 0.05) {
        snp_list <- c(snp_list, snp)
    }
}
test_df <- c(case['snp'], p_value)
colnames(test_df) <- ('snp', 'p_value')

# check out the genotype of those SNPs in both case and contrl group
new_case <- case[case[,'snp'] %in% snp_list, ]
new_ctrl <- ctrl[ctrl[,'snp'] %in% snp_list, ]

# genotype(G:GG,AG,GT; A:AA,AG,AC; C:CC,CT,AC; T:TT,CT,GT)
df_pre <- function(df) {
    if (df['genotype'] == 'G') {
        colnames(df) <- c('snp', 'genotype', 'GG', 'AG', 'GT')
    }
    if (df['genotype'] == 'A') {
        colnames(df) <- c('snp', 'genotype', 'AA', 'AG', 'AC')
    }
    if (df['genotype'] == 'C') {
        colnames(df) <- c('snp', 'genotype', 'CC', 'CT', 'AC')
    }
    if (df['genotype'] == 'T') {
        colnames(df) <- c('snp', 'genotype', 'TT', 'CT', 'GT')
    }
    df <- df[-c(1,2)]
    return(df)
}

new_case <- df_pre(new_case)
new_ctrl <- df_pre(new_ctrl)

genotype_case <- c()
for (snp in snp_list) {
    col <- colnames(new_case[max(new_case)])
    genotype_case <- c(genotype_case, col)
}

genotype_ctrl <- c()
for (snp in snp_list) {
    col <- colnames(new_ctrl[max(new_ctrl)])
    genotype_ctrl <- c(genotype_ctrl, col)
}

genotype <- data.frame(snp_list, genotype_case, genotype_ctrl)
colnames(genotype) <- c('SNP', 'case', 'contrl')











