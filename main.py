from quart import Quart, request, send_file #, websocket
from config.api import api_conf
from src.data_process import process
import json
import pandas as pd
import io
import uuid

app = Quart(__name__)


# https://colab.research.google.com/


@app.route(f'/api/{api_conf["VERSION"]}/models/generator', methods=["POST"])
async def model_generator():
    try:
        csv_file = await request.files
        df = pd.read_csv(io.BytesIO(csv_file["dataset"].read()), delimiter=",", encoding='utf-8')

        df_clean = await process(df=df)

        # Create an in-memory text stream
        buf = io.BytesIO();
        df_clean.to_csv(buf)

        return await send_file(buf, attachment_filename=f'{uuid.uuid4().hex}.csv', as_attachment=True)
    except Exception as e:
        print(e)
        return {"message":"File error while parsing csv"}, 400



# @app.route(f'/api/{api_conf["VERSION"]}')
# async def json():
#     return {"hello": "world"}

# # @app.websocket("/ws")
# # async def ws():
# #     while True:
# #         await websocket.send("hello")
# #         await websocket.send_json({"hello": "world"})

if __name__ == "__main__":
    app.run()

