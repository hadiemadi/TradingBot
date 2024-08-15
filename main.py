import sqlite3, config
from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates


app = FastAPI()
templates = Jinja2Templates(directory="templates")


@app.get("/")
def index(request: Request):
    # print(dir(request))
    connection = sqlite3.connect(config.DB_FILE)    #if the flie does not exist it creates one database
    connection.row_factory = sqlite3.Row

    cursor = connection.cursor()
    cursor.execute("SELECT id, symbol, name FROM stock ORDER BY symbol")
    rows = cursor.fetchall()

    return templates.TemplateResponse(
        request=request, name="index.html", context={"stocks": rows}
    )
    # return{"title": "Dashboard", "stock":rows} 


@app.get("/stock/{symbol}")
def stock_detail(request: Request, symbol):
    connection = sqlite3.connect(config.DB_FILE)    #if the flie does not exist it creates one database
    connection.row_factory = sqlite3.Row

    cursor = connection.cursor()
    cursor.execute("SELECT id, symbol, name FROM stock WHERE symbol = ?", (symbol,)) 
    row = cursor.fetchone()

    cursor.execute("SELECT * FROM stock_price WHERE stock_id = ? ORDER BY date DESC", (row['id'],))
    stock_bars = cursor.fetchall()
                   

    return templates.TemplateResponse(
        request=request, name="stock_detail.html", context={"stock_info": row, "bars": stock_bars}
    )
 