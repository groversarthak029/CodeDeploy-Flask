from flask import Flask,request

app=Flask(__name__)
@app.route("/", methods=["GET"])

def get_my_ip():
    hostname=request.host_url
    ip_address=request.remote_addr
    
    return "IP Address: "+ip_address + '<br/>'+ "Hostname: " +hostname

if __name__=="__main__":

    app.run(host='0.0.0.0',port=8080)
