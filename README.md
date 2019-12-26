# Genome Wide Identification of meQTLs in Whole Blood for Obesity 

## **Analysis Workflow**
1. **SNP genotyping association with clinical traits**

2. **Clustering the SNPs genotype pattern and count the heterozygous and homozygous calling** 

3. **Identification of causal CpGs for obesity via Two sample Mendelian Randomisation (2SMR)**

## **Input Files** 
### SNPs profiling for all samples 

### Clinical traits for all samples 

### SNPs genotype mapping 

### meQTLs for all SNPs

### GWAS SNPs Summary data

## Analysis Steps

### **Data Prepation** [df.py](https://github.com/leungman426/Genome-wide-identification-of-meQTLs/blob/master/df.py)

Output Files: 
- Count the heterzgyous and homozgyous SNPs

- Count the case and control samples for each SNP genotypes 

- Simplified SNPs profiling 


### **SNP genotyping association with clinical traits** [stat_test.R](https://github.com/leungman426/Genome-wide-identification-of-meQTLs/blob/master/stat_test.R)

Outputs:
- Fisher's exact test 

- SNPs' genotyptes significantly different between cases and controls 

### **Clustering the SNPs genotype pattern and count the heterozygous and homozygous calling**
Use the stacked bar plot with dendrogram: Hierachical clustering of SNPs genotypes (dengrogram) and countheterozygous and homozygous calling (bar plot)
[stacked barplot with dendrogram](https://github.com/leungman426/Stacked-Barplot-with-Dendrogram)









