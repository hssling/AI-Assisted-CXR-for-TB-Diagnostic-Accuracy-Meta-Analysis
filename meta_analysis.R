# AI-TB Diagnostic Meta-Analysis
suppressPackageStartupMessages({
  library(readr)
  library(dplyr)
  library(ggplot2)
  library(glue)
  library(mada)
  library(metafor)
  library(meta)
  library(tidyr)
  library(gridExtra)
})

in_csv <- "projects/ai_tb_meta/data/extracted/studies_template.csv"
out_dir <- "projects/ai_tb_meta/outputs"
plot_dir <- file.path(out_dir,"plots")
dir.create(plot_dir, showWarnings=FALSE, recursive=TRUE)
tab_dir  <- file.path(out_dir,"tables")
dir.create(tab_dir,  showWarnings=FALSE, recursive=TRUE)

dat <- read.csv(in_csv, stringsAsFactors = FALSE)
dat$TP <- as.numeric(dat$TP)
dat$FP <- as.numeric(dat$FP)
dat$FN <- as.numeric(dat$FN)
dat$TN <- as.numeric(dat$TN)
dat <- dat[!is.na(dat$TP) & !is.na(dat$FP) & !is.na(dat$FN) & !is.na(dat$TN), ]

if (nrow(dat)<2) {
  writeLines("Not enough filled rows with 2x2 data. Please complete the template.")
  quit(save="no", status=0)
}

# Build mada object
mada_dat <- mada::madad(TP = dat$TP, FN = dat$FN, FP = dat$FP, TN = dat$TN, studlab = dat$study_id)

# Bivariate HSROC model
fit_biv <- try(mada::reitsma(mada_dat), silent=TRUE)

# Forest of sensitivity & specificity (separate RE using logit transform)
calc_logit <- function(x) log((x+0.5)/(1-x+0.5))
se_prop <- function(x,n) sqrt(1/((x+0.5)) + 1/((n-x)+0.5))

sens <- with(dat, TP/(TP+FN))
spec <- with(dat, TN/(TN+FP))
dat$sens <- sens
dat$spec <- spec

m_sens <- rma(measure="PLO", xi=dat$TP, mi=dat$TP+dat$FN, method="REML")
m_spec <- rma(measure="PLO", xi=dat$TN, mi=dat$TN+dat$FP, method="REML")

pred_sens <- transf.ilogit(predict(m_sens)$pred)
pred_spec <- transf.ilogit(predict(m_spec)$pred)

# Save pooled estimates
summary_csv <- file.path(tab_dir,"pooled_estimates.csv")
write.csv(data.frame(
  k=nrow(dat),
  pooled_sensitivity=pred_sens,
  pooled_specificity=pred_spec
), summary_csv, row.names=FALSE)

# Forest plots (sens/spec)
png(file.path(plot_dir,"forest_sensitivity.png"), width=1200, height=900, res=150)
forest(m_sens, slab=dat$study_id, xlab="Sensitivity (logit scale)")
dev.off()
png(file.path(plot_dir,"forest_specificity.png"), width=1200, height=900, res=150)
forest(m_spec, slab=dat$study_id, xlab="Specificity (logit scale)")
dev.off()

# SROC (if bivariate fit succeeded)
if (!inherits(fit_biv, "try-error")) {
  png(file.path(plot_dir,"sroc.png"), width=1200, height=900, res=150)
  plot(fit_biv, sroclwd=2, main="HSROC (bivariate) – AI-assisted CXR for TB")
  dev.off()
}

# PRISMA (simple counts only; you can refine numbers)
png(file.path(plot_dir,"prisma_placeholder.png"), width=1400, height=900, res=150)
plot.new()
title("PRISMA Diagram (placeholder)")
text(0.5,0.8,"Records identified via databases = ?", cex=1.2)
text(0.5,0.7,"Records after duplicates removed = ?", cex=1.2)
text(0.5,0.6,glue("Full-text articles assessed = {nrow(dat)}"), cex=1.2)
text(0.5,0.5,glue("Studies included in meta-analysis = {nrow(dat)}"), cex=1.2)
dev.off()

writeLines("✅ Meta-analysis complete. See outputs/plots & outputs/tables.")
