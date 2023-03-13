import socket
import json

# sunucu soketini oluşturun
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# dinlenecek IP adresi ve port numarasını belirleyin
host = "localhost"
port = 12345

# soketi IP adresi ve port numarasına bağlayın
server_socket.bind((host, port))

# istemci tarafından bağlanması için soketi açın
server_socket.listen()

# bağlantıyı kabul edin ve bağlı soket ve adresi alın
client_socket, client_address = server_socket.accept()

# gönderilecek veri
# data = [3.14, 2.71, 1.618]
data=[31.14283996584254,31.30019746320687,32.998274297776845,34.81146046330588,35.980205052100644,35.87186773372429,36.10856629031821,37.00933727888378,35.801584879944244,33.951152191917345,30.92449882313275,28.53422648493938,26.69278418998732,26.278038866976942,26.499893722893376,27.400202400506487,28.610514057200476,31.199416977939393,37.94296133021072,44.110040362490565,47.05224705720923,45.84196710490096,43.932602578142564,42.0536153372928,41.441415010333856,41.28874684198462,35.16876072597819,30.320502964747902,27.71252403782347,26.294713336187385,26.23225947864387,27.312174361335792,28.222435464717876,32.10856840078691,41.414655285651406,48.58291515958217,50.59832842922589,51.07769408768053,49.315211125988185,45.589932742500025,44.67221667755331,42.5342054424429,36.46693987913022,30.154757435168335,28.444199150971997,26.47144826241106,25.86086239154082,26.48927617043961,28.395519540115345,32.254153822561875,42.156959281042305,49.533020992460365,52.62130122506858,53.582912789976945,51.941863211867656,47.82214490418414,45.29763378929243,43.45797276427834,37.73814530006689,32.03707241112619,29.041889479857446,26.70324280848223,25.971875730832153,26.42652804047094,27.933652651617933,32.31498922445098,41.72620769336356,44.470619467436734,51.508438994909284,53.08522023371842,51.5196849327441,47.77291107148534,45.111100909614095,43.55776194859072,36.064705615913,29.710087597955976,27.400457180305636,27.087781998897526,26.340940057855164,26.25434673836844,28.4035510764121,31.814675768994903,40.27398818956527,39.96112492940284,47.98144811400164,49.534141429164436,48.436493702961855,46.694482126087735,44.930476317723446,42.86888885272356,38.79482820249308,30.019282162640366,27.579324972261247,26.985601407353442,26.257834741170825,26.35749255984365,27.39546327609162,30.479061743180296,36.411751324735974,42.135276906050024,45.675307466490665,45.84649282615902,45.29050155761257,43.91607110331745,42.32965604915029,39.57290002800414,36.44580838548518,31.58027860227122,27.78403488634183,26.598815016820026,25.762756631752836,25.68439809411808,25.9206743518385,27.60810657772265,30.39357365856597,32.13362905265126,32.64415749584418,32.850497205661725,32.75066948062073,32.20959051252186,31.10706582221468,29.987161852824556,29.073159624421578,27.83741358849727,26.637181084218298,25.74024019177898,25.369446875368112,25.391897608014176,25.25349448237256,25.680275548261193,25.899280967453592,26.28205537880268,26.37269456266995,26.778013127322197,26.86375789206386,26.87061943001828,26.78909328259772,26.76362914828485,26.395437680398572,26.16028249189219,25.42407704522799,25.275189893862375,25.22393377271709,25.308788755223077,24.70739220021403,24.749007277133785,24.831275970525212,24.833068483210468,25.061332498219656,25.172652899145646,25.333895874211862,25.40039493017798,25.525675241403235,25.519301555723928,25.251039336596705,25.231910092431974,24.98117861401198,24.79472332374337,25.19526125777719,25.236014983201528,24.40246312597651,24.380228314410658,24.216788416443194,24.30637120260843,24.45458568184614,24.56173236614802,24.648626884197824,24.822811784966348,24.908394201797876,24.664486874932265,24.972326077747425,24.880502738802306,24.69952611723062,24.710794014958196,24.918504929433084,25.336041520900494,24.330091672017943,23.94827480198461,24.11576781365204,23.863558110430915,24.23679567933175,24.126645616779513,24.21335943055044,24.39692879120338,24.673178827907066,24.57237359902598,24.415315356764154,24.513112692999186,24.828937548077135,24.67113753881,25.220165569387177,26.792889273082892]

# JSON formatına dönüştürün
json_data = json.dumps(data)

# veriyi istemciye gönderin
client_socket.sendall(json_data.encode())

# soketi kapatın
client_socket.close()