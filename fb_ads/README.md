# Pull FB Marketing API

## Required fields ([Link](https://developers.facebook.com/apps/421332548268571/marketing-api/quickstart/) for getting params. Work only for hello@windsor.ai)
* access_token ![img](http://dl4.joxi.net/drive/2017/09/05/0020/2358/1321270/70/b1e100f6fd.png)
* ad_account_id ![img](http://dl3.joxi.net/drive/2017/09/05/0020/2358/1321270/70/68847ac96b.png)
* app_secret

## Usage
```bash
pip install -r requirements.txt
python fb_ads.py
```

### Output example fb_ads.csv
```csv
date,campaign_id,campaign_name,spend
2017-07-28,6099997180251,Blog Traffic,0
2017-07-29,6099997180251,Blog Traffic,0.19
2017-07-30,6099997180251,Blog Traffic,4.97
2017-07-31,6099997180251,Blog Traffic,0.67
2017-08-01,6099997180251,Blog Traffic,0
2017-08-02,6099997180251,Blog Traffic,2.21
```
