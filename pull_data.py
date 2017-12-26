from facebookads.adobjects.adaccount import AdAccount
from facebookads.adobjects.campaign import Campaign
from facebookads.adobjects.adset import AdSet
from facebookads.adobjects.adcreative import AdCreative
from facebookads.adobjects.ad import Ad
from facebookads.adobjects.adpreview import AdPreview
from facebookads.api import FacebookAdsApi
from facebookads.adobjects.adsinsights import AdsInsights
import time
import pdb

access_token = 'EAAFZCMyDfMhsBAF4xHdhq0m11Scu87wSFdwoPoPPhEFAlvRyKPp6xyKD1fOJ3opOGtEPLEIE1oanHFUS9s0UZB6S7hUSQAmwYomVc1SvhPXzOLFQH31QPEA5OEL0nlaNiapXqfiMj1U37h3DO0GyAS6v5Ylm5WSNnmsvqBP4LC7XrdPW8WdXG03KdHeoMZD'
FacebookAdsApi.init(access_token=access_token)

ad_account_id = 'act_22759908'

fields = {
    Campaign.Field.name,
    Campaign.Field.objective,
}

params = {
    Campaign.Field.effective_status: [
        'ACTIVE',
    ],
}

account = AdAccount(ad_account_id)
campaigns = account.get_campaigns(fields=fields, params=params)

print campaigns

fields = [
    AdsInsights.Field.impressions,
    AdsInsights.Field.inline_link_clicks,
    AdsInsights.Field.spend,
]

params = {
    'end_time': 1504275690,
}

if len(campaigns) > 0:
	campaign = Campaign(campaigns[0]['id'])
	insights = campaign.get_insights(fields=fields, params=params)

	print insights
