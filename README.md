# Genome Wide Identification of meQTLs in Whole Blood for Obesity 



## **Analysis Workflow**
1. **SNP genotyping association with clinical traits**

2. **Clustering the SNPs genotype pattern and count the heterozygous and homozygous calling** 

3. **Identification of causal CpGs for obesity via Two sample Mendelian Randomisation (2SMR)**

## **Input Files** 
### SNPs profiling for all samples 
| blood05_H035-030K | blood05_H035-031K   | blood05_H035-032K |   id      |
| ------------------|:-------------------:| -----------------:|----------:|
| 3:0               | 3:0                 | 3:0               | rs17541203|

### Clinical traits for all samples 
| Tables        | Are           | Cool  |
| ------------- |:-------------:| -----:|
| col 3 is      | right-aligned | $1600 |

### SNPs genotype mapping 
| Tables        | Are           | Cool  |
| ------------- |:-------------:| -----:|
| col 3 is      | right-aligned | $1600 |

### meQTLs for all SNPs
| Tables        | Are           | Cool  |
| ------------- |:-------------:| -----:|
| col 3 is      | right-aligned | $1600 |

### GWAS SNPs Summary data
| Tables        | Are           | Cool  |
| ------------- |:-------------:| -----:|
| col 3 is      | right-aligned | $1600 |

## Analysis Steps

### **1. Data Prepation** [df.py](https://github.com/leungman426/Genome-wide-identification-of-meQTLs/blob/master/df.py)

Output Files: 
- Count the heterzgyous and homozgyous SNPs
/
- Count the case and control samples for each SNP genotypes 
/
- Simplified SNPs profiling 
/

### **2. SNP genotyping association with clinical traits** [stat_test.R](https://github.com/leungman426/Genome-wide-identification-of-meQTLs/blob/master/stat_test.R)

Outputs:
- Fisher's exact test 
/
- SNPs' genotyptes significantly different between cases and controls 
/
### **3. Clustering the SNPs genotype pattern and count the heterozygous and homozygous calling**
Use the stacked bar plot with dendrogram: Hierachical clustering of SNPs genotypes (dengrogram) and countheterozygous and homozygous calling (bar plot)
[stacked barplot with dendrogram](https://github.com/leungman426/Stacked-Barplot-with-Dendrogram)
img

### **4. Identification of causal CpGs for obesity via Two sample Mendelian Randomisation (2SMR)**
[MR analyse.R](https://github.com/leungman426/Genome-wide-identification-of-meQTLs/blob/master/MR%20analyses.R)

2SMRwas used to identify putatively causal CpGs for obestiy.
Instrumental variable(IV): cis-meQTL SNPs; trans-meQTLs SNPs (anaylsed by ANOVA or Linear Regression)
*cis: a SNP is within 1Mb upstream or downstream of a CpG site; trans: a SNP is >1Mb away from a CpG site

Exposure data -> association of SNPs with CpGs 
/

Outcome data -> association of SNPs with obestiy (from [GWAS Catalog](https://www.genome.gov/genetics-glossary/Genome-Wide-Association-Studies))
/
Required R package: [TwoSampleMR](https://github.com/MRCIEU/TwoSampleMRm)

**steps:**
1. obtain **Exposure data** `read_exposure_data()`
2. obtain **Outcome data** `read_outcome_data()`
3. Harmonise data `harmonise_dataa()`
4. perfom MR `harmonise_data()`













