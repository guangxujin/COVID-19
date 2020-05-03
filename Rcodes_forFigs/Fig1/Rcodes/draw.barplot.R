mkdir<-function(f){
  dir.create(file.path(f), showWarnings = FALSE)
}
library(RColorBrewer)
args = commandArgs(trailingOnly=TRUE)

#table=read.table("cells.sam.statistics",sep='\t',header=F)
data_input='../covid_customized.ref.count.txt.country_num.txt'

col1=brewer.pal(12, "Paired")
col2=brewer.pal(10, "Set3")
col3=brewer.pal(8, "Set2")
col4=brewer.pal(8, "Set1")
colors=c(col1,col2,col3,col4)
#cell="19_NTS_Wuhan"
#data_input="../SARS-COV2_raw/19_NTS_Wuhan_blast_uniq_country/19_NTS_Wuhan.country.statistics"
#cl="../SARS-COV2_raw/19_NTS_Wuhan_blast_uniq_country/19_NTS_Wuhan.country.mean.statistics"
table=read.table(data_input,sep='\t',header=F)
#table=rbind(table,table1)
library(ggplot2)
width = 2
heigth = 4
outdir = '../plots/'
mkdir(outdir)
prefix = "ref_countries_count"
pdf(file.path(outdir, paste0(prefix, ".pdf")), w = width, h = heigth)
data=table
data=data[order(data[,2]),]
head(data)
colnames(data)=c("Country","Count")
data$Country=factor(data$Country,levels=data[,1])
ggplot(data, aes(x=Country, y=Count,fill=Country)) +
  geom_bar(stat="identity")+
  #geom_jitter(shape=16, position=position_jitter(0.3),size=0.3)+
  #ylim(c(0,250))+
  ylab("Count")+
  #ggtitle(cell)+
  theme_classic()+
  #scale_color_gradient(low="cyan",high="red",limits=c(0,1),na.value='cyan')+
  theme(axis.text.x = element_text(angle = 90, hjust = 1))+
  scale_fill_manual(values=colors)+
  theme(legend.position = "none")+
  coord_flip()
dev.off()

