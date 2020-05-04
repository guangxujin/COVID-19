mkdir<-function(f){
  dir.create(file.path(f), showWarnings = FALSE)
}
library(RColorBrewer)
args = commandArgs(trailingOnly=TRUE)

#table=read.table("cells.sam.statistics",sep='\t',header=F)
data_input='../Fig1A.txt.removal_num.txt'

col1=brewer.pal(12, "Paired")
col2=brewer.pal(10, "Set3")
col3=brewer.pal(8, "Set2")
col4=brewer.pal(8, "Set1")
colors=c(col1,col2,col3,col4)
cbp2 <- c("#000000", "#E69F00", "#56B4E9", "#009E73",
          "#F0E442", "#0072B2", "#D55E00", "#CC79A7")
#cell="19_NTS_Wuhan"
#data_input="../SARS-COV2_raw/19_NTS_Wuhan_blast_uniq_country/19_NTS_Wuhan.country.statistics"
#cl="../SARS-COV2_raw/19_NTS_Wuhan_blast_uniq_country/19_NTS_Wuhan.country.mean.statistics"
table=read.table(data_input,sep='\t',header=F)
#table=rbind(table,table1)
library(ggplot2)
width = 6
heigth = 5
outdir = '../plots/'
mkdir(outdir)
prefix = "Fig1A."
pdf(file.path(outdir, paste0(prefix, ".pdf")), w = width, h = heigth)
data=table
#data=data[order(data[,2]),]
data
colnames(data)=c("Dataset","Sample_count","Platform","type")
data$Dataset=factor(data$Dataset,levels=unique(data$Dataset),ordered=TRUE)
ggplot(data, aes(x=Dataset, y=Sample_count,fill=Platform)) +
  geom_bar(stat="identity")+
  #geom_jitter(shape=16, position=position_jitter(0.3),size=0.3)+
  #ylim(c(0,250))+
  ylab("Sample count")+
  #ggtitle(cell)+
  theme_classic()+
  #scale_color_gradient(low="cyan",high="red",limits=c(0,1),na.value='cyan')+
  theme(axis.text.x = element_text(angle = 90, hjust = 1))+
  scale_fill_manual(values=cbp2)+
  theme(legend.position = "right")+
  coord_flip()
dev.off()

