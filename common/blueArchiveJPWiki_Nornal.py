from bs4 import BeautifulSoup
import requests
import pandas as pd

class BlueArchiveNormal:

    def getNormalPic(self, pageStart, pageEnd, Ch):

        for page in range(pageStart, pageEnd):

            url = 'https://bluearchive.wikiru.jp/' + '?' + str(Ch) + '%E7%AB%A0/' + str(Ch) + '-' + str(page)

            response = requests.get(url)
            soup = BeautifulSoup(response.text, "html.parser")

            normalCh2 = url[42:44] + str(page)
            picTitles = soup.find_all("img", attrs={'title': 'N' + normalCh2 + '.jpg'})
            for picTitle in picTitles:
                ch2PicPath = picTitle['data-src']
                ch2PicUrl = 'https://bluearchive.wikiru.jp/' + ch2PicPath
                return ch2PicUrl


    def getNormalTable(self, pageStart, pageEnd, Ch):
        for page in range(pageStart, pageEnd):

            url = 'https://bluearchive.wikiru.jp/' + '?' + str(Ch) + '%E7%AB%A0/' + str(Ch) + '-' + str(page)

            response = requests.get(url)

            soup = BeautifulSoup(response.text, "html.parser")


            table = soup.find('div', {'id': 'rgn_content1'})
            columns = [th.text.replace('\n', '') for th in table.find('thead').find_all('th')]
            trs = table.find_all('tr')[1:]
            rows = list()
            for tr in trs:
                rows.append([td.text.replace('\n', '').replace('\xa0', '') for td in tr.find_all('td')])
            rows[:5]
            df = pd.DataFrame(data=rows, columns=columns)
            df.head()
            return df