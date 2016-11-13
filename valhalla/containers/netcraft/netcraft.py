from bs4 import BeautifulSoup
from urllib import request
from random import randint
import time
import sys
import argparse
import re

def main():
    parser = argparse.ArgumentParser(description='Netcraft Scraper Script')
    parser.add_argument('-H', '--host', help='hostname to scan', required=True)
    args = parser.parse_args()
    info = {}
    with request.urlopen('http://toolbar.netcraft.com/site_report?url='+ args.host) as response:
        html = response.read()
        soup = BeautifulSoup(html, "html.parser")

        print('[ ', args.host, ' fingerprint ', ' ]')
        background_rows = soup.find('section', {"id" : 'background_table'})\
            .find('table', {"class":"TBtable"}).find_all('tr')

        if background_rows:
            background = ''
            for row in background_rows:
                headers = row.find_all('th')
                tds     = row.find_all('td')
                for header, td in zip(headers, tds):
                    background += header.get_text() + ' - ' + td.get_text().strip() + '\n'
            print(background)

        network_rows = soup.find('section', {"id" : 'network_table'})\
            .find('table', {"class":"TBtable"}).find_all('tr')

        if network_rows:
            network_info = ''
            for row in network_rows:
                headers = row.find_all('th')
                tds = row.find_all('td')
                for header, td in zip(headers, tds):
                    if (header.get_text() == 'Latest Performance') : continue
                    network_info += header.get_text() + ' - ' + td.get_text().strip() + '\n'
            print(network_info)

        last_reboot = soup.find('section', {"id": 'last_reboot'})
        if last_reboot:
            span = last_reboot.find('h2').find('span')
            print('Last reboot', '-' ,re.sub('[()]', '', span.get_text()))

        hosting_rows = soup.find('section', {"id": 'history_table'}) \
            .find('table', {"class": "TBtable"})

        if hosting_rows:
            headers = hosting_rows.find('thead').find('tr').find_all('th')
            host_info = ''
            rows = hosting_rows.find('tbody').find_all('tr')
            for row in rows:
                tds = hosting_rows.find('tbody').find_all('td')
                for header, td in zip(headers, tds):
                    host_info += header.get_text() + ' - ' + td.get_text().strip() + ', '
                host_info = host_info[:-2] + '\n'

            print(host_info)

    time.sleep(randint(2,5))
    sys.exit(0)

if __name__ == "__main__":
    main()