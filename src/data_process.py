import asyncio
import pandas as pd
import numpy as np

async def process(df):
    to_clear = ["hobbiesName", "hobbiesDetails"]

    df_tmp={}
    for i in range(df.index.start, df.index.stop):
       for idx, hobby in enumerate(df.loc[i]["hobbiesName"].split(" ")):
            detail = df.loc[i]["hobbiesDetails"].split(",")[idx]
            if ( hobby not in df_tmp ):
                df_tmp[hobby] = [detail]
            else:
                df_tmp[hobby].append(detail)


    # Give default None for empty
    df_clean = pd.DataFrame.from_dict(df_tmp, orient='index').transpose()

    for name_col_to_clear in to_clear:
        df.pop(name_col_to_clear)

    for col_name in df_clean:
        df[col_name] = df_clean[col_name]

    # Implement download CSV file
    return df_clean