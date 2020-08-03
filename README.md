## Price Tracker

This repository hosts a simple website to track driver and constructor prices for the F1 Fantasy league. It is updated every hour, except on race weekends (when teams are locked).

#### How it works

1. Running main.py starts a firefox selenium instance that logs into a dummy account. This then scrapes data from the F1 fantasy site after.
2. Data is parsed into a df and stored in an excel file.
3. Excel file is accessed, and graphed with matplot.
4. Update_markdown.py updates the index.md landing page.
5. Bash script pushes everything to this repo every hour, with the latest driver prices.

.


