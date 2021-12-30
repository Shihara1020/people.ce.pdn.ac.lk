# Create json file in _data/stud/*.json + download image using information taken from javascript code
#  https://cepdnaclk.github.io/department-website-2013/people/e08.html
# Author: E/18/098 Ishan Fernando - e18098@eng.pdn.ac.lk

# run js on site
"""
output = {};
list1 = document.getElementsByTagName("tr");
let count = 0;
for (let i = 0; i < list1.length; i=i+1) {
  output[count] = { name : list1[i].getElementsByTagName("th")[0].innerText , image : list1[i].getElementsByTagName("th")[1].getElementsByTagName("img")[0].src }
  count = count + 1;
  output[count] = { name : list1[i].getElementsByTagName("th")[3].innerText , image : list1[i].getElementsByTagName("th")[4].getElementsByTagName("img")[0].src }
  count = count + 1;
}
JSON.stringify(output)
"""

import urllib.request
import json


# the output,

outputFromJavaScript = """
{"0":{"name":"e05200 - G.L.C.B.MELRONI","image":"https://cepdnaclk.github.io/department-website-2013/people/images/e06/e05200.jpg"},"1":{"name":"e06007 - A.A.N.ADIKARI","image":"https://cepdnaclk.github.io/department-website-2013/people/images/e06/e06007.jpg"},"2":{"name":"e06009 - M.A.M.AJHAR","image":"https://cepdnaclk.github.io/department-website-2013/people/images/e06/e06009.jpg"},"3":{"name":"e06016 - D.G.D.L.AMITHASEKARA","image":"https://cepdnaclk.github.io/department-website-2013/people/images/e06/e06016.jpg"},"4":{"name":"e06020 - W.D.S.S.APPUHAMI","image":"https://cepdnaclk.github.io/department-website-2013/people/images/e06/e06020.jpg"},"5":{"name":"e06028 - K.BAHERATHAN","image":"https://cepdnaclk.github.io/department-website-2013/people/images/e06/e06028.jpg"},"6":{"name":"e06031 - A.N.P.BANDARA","image":"https://cepdnaclk.github.io/department-website-2013/people/images/e06/e06031.jpg"},"7":{"name":"e06034 - K.M.P.D.R.BANDARA","image":"https://cepdnaclk.github.io/department-website-2013/people/images/e06/e06034.jpg"},"8":{"name":"e06040 - P.B.N.B.BULUMULLA","image":"https://cepdnaclk.github.io/department-website-2013/people/images/e06/e06040.jpg"},"9":{"name":"e06041 - A.G.K.M.A.G.S.D.J.B.CHANDRASEKARA","image":"https://cepdnaclk.github.io/department-website-2013/people/images/e06/e06041.jpg"},"10":{"name":"e06047 - W.M.B.P.DASSANAYAKA","image":"https://cepdnaclk.github.io/department-website-2013/people/images/e06/e06047.jpg"},"11":{"name":"e06061 - K.M.A.C.B.DISSANAYAKE","image":"https://cepdnaclk.github.io/department-website-2013/people/images/e06/e06061.jpg"},"12":{"name":"e06063 - D.K.B.DODANWALA","image":"https://cepdnaclk.github.io/department-website-2013/people/images/e06/e06063.jpg"},"13":{"name":"e06068 - N.C.ELLEPOLA","image":"https://cepdnaclk.github.io/department-website-2013/people/images/e06/e06068.jpg"},"14":{"name":"e06073 - K.K.M.FERNANDO","image":"https://cepdnaclk.github.io/department-website-2013/people/images/e06/e06073.jpg"},"15":{"name":"e06075 - Y.A.GAJADEERA","image":"https://cepdnaclk.github.io/department-website-2013/people/images/e06/e06075.jpg"},"16":{"name":"e06080 - H.M.GUNARATHNE","image":"https://cepdnaclk.github.io/department-website-2013/people/images/e06/e06080.jpg"},"17":{"name":"e06081 - W.D.W.M.GUNASINGHE","image":"https://cepdnaclk.github.io/department-website-2013/people/images/e06/e06081.jpg"},"18":{"name":"e06090 - K.B.HERATH","image":"https://cepdnaclk.github.io/department-website-2013/people/images/e06/e06090.jpg"},"19":{"name":"e06091 - P.H.A.T.HETTIARACHCHI","image":"https://cepdnaclk.github.io/department-website-2013/people/images/e06/e06091.jpg"},"20":{"name":"e06104 - N.A.N.JAYARATHNE","image":"https://cepdnaclk.github.io/department-website-2013/people/images/e06/e06104.jpg"},"21":{"name":"e06105 - M.M.N.N.JAYASEKARA","image":"https://cepdnaclk.github.io/department-website-2013/people/images/e06/e06105.jpg"},"22":{"name":"e06110 - J.M.G.JAYASUNDARA","image":"https://cepdnaclk.github.io/department-website-2013/people/images/e06/e06110.jpg"},"23":{"name":"e06117 - K.G.J.M.JAYATHILAKE","image":"https://cepdnaclk.github.io/department-website-2013/people/images/e06/e06117.jpg"},"24":{"name":"e06137 - J.M.M.S.KULARATHNA","image":"https://cepdnaclk.github.io/department-website-2013/people/images/e06/e06137.jpg"},"25":{"name":"e06138 - C.K.P.I.KUMARA","image":"https://cepdnaclk.github.io/department-website-2013/people/images/e06/e06138.jpg"},"26":{"name":"e06145 - W.D.D.LALANTHA","image":"https://cepdnaclk.github.io/department-website-2013/people/images/e06/e06145.jpg"},"27":{"name":"e06154 - H.A.K.MADHUSANKHA","image":"https://cepdnaclk.github.io/department-website-2013/people/images/e06/e06154.jpg"},"28":{"name":"e06156 - H.D.C.MADURANGA","image":"https://cepdnaclk.github.io/department-website-2013/people/images/e06/e06156.jpg"},"29":{"name":"e06157 - L.S.K.K.D.MADURANGA","image":"https://cepdnaclk.github.io/department-website-2013/people/images/e06/e06157.jpg"},"30":{"name":"e06171 - M.M.MIRAJ","image":"https://cepdnaclk.github.io/department-website-2013/people/images/e06/e06171.jpg"},"31":{"name":"e06177 - H.P.S.NANDASIRI","image":"https://cepdnaclk.github.io/department-website-2013/people/images/e06/e06177.jpg"},"32":{"name":"e06178 - H.M.P.C.K.NAVARATHNA","image":"https://cepdnaclk.github.io/department-website-2013/people/images/e06/e06178.jpg"},"33":{"name":"e06179 - I.B.NAWINNE","image":"https://cepdnaclk.github.io/department-website-2013/people/images/e06/e06179.jpg"},"34":{"name":"e06183 - N.M.J.W.NISHSHANKA","image":"https://cepdnaclk.github.io/department-website-2013/people/images/e06/e06183.jpg"},"35":{"name":"e06194 - H.A.A.S.PERERA","image":"https://cepdnaclk.github.io/department-website-2013/people/images/e06/e06194.jpg"},"36":{"name":"e06195 - M.A.S.M.PERERA","image":"https://cepdnaclk.github.io/department-website-2013/people/images/e06/e06195.jpg"},"37":{"name":"e06196 - N.S.D.M.D.PERERA","image":"https://cepdnaclk.github.io/department-website-2013/people/images/e06/e06196.jpg"},"38":{"name":"e06202 - M.A.L.PRARTHANA","image":"https://cepdnaclk.github.io/department-website-2013/people/images/e06/e06202.jpg"},"39":{"name":"e06211 - D.H.T.PUNCHIHEWA","image":"https://cepdnaclk.github.io/department-website-2013/people/images/e06/e06211.jpg"},"40":{"name":"e06219 - I.R.R.C.D.RANABAHU","image":"https://cepdnaclk.github.io/department-website-2013/people/images/e06/e06219.jpg"},"41":{"name":"e06222 - B.A.RANAWEERA","image":"https://cepdnaclk.github.io/department-website-2013/people/images/e06/e06222.jpg"},"42":{"name":"e06223 - R.A.D.S.C.RANDENI","image":"https://cepdnaclk.github.io/department-website-2013/people/images/e06/e06223.jpg"},"43":{"name":"e06227 - R.M.E.D.RATHNAYAKE","image":"https://cepdnaclk.github.io/department-website-2013/people/images/e06/e06227.jpg"},"44":{"name":"e06228 - R.M.G.H.N.RATHNAYAKE","image":"https://cepdnaclk.github.io/department-website-2013/people/images/e06/e06228.jpg"},"45":{"name":"e06230 - R.M.P.RATHNAYAKE","image":"https://cepdnaclk.github.io/department-website-2013/people/images/e06/e06230.jpg"},"46":{"name":"e06232 - S.RENUKA","image":"https://cepdnaclk.github.io/department-website-2013/people/images/e06/e06232.jpg"},"47":{"name":"e06239 - M.M.U.C.SAMARANAYAKE","image":"https://cepdnaclk.github.io/department-website-2013/people/images/e06/e06239.jpg"},"48":{"name":"e06242 - D.D.SAMARASINGHE","image":"https://cepdnaclk.github.io/department-website-2013/people/images/e06/e06242.jpg"},"49":{"name":"e06243 - K.B.R.G.T.SAMARASINGHE","image":"https://cepdnaclk.github.io/department-website-2013/people/images/e06/e06243.jpg"},"50":{"name":"e06260 - S.G.M.A.B.SENAVIRATHNA","image":"https://cepdnaclk.github.io/department-website-2013/people/images/e06/e06260.jpg"},"51":{"name":"e06263 - P.A.V.SHYAMANI","image":"https://cepdnaclk.github.io/department-website-2013/people/images/e06/e06263.jpg"},"52":{"name":"e06272 - R.J.STANLY","image":"https://cepdnaclk.github.io/department-website-2013/people/images/e06/e06272.jpg"},"53":{"name":"e06273 - P.M.SUDUSINGHE","image":"https://cepdnaclk.github.io/department-website-2013/people/images/e06/e06273.jpg"},"54":{"name":"e06282 - D.R.V.L.B.THAMBAWITA","image":"https://cepdnaclk.github.io/department-website-2013/people/images/e06/e06282.jpg"},"55":{"name":"e06288 - T.THARMINI","image":"https://cepdnaclk.github.io/department-website-2013/people/images/e06/e06288.jpg"},"56":{"name":"e06296 - G.THINESH","image":"https://cepdnaclk.github.io/department-website-2013/people/images/e06/e06296.jpg"},"57":{"name":"e06314 - W.M.P.B.WASALA","image":"https://cepdnaclk.github.io/department-website-2013/people/images/e06/e06314.jpg"},"58":{"name":"e06315 - W.A.A.WEERAKOON","image":"https://cepdnaclk.github.io/department-website-2013/people/images/e06/e06315.jpg"},"59":{"name":"e06321 - W.R.M.M.S.WICKRAMASINGHE","image":"https://cepdnaclk.github.io/department-website-2013/people/images/e06/e06321.jpg"},"60":{"name":"e06333 - S.YAMUNA","image":"https://cepdnaclk.github.io/department-website-2013/people/images/e06/e06333.jpg"},"61":{"name":"e06339 - K.G.K.G.KOTTEGODA","image":"https://cepdnaclk.github.io/department-website-2013/people/images/e06/e06339.jpg"}}

"""

data = json.loads(outputFromJavaScript)
outputJSON = {}

for i in range(len(data)):
    name = data[str(i)]["name"]
    batch = int(name[1:3])
    regNo = int(name[3:6])
    url = data[str(i)]["image"]
    name = name.split("-")[1].strip()
    print(name, batch, regNo, url)
    image_path = f"images/students/e{str(batch).zfill(2)}/e{str(batch).zfill(2)}{str(regNo).zfill(3)}.jpg"
    outputJSON[str(f"E/{str(batch).zfill(2)}/{str(regNo).zfill(3)}")] = {"reg_no": f"E/{str(batch).zfill(2)}/{str(regNo).zfill(3)}",
                                                                         "name_with_initials": name,
                                                                         "image_url": image_path}
    urllib.request.urlretrieve(url, "../"+image_path)


outputJSONFile = open(f"../_data/stud/e{str(batch).zfill(2)}.json", "w")
outputJSONFile.write(json.dumps(outputJSON, indent=4))
outputJSONFile.close()
