import json

import requests


# 组织事件回测的json字符串
def organize_json_format(
        sectionTags: list, filterTags: list, assetsIds: list,
        eventTag: list, dayOffsets: int, benchmarkParams: int):
    '''组织事件回测的json字符串'''

    url = 'http://123.56.139.121:8000/api/v1/events/do-backtest'

    headers = {'Content-Type': 'application/json',
               'Authentication': 'eyJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJ7XCJpZFwiOjksXCJ1c2VyVHlwZVwiOjEsXCJ1c2VybmFtZVwiOlwi6Zi_5ZGGXCIsXCJlbWFpbFwiOlwiNDQxMTYxMTI3QHFxLmNvbVwiLFwicG9pbnRzXCI6MC4wLFwib3B0aW9uYWxBc3NldHNJZHNcIjpbXX0ifQ.R9SWlV87_l-hjW_2x6ajTPiFR26VEeWEOCOvvqYxw_o'}

    data = {
        "batchId": "123",
        "xbtContext": [
            {
                "taskId": "123",
                "strategyModelId": "EventBasedStrategyModel",
                "entryStrategyParams": [
                    {
                        "strategyId": 1,
                        "sectionTags": [section_tag for section_tag in sectionTags],
                        "filterTags": [filter_tag for filter_tag in filterTags],
                        "assetsIds": [assets_id for assets_id in assetsIds],
                        "specialParams": {
                            "eventTagParams": [
                                {
                                    "eventTag": tag,
                                    "degree": -2,
                                    "direction": -1,
                                    "market_type": 1,
                                    "status": 2,
                                    "media_source": ""
                                } for tag in eventTag
                            ]
                        }
                    }
                ],
                "exitStrategyParams": [
                    {
                        "strategyId": 1282,
                        "sectionTags": [],
                        "assetsIds": [],
                        "specialParams": {
                            "ifBackward": 0,
                            "dayOffsets": dayOffsets
                        }
                    }
                ],
                "timeParams": {
                    "timeFrame": "Day1",
                    "timeAfter": "2019-01-01 00:00:00",
                    "timeBefore": "2020-07-01 00:00:00"
                },
                "portfolioParams": {
                    "enable": False,
                    "baseCurrency": "CNY",
                    "initBasePosition": 10000,
                    "initAssetsPosition": 0,
                    "benchmarkId": "000300.ZICN",
                    "benchmarkParams": benchmarkParams
                },
                "marketParams": {
                    "enable": True,
                    "slippage": 0.0,
                    "commission": 0.0005,
                }
            }
        ]
    }

    data_json = json.dumps(data)
    print(data_json)

    # 发送请求
    # response = requests.post(url=url, headers=headers, json=data)


if __name__ == "__main__":
    sec = ['金融', '会计', '互联网']
    filter = ['filter', 'filter', 'filter']
    assid = ['000001.XHFT', '000002.XHFT', '000003.XHFT', '000004.XHFT']
    even = ['金融', '会计', '互联网']
    dayOffsets = 5
    organize_json_format(sec, filter, assid, even, dayOffsets, dayOffsets)
