from flask import Flask
import getpass
import datetime
import subprocess
import pytz

app = Flask(__name__)

@app.route("/htop")
def htop():
    name = "Murali Karthic B S"
    username = getpass.getuser()

    tz = pytz.timezone('Asia/Kolkata')
    server_time = datetime.datetime.now(tz).strftime('%Y-%m-%d %H:%M:%S %Z')

    top_output = subprocess.getoutput('top -b -n 1 | head -10').replace('\n', '<br>')

    return f"""
    <h1>HTOP Dashboard</h1>
    <p><b>Name:</b> {name}</p>
    <p><b>Username:</b> {username}</p>
    <p><b>Server Time (IST):</b> {server_time}</p>
    <p><b>Top Output:</b><br>{top_output}</p>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

git add .
git commit -m "Initial htop endpoint"
git push
