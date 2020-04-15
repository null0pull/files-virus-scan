import requests
from webbrowser import open 

print('Note that U must sign up to get api(key) for free or Contact With me Via InstaGram (ah_trojan) to get my own.')

gotows = input('Press[1] to gonna SignUp or Press[Enter] to pass : ')
if gotows == 1:
    open('https://www.virustotal.com/gui/join-us')
else:
    pass
#getAPIkey
apikey = str(input('Enter Your API Key : '))

#getFileToScan
print('Note That maxSize Must be 32 MB')
f = str(input('Enter Path ur file : '))

url = 'https://www.virustotal.com/vtapi/v2/file/scan'

params = {'apikey': apikey}

file = open(f , 'rb')

files = {'file': (f, file)}

response_resource = requests.post(url, files=files, params=params)

#print(response_resource.json())

def report():
    url = 'https://www.virustotal.com/vtapi/v2/file/report'
    params = {'apikey': apikey, 'resource': str(response_resource.json()['resource'])}

    response = requests.get(url, params=params)
    #print(response.json()) #>> For ALL Info

    print('Response Code : ',response.json()['response_code'])
    print('Verbose msg : ',response.json()['verbose_msg'])
    print('Scan date : ',response.json()['scan_date'])
    print('Total Engines : ',response.json()['total'])
    print('***** POSITIVES ***** : ',response.json()['positives'])
    if response.json()['positives'] == 0 :
        print('There\'s No Virus.')
        print('Nice Bro it\'s CLEEEEEEEEEAAAAAAAAAAAAAN')
    else:
        c = input('Enter y to see Result or n to Exit : ')
        if c == 'y':
            print('SCans : ',response.json()['scans'])
        elif c == 'n':
            exit()
    
report()
