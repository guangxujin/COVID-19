mkdir<-function(f){
  dir.create(file.path(f), showWarnings = FALSE)
}
library(RColorBrewer)
args = commandArgs(trailingOnly=TRUE)

#table=read.table("cells.sam.statistics",sep='\t',header=F)
data_input='../USA.hits.seq.count.txt'

col1=brewer.pal(12, "Paired")
col2=brewer.pal(10, "Set3")
col3=brewer.pal(10, "Set2")
colors=c(col1,col2,col3)
#cell="19_NTS_Wuhan"
#data_input="../SARS-COV2_raw/19_NTS_Wuhan_blast_uniq_country/19_NTS_Wuhan.country.statistics"
#cl="../SARS-COV2_raw/19_NTS_Wuhan_blast_uniq_country/19_NTS_Wuhan.country.mean.statistics"
table=read.table(data_input,sep='\t',header=F)
#table=rbind(table,table1)
table=table[order(-table[,2]),]
head(table)
library(ggplot2)
width = 3.5
heigth = 5
outdir = '../plots/'
mkdir(outdir)
prefix = "US_hit_count"
pdf(file.path(outdir, paste0(prefix, ".pdf")), w = width, h = heigth)
data=table
total=sum(data[,2])
data[,2]=data[,2]/total
colnames(data)=c("Genome","Hit_number")
data=data[1:25,]
data$Genome=factor(data$Genome,levels=table[,1])
ggplot(data, aes(x=Genome, y=Hit_number,width=0.6)) +
  geom_bar(stat="identity",color="blue",fill='blue')+
  #geom_jitter(shape=16, position=position_jitter(0.3),size=0.3)+
  #ylim(c(0,250))+
  xlab("SARS-Cov-2\nGenome from USA")+
  #ylab("Reference genome number")+
  #ggtitle(cell)+
  theme_classic()+
  #scale_color_gradient(low="cyan",high="red",limits=c(0,1),na.value='cyan')+
  theme(axis.text.x = element_text(angle = 90, hjust = 1))+
  #scale_fill_manual(values=colors)+
  theme(legend.position = "none")+
  scale_y_continuous(labels = scales::percent)
dev.off()

