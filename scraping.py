import requests
from bs4 import BeautifulSoup
import pandas as pd
import re


# Function to scrape Stocktitan
def scrape_stocktitan():
    print("Scraping StockTitan...")
    base_url = "https://www.stocktitan.net"
    url = base_url + "/scanner/momentum"

    columns = ['name', 'change', 'source']
    df = pd.DataFrame(columns=columns)

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
    }
    response = requests.get(url, headers=headers)
    if response.status_code != 200:
        print(f"Failed to retrieve StockTitan page. Status code: {response.status_code}")
        return df

    soup = BeautifulSoup(response.content, "html.parser")
    top_gainers_div = soup.find("div", {"id": 'gainers'})
    top_gainers_table = top_gainers_div.find("div", {"class": 'body'}).find_all("div", {'class': 'content'})

    print(f"StockTitan: Found {len(top_gainers_table)} items.")
    for i in range(min(6, len(top_gainers_table))):
        name_news_div = top_gainers_table[i].find("div", {'class': 'symbol'})
        stock = name_news_div.get_text().split(':')[0].strip() if name_news_div else None
        card_info_divs = top_gainers_table[i].find("div", {'class': "data-group"})
        change_span = card_info_divs.find('span', {'class': 'price-change-ratio'})
        if change_span:
            change = change_span.get_text().replace(r"\r\n", '')
            change_num = float(re.sub(r'[,+%]', '', change))
            print(f"StockTitan - stock: {stock}, change: {change_num}")
            df = pd.concat([df, pd.DataFrame([{'name': stock, 'change': change_num, 'source': 'StockTitan'}])], ignore_index=True)
    return df


# Function to scrape StockAnalysis
def scrape_stockanalysis():
    print("Scraping StockAnalysis...")
    base_url = "https://stockanalysis.com/"
    url = base_url + "/markets/gainers/"

    columns = ['name', 'change', 'source']
    df = pd.DataFrame(columns=columns)

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
    }
    response = requests.get(url, headers=headers)
    if response.status_code != 200:
        print(f"Failed to retrieve StockAnalysis page. Status code: {response.status_code}")
        return df

    soup = BeautifulSoup(response.content, "html.parser")
    gainers_table = soup.find('table', {'id': 'main-table'})
    table_rows = gainers_table.find_all('tr')
    print(f"StockAnalysis: Found {len(table_rows)} rows.")
    for i in range(1, min(7, len(table_rows))):
        cols_in_row = table_rows[i].find_all('td')
        if len(cols_in_row) >= 4:
            name = cols_in_row[1].get_text()
            change = cols_in_row[3].get_text()
            change_num = float(re.sub(r'[,+%]', '', change))
            print(f"StockAnalysis - stock: {name}, change: {change_num}")
            df = pd.concat([df, pd.DataFrame([{'name': name, 'change': change_num, 'source': 'StockAnalysis'}])], ignore_index=True)
    return df



def get_price_volume_stockanalysis(stock_list: list):
    
    columns = ['name', 'price', 'volume']
    df = pd.DataFrame(columns=columns)

    for stock in stock_list:
        
        # print("stock: ",stock)
        url = f'https://stockanalysis.com/stocks/{stock}/'

        # Send a GET request to the URL
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
        }
        response = requests.get(url, headers=headers)

        # Check if request was successful
        if response.status_code != 200:
            print(f"Failed to retrieve the page. Status code: {response.status_code}")
            exit()
            new_row = {'name': stock,
                    'price': None,
                    'volume': None}
            df = pd.concat([df, pd.DataFrame([new_row])], ignore_index=True)
        
        else:
            soup = BeautifulSoup(response.content, "html.parser")
            price_table = soup.find('table', {'data-test': 'overview-quote'}).find_all("tr")

            len(price_table)

            price = None
            volume = None
            for row in price_table:
                cols = row.find_all('td')
                if cols[0].get_text() == "Previous Close":
                    price = cols[1].get_text()
                
                elif cols[0].get_text() == "Volume":
                    volume = cols[1].get_text()
            
            new_row = {'name': stock,
                    'price': price,
                    'volume': volume}
            df = pd.concat([df, pd.DataFrame([new_row])], ignore_index=True)

    return df



def get_details_stocktitan(stock_list:list):

    columns = ['name', 'market_cap','float', 'short_percent', 'industry', 'sector', 'country', 'news_link','news_impact_star', 'news_sentiment_star']
    df = pd.DataFrame(columns=columns)

    for stock in stock_list:
    
        url = f"https://www.stocktitan.net/news/{stock}/"
        # Send a GET request to the URL
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
        }
        response = requests.get(url, headers=headers)

        # Check if request was successful
        if response.status_code != 200:
            print(f"Failed to retrieve the page. Status code: {response.status_code}")
            exit()
            new_row = {
            'name': stock,
            'market_cap': None,
            'float': None,
            'short_percent': None,
            'industry': None,
            'sector': None,
            'country': None,
            'news_link': None,
            'news_impact_star': None,
            'news_sentiment_star': None
            }

            df = pd.concat([df, pd.DataFrame([new_row])], ignore_index=True)
        
        else:
            # Parse the HTML content using BeautifulSoup
            soup = BeautifulSoup(response.content, "html.parser")
            
            stock_data_div = soup.find_all('div', {'class': 'article-data-panel'})[-1].find_all('div',{'class': 'news-list-item stock-data'})

            market_cap_value = None
            float_value = None
            short_percent = None
            industry = None
            sector = None
            country = None

            for div in stock_data_div:
                # print(div.find('label').get_text())
                # print("==========================")
                if div.find('label').get_text() == "Short Percent":
                    short_percent = div.find('span').get_text()
                
                elif div.find('label').get_text() == "Industry":
                    industry = div.find('span').get_text()

                elif div.find('label').get_text() == "Sector":
                    sector = div.find('span').get_text()

                elif div.find('label').get_text() == "Country":
                    country = div.find('span').get_text()

                elif div.find('label').get_text() == "Market Cap":
                    market_cap_value = div.find('span').get_text()

                elif div.find('label').get_text() == "Float":
                    float_value = div.find('span').get_text()

            news_impact_star = len(soup.find('div', {'class': 'impact-container'}).find_all('div',{'class': 'full'}))
            news_sentiment_star = len(soup.find('div', {'class': 'sentiment-container'}).find_all('div',{'class': 'full'}))

            new_row = {
            'name': stock,
            'market_cap': market_cap_value,
            'float': float_value,
            'short_percent': short_percent,
            'industry': industry,
            'sector': sector,
            'country': country,
            'news_link': url,
            'news_impact_star': news_impact_star,
            'news_sentiment_star': news_sentiment_star
            }

            df = pd.concat([df, pd.DataFrame([new_row])], ignore_index=True)
    return df