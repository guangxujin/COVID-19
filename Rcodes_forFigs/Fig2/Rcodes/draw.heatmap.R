mkdir<-function(f){
  dir.create(file.path(f), showWarnings = FALSE)
}

args = commandArgs(trailingOnly=TRUE)

#table=read.table("cells.sam.statistics",sep='\t',header=F)
acc=args[1]

#source("Decorate.r") 
#library(pheatmap)
library(ggplot2)
library(RColorBrewer)
library(viridis)

f=paste0("../all.countries.hits")
table_r = read.table(f,sep='\t',header=T,row.names=1)
head(table_r)
data=table_r
f=paste0("../all.countries.hits.mean.txt")
col_r = read.table(f,sep='\t',header=F,row.names=1)
head(col_r)
library(ComplexHeatmap)
library(circlize)
library(gplots)
#library(scales)
library(dendextend)

head(table_r)
head(col_r)
col="deepskyblue2"

coln=30000
#f2=colorRamp2(seq(0,1,length = coln), colorpanel(coln,"black","yellow","yellow"), space = "RGB") 
f2=colorRamp2(c(0,1), c("yellow", "red"))
f2=colorRamp2(c(min(data), 0.1,max(data)-0.6), c(col, "white","red"))#rev(colorRampPalette(brewer.pal(11, "RdYlBu"))(2000))
row_ha = rowAnnotation(
  hit_total_score = anno_barplot(col_r[,1],
    gp = gpar(fill = 'red'),
    width = unit(4, "cm")))
heatmap_name='Blast_hits.'
row_dend = as.dendrogram(hclust(dist(t(as.matrix(data)))))
row_dend = color_branches(row_dend, k = 4)
ht1 = Heatmap(t(as.matrix(data)), 
  name = "ht1", 
  col = f2, 
  #row_split = factor(split,levels=c("D-low","D-high")),
  #row_split = factor(col_split,levels=c("exh","eff","mem")),
  column_km = 4,
  row_km = 4,
  #row_split = c(rep("III", "IV","II","I")
  #column_title = heatmap_name,
  cluster_rows = T, 
  cluster_columns = T, 
  show_row_names = T,
  show_column_names = T,
  show_column_dend = T,
  right_annotation = row_ha,
  border='black',
  rect_gp = gpar(col = "grey50", lwd = 1.5),
  #cluster_rows = dend,
  column_names_gp = gpar(fontsize = 7),
  #row_order = order(as.numeric(sort(marker[,2]))),

  #column_names_gp = gpar(fontsize = 6),
  #rect_gp = gpar(col = 'grey90'),
  #split=table[,2],
  #rect_gp = gpar(col = "white", lty = 2, lwd = 2)
  )

width = 10
heigth = 7
out_dir = '../plots/'
mkdir(out_dir)
prefix = heatmap_name
pdf(file.path(out_dir, paste0(prefix,'.', acc,".pdf")), w = width, h = heigth)
draw(ht1,heatmap_legend_side = "right")
dev.off()
