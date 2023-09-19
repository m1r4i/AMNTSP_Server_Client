import socket

AmaneGender = "Boy"
AmaneMood = "Happy"


def res400(data,header_parts):
    data+="400 e? AMNTSP/1.0\r\n"
    for k,v in header_parts.items():
        data+=str(k)+":"+str(v)+"\r\n"
    data+="\r\n400 e? - リクエストが間違ってるみたい!\r\n"

    return data

def res418(data,header_parts):
    data+="418 I am Amane AMNTSP/1.0\r\n"
    for k,v in header_parts.items():
        data+=str(k)+":"+str(v)+"\r\n"
    data+="\r\n418 I am Amane - プロトコルが間違ってるみたい!\r\n"

    return data


def res200(data,header_parts):
    data+="200 Hello AMNTSP/1.0\r\n"
    for k,v in header_parts.items():
        data+=str(k)+":"+str(v)+"\r\n"
    data+="\r\nこんにちは!\r\n"

    return data

def res201(data,header_parts):
    data+="201 Awawawa AMNTSP/1.0\r\n"
    for k,v in header_parts.items():
        data+=str(k)+":"+str(v)+"\r\n"
    data+="\r\nうわっ…！！\r\n"

    return data

def res202(data,header_parts):
    data+="202 Wa-i AMNTSP/1.0\r\n"
    for k,v in header_parts.items():
        data+=str(k)+":"+str(v)+"\r\n"
    data+="\r\nよかった戻れたーー！！\r\n"

    return data

def res203(data,header_parts):
    data+="203 Ehehe AMNTSP/1.0\r\n"
    for k,v in header_parts.items():
        data+=str(k)+":"+str(v)+"\r\n"
    data+="\r\nわーい\r\n"

    return data


def res300(data,location):
    header_parts = {
        'Content-Type' : 'message/yuika',
        'Location': location,
    }

    data+="300 Acchi-iruyo AMNTSP/1.0\r\n"
    for k,v in header_parts.items():
        data+=str(k)+":"+str(v)+"\r\n"
    data+="\r\n今は違うとこにいるみたい〜\r\n"

    return data

def res401(data,header_parts):
    data+="401 Ya-dayo AMNTSP/1.0\r\n"
    for k,v in header_parts.items():
        data+=str(k)+":"+str(v)+"\r\n"
    data+="\r\n残念でしたー！！\r\n"

    return data

def res460(data,header_parts):
    data+="460 Cho-chotto AMNTSP/1.0\r\n"
    for k,v in header_parts.items():
        data+=str(k)+":"+str(v)+"\r\n"
    data+="\r\nちょっと痛いーー\r\n"

    return data

def res500(data,header_parts):
    data+="500 Internal Server Error AMNTSP/1.0\r\n"
    for k,v in header_parts.items():
        data+=str(k)+":"+str(v)+"\r\n"
    data+="\r\n...\r\n"

    return data

def res503(data,header_parts):
    data+="503 Hehe-n AMNTSP/1.0\r\n"
    for k,v in header_parts.items():
        data+=str(k)+":"+str(v)+"\r\n"
    data+="\r\nざんねーーん！！\r\n"

    return data

def res560(data,header_parts):
    data+="560 E-usodesyo!? AMNTSP/1.0\r\n"
    for k,v in header_parts.items():
        data+=str(k)+":"+str(v)+"\r\n"
    data+="\r\n「戻ってない！？！？」(スマホのインカメを見ながら)\r\n"

    return data


def getHost(uri):
    for f in uri.split("\r\n"):
        if f.find('Host:') != -1:
            host = f.replace("Host: ","");

    return host

def getGender(uri):
    for f in uri.split("\r\n"):
        if f.find('Gender:') != -1:
            host = f.replace("Gender: ","");

    return host

def getCount(uri):
    for f in uri.split("\r\n"):
        if f.find('Count:') != -1:
            host = f.replace("Count: ","");

    return host


def detect_method(uri):
    global AmaneGender
    global AmaneMood

    data=""
    header_parts = {
        'Content-Type' : 'message/amane',
        'Gender': AmaneGender,
        'mood': AmaneMood
    }


    serial = 0
    if len(uri.replace("amnts://","").split(" ")[1].split("/")) == 2:
        serial = uri.replace("amnts://","").split(" ")[1].split("/")[1]
    else:
        return res400(data,header_parts)


    if uri.find('Host:') == -1:
        return res400(data,header_parts)

    host = getHost(uri)


    if 'GET' in uri:
        res200(data,header_parts)
    elif 'CHANGE' in uri:
        gender = ""
        if uri.find('Gender:') == -1:
            return res400(data,header_parts)
        gender = getGender(uri)

        if gender == "Girl":
            AmaneGender = "Girl"
            AmaneMood ="Panic"
            header_parts = {
                'Content-Type' : 'message/amane',
                'Gender': AmaneGender,
                'mood': AmaneMood
            }

            return res201(data,header_parts)

        elif gender == "Boy":
            AmaneGender = "Boy"
            AmaneMood = "Happy"
            header_parts = {
                'Content-Type' : 'message/amane',
                'Gender': AmaneGender,
                'mood': AmaneMood
            }
            return res202(data,header_parts)

        else:
            return res400(data,header_parts)
    elif 'NADENADE' in uri:
        if uri.find('Count:') == -1:
            return res400(data,header_parts)

        count = getCount(uri)
        try:
            int(count)
        except:
            return res400(data,header_parts)

        if int(count) < 20:
            AmaneMood = "Fancy"
            return res203(data,header_parts)
        else:
            AmaneMood = "Angry"
            return res460(data,header_parts)

    else:
        return res400(data,header_parts)


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind(('127.0.0.1', 50007))
    s.listen(1)
    while True:
        conn, addr = s.accept()
        with conn:
            while True:
                data = conn.recv(1024)
                if not data:
                    break
                query = data.decode('utf-8','replace')
                if query.find('AMNTSP') != -1 and query.find('amnts') != -1:
                    res = detect_method(query)
                    print(query)
                else:
                    data=""
                    header_parts = {
                        'Content-Type' : 'message/amane',
                        'Gender': AmaneGender,
                        'mood': AmaneMood
                    }

                    res = res418(data,header_parts);

                if query.find('HTTP') != -1:
                    data="HTTP/1.1 400 Bad Request\r\n"
                    header_parts = {
                        'Content-Type' : 'text/html',
                        'Gender': AmaneGender,
                        'mood': AmaneMood,
                        'AMNTSP Status': '418 I am Amane'
                    }
                    for k,v in header_parts.items():
                        data+=str(k)+": "+str(v)+"\r\n"
                    data+="\r\n<meta charset=\"utf-8\" />HTTPではリクエストを処理できません。<br>AMNTSPを利用してください。<br><a href=\"https://m1r4i.com/AMNTSP/AMNTSP.html\">Docs</a>\r\n"

                    res = data


                conn.sendall(res.encode())