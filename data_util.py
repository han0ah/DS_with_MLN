import json
import urllib

def get_nlp_parse_result(text):
    '''
    주어진 텍스트에 대해서 ETRI 텍스트 분석 결과를 반환한다. 
    '''
    etri_pos_url = 'http://143.248.135.20:22334/controller/service/etri_parser '
    data = "sentence="+text
    try:
        req = urllib.request.Request(etri_pos_url, data=data.encode('utf-8'))
        response = urllib.request.urlopen(req)
        result = response.read().decode('utf-8')
        result = json.loads(result)
    except:
        #print('error text : ' + text)
        return None
    return result