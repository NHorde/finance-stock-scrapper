from state import State

def get_html(state: State):
    soup = BeautifulSoup(
        requests.get("https://finance.yahoo.com/quote/%s/key-statistics?p=%s" % (self.ticker, self.ticker)).content,
        'lxml')
    script = soup.find("script", text=re.compile("root.App.main")).text
    data = loads(re.search("root.App.main\s+=\s+(\{.*\})", script).group(1))
    state.url = data['context']['dispatcher']['stores']

def manager(state: State):
    """  
    :param state: 
    :type state: State
    :rtype: dict
    :return: object
    """
    try:
        result = get_html(state)
        print("good")
    except:
        result = "nice try"
        print("not good")
    return result

state = State()
print(state.url)
# manager(state = state)

