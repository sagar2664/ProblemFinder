from bs4 import BeautifulSoup
import requests
import pandas as pd


def saveCsv(problems):
    df = pd.DataFrame(problems[1:], columns=problems[0])
    df.to_csv('problems.csv', index=False)

def webPage(url):
    re = requests.get(url)
    soup = BeautifulSoup(re.content, 'lxml')
    return soup

def fetchText(url):
    soup = webPage(url)
    try :
        text = soup.select_one("#pageContent > div.problemindexholder > div.ttypography > div > div:nth-child(2)").text
        text = text.replace('$', '')
    except Exception as _:
        text = ''
    return text

def fetch(url , sheet):
    soup = webPage(url)
    s = soup.findAll('tr')
    for i in (s):
        
        # Question Name
        name = i.find(attrs={'style': 'float: left;'})
        if(name is None):
           continue
        name = ((name.text).replace('\n', ''))[1:]
            
        # Question Tag
        tag = i.find(class_="notice")
        if (tag is not None):
            tag = tag.text
        else:
            tag = ''
        
        # Question URL
        qurl = i.find('a')['href']
        qurl = "https://leetcode.com"+qurl
        
        # Difficulty
        diff = i.find(class_="ProblemRating").text
        diff = int(diff)

        text = fetchText(qurl)
        
        # append to sheet
        sheet.append([name, qurl, tag, diff, text])
    return



def getProblems(problemUrl , order):
    soup = webPage(problemUrl+"?order="+order)

    # find the number of pages
    pages = soup.find('div', class_="pagination")
    pages = pages.find_all('li')
    pages = pages[-2].text
    pages = int(pages)
    print("Total pages:", pages)
    
    # List to store all the questions
    problems = [["Name", "URL", "Tag", "Difficulty", "Text"],]

    # Fetching data from each page
    for index in range(1 , pages+1):
        print(f"\n********Fetching Page {index}********")
        url = problemUrl+"/page/"+str(index)+"?order="+order
        fetch(url, problems)
        print("********Done********")
    
    # All fetched data and now creating excel sheet with the data
    print("*****Done all pages*****")
    print(f"Total {problems.__len__()} questions fetched")

    saveCsv(problems)
    return


if __name__ == "__main__":
    problemUrl = "https://leetcode.com/problemset"
    order = "BY_RATING_ASC"
    getProblems(problemUrl, order)

