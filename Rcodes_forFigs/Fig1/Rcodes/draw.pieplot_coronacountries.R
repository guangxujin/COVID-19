mkdir<-function(f){
  dir.create(file.path(f), showWarnings = FALSE)
}




library(RColorBrewer)
args = commandArgs(trailingOnly=TRUE)

#table=read.table("cells.sam.statistics",sep='\t',header=F)
data_input='../covid_ref.count.txt.clean.txt'

col1=brewer.pal(12, "Paired")
col2=brewer.pal(10, "Set3")
col3=brewer.pal(6, "Set2")
col4=brewer.pal(6, "Set1")
colors=c(col1,col2,col3,col4)
#cell="19_NTS_Wuhan"
#data_input="../SARS-COV2_raw/19_NTS_Wuhan_blast_uniq_country/19_NTS_Wuhan.country.statistics"
#cl="../SARS-COV2_raw/19_NTS_Wuhan_blast_uniq_country/19_NTS_Wuhan.country.mean.statistics"
table=read.table(data_input,sep='\t',header=F)
#table=rbind(table,table1)
library(ggplot2)
library(scales)
width = 6
heigth = 4
outdir = '../plots/'
mkdir(outdir)
prefix = "NCBI_countries_count.pie.withlabels"
pdf(file.path(outdir, paste0(prefix, ".pdf")), w = width, h = heigth)
data=table
data=data[order(data[,2]),]
head(data)
colnames(data)=c("Country","Count")
data$Country=factor(data$Country,levels=data[,1])
value=data[,2]
ggplot(data, aes(x=factor(1), y=Count,fill=Country)) +
  geom_bar(stat="identity")+ coord_polar("y", start=0)+
  #geom_jitter(shape=16, position=position_jitter(0.3),size=0.3)+
  #ylim(c(0,250))
  scale_fill_manual(values=colors)+
  theme(axis.text.x=element_blank(),
    axis.text.y=element_blank()) +
  #axis.text.y=element_blank())
  geom_text(aes(label = paste(round(Count / sum(Count) * 100, 1), "%")),
            position = position_stack(vjust = 0.5),color='black') +
  theme(
  axis.title.x = element_blank(),
  axis.title.y = element_blank(),
  panel.border = element_blank(),
  panel.grid=element_blank(),
  axis.ticks = element_blank(),
  plot.title=element_text(size=12, face="bold"))
dev.off()

