mkdir<-function(f){
  dir.create(file.path(f), showWarnings = FALSE)
}
library(RColorBrewer)
args = commandArgs(trailingOnly=TRUE)

#table=read.table("cells.sam.statistics",sep='\t',header=F)
data_input='../all.countries.hits.mean.txt.cases.txt'

col1=brewer.pal(6, "Paired")
col2=brewer.pal(6, "Set3")
col3=brewer.pal(6, "Set2")
colors=c(col1,col2,col3)
#cell="19_NTS_Wuhan"
#data_input="../SARS-COV2_raw/19_NTS_Wuhan_blast_uniq_country/19_NTS_Wuhan.country.statistics"
#cl="../SARS-COV2_raw/19_NTS_Wuhan_blast_uniq_country/19_NTS_Wuhan.country.mean.statistics"
table=read.table(data_input,sep='\t',header=F)
#table=rbind(table,table1)
head(table)
library(ggplot2)
width = 5
heigth = 5
outdir = '../plots/'
mkdir(outdir)
prefix = "ref_countries_death_"
pdf(file.path(outdir, paste0(prefix, ".pdf")), w = width, h = heigth)
data=table
colnames(data)=c("Country","BTHS","Cases","Death")
data$Country=factor(data$Country,levels=table[,1])
ggplot(data, aes(x=BTHS, y=Death,color=Country)) +
  geom_point()+
  #geom_jitter(shape=16, position=position_jitter(0.3),size=0.3)+
  #ylim(c(0,250))+
  #ylab("Reference genome number")+
  #ggtitle(cell)+
  theme_classic()+
  #scale_color_gradient(low="cyan",high="red",limits=c(0,1),na.value='cyan')+
  #theme(axis.text.x = element_text(angle = 90, hjust = 1))+
  scale_color_manual(values=colors)+
  theme(legend.position = "none")+
  geom_smooth(method=lm,  linetype="dashed",
             color="darkred", fill="blue")+
  theme(legend.position="right")
dev.off()
cor.test(data$BTHS,data$Death)

