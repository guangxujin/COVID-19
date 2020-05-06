mkdir<-function(f){
  dir.create(file.path(f), showWarnings = FALSE)
}

args = commandArgs(trailingOnly=TRUE)

#table=read.table("cells.sam.statistics",sep='\t',header=F)
cell=args[1]
data_input=args[2]
cl=args[3]
out=args[4]
#cell="19_NTS_Wuhan"
#data_input="../SARS-COV2_raw/19_NTS_Wuhan_blast_uniq_country/19_NTS_Wuhan.country.statistics"
#cl="../SARS-COV2_raw/19_NTS_Wuhan_blast_uniq_country/19_NTS_Wuhan.country.mean.statistics"
table=read.table(data_input,sep='\t',header=F)
#table=rbind(table,table1)
table_m=read.table(cl,sep='\t',header=F)
head(table)
head(table_m)
table_m=table_m[order(table_m[,2]),]
library(ggplot2)
width = 5
heigth = 5
outdir = out
mkdir(outdir)
prefix = ".covid_19_hit_countries"
pdf(file.path(outdir, paste0(cell,prefix, ".pdf")), w = width, h = heigth)
data=data.frame(table[,1],table[,5])
colnames(data)=c("Country","Hit_probability")
data$Country=factor(data$Country,levels=table_m[,1])
ggplot(data, aes(x=Country, y=Hit_probability,color=Country)) +
  geom_boxplot()+
  geom_jitter(shape=16, position=position_jitter(0.3),size=0.3)+
  #ylim(c(0,1))+
  ggtitle(cell)+
  theme_classic()+
  #scale_color_gradient(low="cyan",high="red",limits=c(0,1),na.value='cyan')+
  theme(axis.text.x = element_text(angle = 90, hjust = 1))
dev.off()

