
#!/usr/bin/env python3
import argparse, json, time
from http.server import BaseHTTPRequestHandler, HTTPServer
from pathlib import Path
class Handler(BaseHTTPRequestHandler):
    def do_POST(self):
        if self.path!="/hook": self.send_response(404); self.end_headers(); self.wfile.write(b"Not found"); return
        n=int(self.headers.get("Content-Length","0")); raw=self.rfile.read(n) if n else b"{}"
        try: payload=json.loads(raw.decode("utf-8"))
        except Exception: payload={"raw":raw.decode("utf-8","ignore")}
        Path("./examples").mkdir(parents=True, exist_ok=True)
        ts=time.strftime("%Y%m%d_%H%M%S"); out=f"./examples/slack_{ts}.json"
        with open(out,"w",encoding="utf-8") as f: json.dump(payload,f,indent=2)
        result={"created":True,"issue_key":f"IT-{int(time.time())%100000}","stored":out}
        data=json.dumps(result).encode("utf-8")
        self.send_response(200); self.send_header("Content-Type","application/json"); self.send_header("Content-Length",str(len(data))); self.end_headers(); self.wfile.write(data)
def main():
    ap=argparse.ArgumentParser(); ap.add_argument("--port",type=int,default=8080); a=ap.parse_args()
    srv=HTTPServer(("0.0.0.0",a.port),Handler); print(f"Listening on http://0.0.0.0:{a.port}  (POST /hook)")
    try: srv.serve_forever()
    except KeyboardInterrupt: print("Shutting down..."); srv.server_close()
if __name__=="__main__": main()
