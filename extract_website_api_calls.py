# %%
from requests_html import HTMLSession
from bs4 import BeautifulSoup
import requests
from selenium import webdriver
from deepdiff import DeepDiff

tesla_api = "https://auto-abonnement.centraalbeheer.nl/api/v1/VehicleVariation?Filters.Segment=Cars&Filters.Make=Tesla&Filters.Model=Model+3&Filters.IncludeTaxInPrices=false&Filters.NumberOfKmPerMonth=1000&Filters.IncludeMileageCostsInPricing=true&Filters.IncludeFuelCostsInPricing=false&SortBy=PriceInEuro&Filters.MaxPricePerMonth=1200&Filters.ActualBudgetPerMonth=1200"




# %%
# Full scrape : brands_overview_api -> check is brand + model is present -> scrape brand + model specific page url -> scrape api calls at brand + model specific page url -> use brand + model api call to get info -> extract info -> present info to person