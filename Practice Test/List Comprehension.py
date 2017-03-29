i = [[x,x**2] for x in range(1,11)]
print i

i = {x:x**2 for x in range(1,11)}
print i

form = {"Chelsea":"WDWWW", "Tottenham":"WLWWW", "ManCity":"WWWDD", "LiverPool":"WLWWD"}
print form

form["LiverPool"] = "LWWDL"
print form

form["ManUTD"] = "DWWDW"
print form