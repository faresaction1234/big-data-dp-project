library(rvest)

link <- "https://steamcommunity.com/app/256460/reviews/?p=1&browsefilter=toprated"

review <- read_html(link) %>%
  html_nodes("div.apphub_CardTextContent") %>%
  html_text()

opinion <- read_html(link) %>%
  html_nodes("div.title") %>%
  html_text()

hoursplayed <- read_html(link) %>%
  html_nodes("div.hours") %>%
  html_text()

helpful <- read_html(link) %>%
  html_nodes("div.found_helpful") %>%
  html_text()

date <- read_html(link) %>%
  html_nodes("div.date_posted") %>%
  html_text()

tab <- data.frame("Posted" = date, "Review" = review, "Opinion" = opinion, "Hours Played" = hoursplayed, "Number of helpful vote" = helpful)
library('xlsx')
write.xlsx(tab, 'C:/Users/MFBA/Documents1/big data dp project/Web scrapping/data/input.xlsx', sheetName = "dataset", 
           col.names = TRUE, row.names = TRUE, append = FALSE)

