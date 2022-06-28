from flask import Flask
from flask import request
import psycopg2

app = Flask("Job site")


@app.route("/")
def hello():
    ret = []
    conn = psycopg2.connect("dbname=naukri")
    cur = conn.cursor()
    cur.execute("select title,company_name,jd_text from job_openings;")
    for title,company_name,jd in cur.fetchall():
        item = f"<b>{title}</b> ::: {company_name}</br>{jd}"
        ret.append(item)

    l = "<hr/>".join(ret)                                 #refer html for this <hr/> tag.
    return f"List of jobs :</br></br></br>{l}"
