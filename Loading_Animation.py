import sys, time

load_zero =    "Loading [          ] - 0%"
load_ten =     "Loading [|         ] - 10%"
load_twenty =  "Loading [||        ] - 20%"
load_thirty =  "Loading [|||       ] - 30%"
load_forty =   "Loading [||||      ] - 40%"
load_fifty =   "Loading [|||||     ] - 50%"
load_sixty =   "Loading [||||||    ] - 60%"
load_seventy = "Loading [|||||||   ] - 70%"
load_eighty =  "Loading [||||||||  ] - 80%"
load_ninety =  "Loading [||||||||| ] - 90%"
load_hundred = "Loading [||||||||||] - 100%"
start =        "<Press Start>"

load_list = [load_zero, load_ten, load_twenty, load_thirty, load_forty, load_fifty, load_sixty, load_seventy, load_eighty, load_ninety, load_hundred]

for x in range(0, 11):
    load = load_list[x]
    print (load, end="\r")
    time.sleep(1)