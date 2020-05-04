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
heatmap_name='Blast_hits.bytime.clustered.'
f=paste0("../all.countries.hits.with_collectiontime.txt")
table_r = read.table(f,sep='\t',header=T,row.names=1)
head(table_r)
colnames(table_r)
table_r=table_r[order(table_r[,1]),]
y=length(table_r)
data=table_r[,5:y]
f=paste0("../all.countries.hits.mean.txt")
col_r = read.table(f,sep='\t',header=F,row.names=1)
#col_r=col_r[colnames(data),]
library(ComplexHeatmap)
library(circlize)
library(gplots)
#library(scales)
library(dendextend)

head(data)
head(col_r)
print (dim(col_r))
print(dim(data))
print(dim(table_r))
#heatmap annotation

ha = HeatmapAnnotation(Date=table_r[,1],
  Country_city=table_r[,2],
  Country=table_r[,3],
  #sample=table_r$samp,
  #type=table_r$type,
  col=list(
    Date=c('2019-12'="red",
      "2020-01"="orange",
      "2020-02"="yellow",
      "2020-03"="green",
      "2020-04"="black"),
    Country_city=c('Australia'="#08306b",
      "Cambodia"="#08519c",
      "Canada"="#2171b5",
      'China-BGI'="#78c679",
      "China-Beijing"="#78c679",
      "China-Hongkong"="#41ab5d",
      "China-Hubei"="#006837",
      "China-Shenzhen"="#238443",
      "China-Wuhan"="#00441b",
      "Malaysia"="#4292c6",
      "Nepal"="#6baed6",
      "Peru"="#9ecae1",
      'USA--WI'="#662506",
      "USA-CA"="#fe9929",
      "USA-MD"="#fc4e2a",
      "USA-Utah"="#e31a1c",
      "USA-WA"="red",
      "USA-WI"="#662506",
      "USA-Yale"="#993404",
      "S.Africa"="#9ecae1"),
    Country=c('Australia'="cyan",
      "Cambodia"="cyan",
      "Canada"="cyan",
      'China'="darkgreen",
      "Malaysia"="cyan",
      "Nepal"="cyan",
      "Peru"="cyan",
      "S.Africa"="cyan",
      'USA'="red"
      )
    #type=c('front'="red","medium"="pink","back"="yellow","unsorted"="grey")
    )
  )


col="deepskyblue2"

coln=30000
#f2=colorRamp2(seq(0,1,length = coln), colorpanel(coln,"black","yellow","yellow"), space = "RGB") 
f2=colorRamp2(c(0,1), c("yellow", "red"))
dim(col_r)
f2=colorRamp2(c(min(data), 0.05,max(data)-0.1), c(col, "white","red"))#rev(colorRampPalette(brewer.pal(11, "RdYlBu"))(2000))
row_ha = rowAnnotation(
  BLAST_total_score = anno_barplot(col_r[,1],
    gp = gpar(fill = 'red'),
    width = unit(4, "cm")))

row_dend = as.dendrogram(hclust(dist(t(as.matrix(data)))))
row_dend = color_branches(row_dend, k = 4)

count=as.data.frame(table(table_r[,1]))
count
count[1,1]
col_split=c(rep('2019-12',count[1,2]),
  rep('2020-01',count[2,2]),
  rep('2020-02',count[3,2]),
  rep('2020-03',count[4,2]),
  rep('2020-04',count[5,2]))
col_split
ht1 = Heatmap(t(as.matrix(data)), 
  name = "ht1", 
  col = f2, 
  #row_split = factor(split,levels=c("D-low","D-high")),
  #row_split = factor(col_split,levels=c("exh","eff","mem")),
  column_km = 4,
  row_km = 4,
  #column_split = col_split,
  #column_title = heatmap_name,
  cluster_rows = T, 
  cluster_columns = T, 
  show_row_names = T,
  show_column_names = F,
  #show_column_dend = T,
  right_annotation = row_ha,
  top_annotation = ha,
  border='black',
  #rect_gp = gpar(col = "grey50", lwd = 1.5),
  #cluster_rows = dend,
  column_names_gp = gpar(fontsize = 7),
  #row_order = order(as.numeric(sort(marker[,2]))),

  #column_names_gp = gpar(fontsize = 6),
  #rect_gp = gpar(col = 'grey90'),
  #split=table[,2],
  #rect_gp = gpar(col = "white", lty = 2, lwd = 2)
  heatmap_legend_param = list(
    #legend_direction = "horizontal",
    legend_side="null",
    title = "Hit_score",
    legend_height = unit(2, "cm")
)


  )

width = 13.5
heigth = 6
out_dir = '../plots_customized/'
mkdir(out_dir)
prefix = heatmap_name
pdf(file.path(out_dir, paste0(prefix,'.', acc,".pdf")), w = width, h = heigth)
draw(ht1,heatmap_legend_side = "right")
dev.off()
