from bs4 import BeautifulSoup
import requests
import pandas as pd

class BlueArchiveNormal:

    def getNormalPic(self, pageStart, pageEnd, Ch):

        for page in range(pageStart, pageEnd):

            url = 'https://bluearchive.wikiru.jp/' + '?' + str(Ch) + '%E7%AB%A0/' + str(Ch) + '-' + str(page)

            response = requests.get(url)
            soup = BeautifulSoup(response.text, "html.parser")

            if Ch == 10:
                missionCh = url[43:46] + str(page)
                picTitles = soup.find_all("img", attrs={'title': 'N' + missionCh + '.jpg'})
                for picTitle in picTitles:
                    chPicPath = picTitle['data-src']
                    chPicUrl = 'https://bluearchive.wikiru.jp/' + chPicPath
                    return chPicUrl
            elif Ch < 10:
                missionCh = url[42:44] + str(page)
                picTitles = soup.find_all("img", attrs={'title': 'N' + missionCh + '.jpg'})
                for picTitle in picTitles:
                    chPicPath = picTitle['data-src']
                    chPicUrl = 'https://bluearchive.wikiru.jp/' + chPicPath
                    return chPicUrl
            elif Ch > 10:
                missionCh = url[43:46] + str(page)
                picTitles = soup.find_all("img", attrs={'title': missionCh + '攻略' + '.jpg'})
                for picTitle in picTitles:
                    chPicPath = picTitle['data-src']
                    chPicUrl = 'https://bluearchive.wikiru.jp/' + chPicPath
                    return chPicUrl


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


    def getHardPic(self, pageStart, pageEnd, Ch):

        for page in range(pageStart, pageEnd):

            url = 'https://bluearchive.wikiru.jp/' + '?' + str(Ch) + '%E7%AB%A0/' + 'H' + str(Ch) + '-' + str(page)

            response = requests.get(url)
            soup = BeautifulSoup(response.text, "html.parser")

            if Ch == 10:
                missionCh = url[44:47] + str(page)
                picTitles = soup.find_all("img", attrs={'title': 'H' + missionCh + '.jpg'})
                for picTitle in picTitles:
                    chPicPath = picTitle['data-src']
                    chPicUrl = 'https://bluearchive.wikiru. jp/' + chPicPath
                    return chPicUrl
            elif Ch < 10:
                missionCh = url[43:45] + str(page)
                picTitles = soup.find_all("img", attrs={'title': 'H' + missionCh + '.jpg'})
                for picTitle in picTitles:
                    chPicPath = picTitle['data-src']
                    chPicUrl = 'https://bluearchive.wikiru.jp/' + chPicPath
                    return chPicUrl
            elif Ch > 10:
                missionCh = url[44:47] + str(page)
                picTitles = soup.find_all("img", attrs={'title': 'H' + missionCh + '攻略' + '.jpg'})
                for picTitle in picTitles:
                    chPicPath = picTitle['data-src']
                    chPicUrl = 'https://bluearchive.wikiru.jp/' + chPicPath
                    return chPicUrl


    def getHardTable(self, pageStart, pageEnd, Ch):

        for page in range(pageStart, pageEnd):

            url = 'https://bluearchive.wikiru.jp/' + '?' + str(Ch) + '%E7%AB%A0/' + 'H' + str(Ch) + '-' + str(page)

            response = requests.get(url)
            soup = BeautifulSoup(response.text, "html.parser")
            table = soup.find('div', {'id': 'rgn_content2'})
            columns = [th.text.replace('\n', '') for th in table.find('thead').find_all('th')]
            trs = table.find_all('tr')[1:]
            rows = list()

            for tr in trs:
                rows.append([td.text.replace('\n', '').replace('\xa0', '') for td in tr.find_all('td')])
            rows[:5]
            print(rows[:5])
            df = pd.DataFrame(data=rows, columns=columns)
            df.head()
            return df
