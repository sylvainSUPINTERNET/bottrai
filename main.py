from quart import Quart, request #, websocket
from config.api import api_conf
from src.data_process import process

import pandas as pd
import io
    

app = Quart(__name__)

@app.route(f'/api/{api_conf["VERSION"]}/models/generator', methods=["POST"])
async def model_generator():
    try:
        test = await request.files
        df = pd.read_csv(io.BytesIO(test["dataset"].read()), delimiter=",", encoding='utf-8')

        # WIP
        test = await process(df=df)

        return {"message":"df generated" }, 200
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


# https://colab.research.google.com/
# import pandas as pd
# import numpy as np

# d = {'hobbiesName': ["football basketball", "volley football"], 'hobbiesDetails': ["souvent,desfois", "souvent,de temps en temps "]}
# df = pd.DataFrame(data=d)

# # Get dataframe interessting info
# to_clear = ["hobbiesName", "hobbiesDetails"]

# new_columns_hobbies_name = []
# new_columns_hobbies_details = []

# for i in range(df.index.start, df.index.stop):
#    new_columns_hobbies_name = np.concatenate([new_columns_hobbies_name, df.loc[i]["hobbiesName"].split(" ")])
#    new_columns_hobbies_details = np.concatenate([new_columns_hobbies_details, df.loc[i]["hobbiesDetails"].split(",")])

# hobbies = list(set(new_columns_hobbies_name))
# hobbies_details = list(set(new_columns_hobbies_details))

# print(hobbies)
# print(hobbies_details)

# # Create a proper dataframe with interessting data



# print("=========")
# df