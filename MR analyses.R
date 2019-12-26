library(dplyr)
library(TwoSampleMR)

# df <- read.csv("/linear_cis.txt", sep = "\t", header = FALSE, stringsAsFactors = FALSE)

# snp
snp <- separate(df, df$V1, sep = '_', c(".", ".", 'SNP'))['SNP']

# effect size
effect_size <- df$V7

#effect allele
gwas_df = list(set(gwas_df))
effect_allele <- c()
for (i in snp) {
    allele <- gwas_df[gwas_df['SNPS'] == i, "STRONGEST SNP-RISK ALLELE"]
    effect_allele <- c(effect_allele, allele)
}

# exposure data
# 'exp_file'
exp_dat <- read_exposure_data(
    filename = exp_file,
    sep = "/t",
    snp_col = "snp",
    beta_col = "effect_size",
    se_col = "SE",
    effect_allele_col = "effect_allele"
)

# outcome data
# GWAS summary data from database  “gwas_summary.csv”
outcome_dat <- read_outcome_data(
    snps = bmi_exp_dat$SNP,
    filename = "gwas_summary.csv",
    sep = ",",
    snp_col = "rsid",
    beta_col = "effect",
    se_col = "SE",
    effect_allele_col = "a1",
    other_allele_col = "a2",
    eaf_col = "a1_freq",
    pval_col = "p-value",
    units_col = "Units",
    gene_col = "Gene",
    samplesize_col = "n"
)

# Harmonise data
dat <- harmonise_data(
    exposure_dat = exp_dat,
    outcome_dat = outcome_dat
)

# Perform MR
res <- mr(dat)

# scatter plot: relationship of the SNP effects on the exposure against the SNP effects on the outcome using a scatter plot.
p1 <- mr_scatter_plot(res, dat)











