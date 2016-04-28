import json
import requests

def fibogetnum(inpnum,requesttype):
    """
    inpnum = any alphanumeric, requesttype = 'get','post','put','delete'
    returns the fibonacci number as int or service error message
    """
    hostip = '52.27.221.233'
    url = 'http://' + hostip + ':5000/api/fibonacci/' + str(inpnum)
    response = requests.request(requesttype,url)
    response_json = response.json()
    if requesttype == 'get':
        if 'fibonacci' in response_json:
            return int(response_json['fibonacci'])
        else:
            return response_json['error']
    else:
        return response_json['error']
    
def getfiboresp(inpnum,requesttype):
    """
    inpnum = any alphanumeric, requesttype = 'get','post','put','delete'
    returns the json response
    """
    hostip = '52.27.221.233'
    url = 'http://' + hostip + ':5000/api/fibonacci/' + str(inpnum)
    response = requests.request(requesttype,url)
    return response.json()

def findmaxtermfibo(maxelem):
    """
    maxelem: maximum term to check
    returns the maximum term returning a fibonacci number
    """
    counter = 0
    fibexist = 1
    while fibexist == 1 and counter <= maxelem: 
        json_response=getfiboresp(counter,'get')
        if 'fibonacci' in json_response:
            counter+=1
        else:
            fibexist = 0
    return counter-1

def getfibo_accuracy(maxterm):
    """
    maxterm: largest term that generated a fibonacci number
    returns the last term returning an accurate fibonacci number
    accurate defined as term(n) = term(n-1) + term(n-2)
    """
    counter = 0
    fibseries = []
    """ load list with fibonacci numbers from service """
    while counter <= maxterm: 
        fibseries.append(fibogetnum(counter,'get'))
        counter+=1
        
    """ compute accuracy of fibonacci terms """
    counter = 2
    while counter <= maxterm:
        if fibseries[counter] != fibseries[counter-1]+fibseries[counter-2]:
            break
        counter+=1
    return counter-1
