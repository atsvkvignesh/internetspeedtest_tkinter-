import speedtest
import pickle as p
st=speedtest.Speedtest()
servernames=[]
st.get_servers(servernames)
with open("nettesttxt.dat","ab+") as fo:
    p.dump(st.download() *1e-6,fo)
    p.dump(st.upload() * 1e-6,fo)
    p.dump(st.results.ping,fo)
