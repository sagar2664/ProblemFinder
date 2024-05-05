from bs4 import BeautifulSoup
import requests

def webPage(url):
    re = requests.get(url)
    soup = BeautifulSoup(re.content, 'lxml')
    return soup


def fetchPageData(pageUrl, Queslist):
    newSoup = webPage(pageUrl)

    if(newSoup is None): 
        return
    #the block of questions div
    questionBlock = newSoup.find('div', role='rowgroup')
    #all the questions div in the block
    questionList = questionBlock.find_all('div', role='row')

    for question in questionList:
        row = question.find_all('div', role='cell')
        questionName = row[1].find('a').text.split(". ")[1]
        questionUrl = row[1].find('a')['href']
        questionUrl = 'https://leetcode.com' + questionUrl
        questionDifficulty = row[4].find('span').text
        
        Queslist.append([questionName, questionUrl, questionDifficulty])
        
    print("********Done*********")

    return


def getData(siteUrl):
    # List to store all the questions
    question = [["Question Name", "Question Url", "Question Difficulty"],]

    # Opening browser with Headless mode and wait for 2 seconds for page to load and fetch the html of page
    soup = webPage(siteUrl)
    if(soup is None):
        return
    # Fetching total number of pages
    totalPage = soup.find_all(class_ = "flex items-center justify-center px-3 h-8 rounded select-none focus:outline-none bg-fill-3 dark:bg-dark-fill-3 text-label-2 dark:text-dark-label-2 hover:bg-fill-2 dark:hover:bg-dark-fill-2")
    totalPage = totalPage[-2].text
    totalPage = int(totalPage)
    print(f"Total {totalPage} pages available")

    # Fetching data from each page
    for page in range(1, totalPage + 1):
        print(f"\n********Fetching Page {page}********")
        pageUrl = siteUrl + '?page=' + str(page)
        fetchPageData(pageUrl, question)

    # All fetched data and now creating excel sheet with the data
    print("*****Done all pages*****")
    print(f"Total {question.__len__()} questions fetched")



siteUrl = 'https://leetcode.com/problemset/'
getData(siteUrl)
