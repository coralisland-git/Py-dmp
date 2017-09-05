# Copyright 2014 Facebook, Inc.

# You are hereby granted a non-exclusive, worldwide, royalty-free license to
# use, copy, modify, and distribute this software in source code or binary
# form for use in connection with the web services and APIs provided by
# Facebook.

# As with any software that integrates with the Facebook platform, your use
# of this software is subject to the Facebook Developer Principles and
# Policies [http://developers.facebook.com/policy/]. This copyright notice
# shall be included in all copies or substantial portions of the software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL
# THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
# FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER
# DEALINGS IN THE SOFTWARE.

from facebookads.adobjects.adaccount import AdAccount
from facebookads.api import FacebookAdsApi
from facebookads.adobjects.campaign import Campaign
import csv


access_token = 'EAAFZCMyDfMhsBAE1t4rVg4go6iEe4sUBL5miKpr5M0Ldj1p36A2G4oDUoXGaB3TFPGgZAGtJC2hQogCyZBZCVzZAEWf5GNrNzKatYS93JxHSXPUTddhcBl9dkxEtJuPni6iBTSrvZAdYWbtgAXLx8JI26Ly0LwZAOC9HqzbLEcaGvqoIZCm1mkb98mEDDIMR5CMZD'
ad_account_id = 'act_22759908'
app_secret = 'f9f994fef60e6bcbea099ca791935fd5'
FacebookAdsApi.init(access_token=access_token)

adAccounts = AdAccount(ad_account_id).get_insights(
    fields=['campaign_id'],
    params={
        'level': 'campaign',
        'breakdowns': [],
    },
)

insights = []

with open('fb_ads.csv', 'w') as csvfile:

    writter = csv.writer(
        csvfile, delimiter=',',
        quotechar='|', quoting=csv.QUOTE_MINIMAL
    )

    writter.writerow(['date', 'campaign_id', 'campaign_name', 'spend'])

    for adAccount in adAccounts:
        campaign = Campaign(adAccount['campaign_id'])

        params = {
            'level': 'ad',
            'date_preset': 'lifetime',
            'time_increment': 1,
            'fields': [
                'campaign_id', 'spend', 'campaign_name'
            ]
        }

        insights += campaign.get_insights(params=params)

    for insight in insights:
        writter.writerow([
            insight['date_start'],
            insight['campaign_id'],
            insight['campaign_name'],
            insight['spend'],
        ])
