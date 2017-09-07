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

import argparse
import csv
import json
import os

from facebookads.adobjects.adaccount import AdAccount
from facebookads.adobjects.campaign import Campaign
from facebookads.api import FacebookAdsApi


def main(access_token, ad_account_id, app_secret, *args, **kwargs):
    FacebookAdsApi.init(access_token=access_token)

    adAccounts = AdAccount(ad_account_id).get_insights(
        fields=['campaign_id'],
        params={
            'level': 'campaign',
            'breakdowns': [],
        },
    )

    insights = []

    with open('ads.csv', 'w') as csvfile:

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


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='FB Marketing API')
    parser.add_argument(
        '--file', '-f',
        default=os.path.abspath('./credentials.json'),
        help='JSON file with credentials (access_token, ad_account_id, app_secret)'
    )
    args = parser.parse_args()
    with open(args.file) as json_file:
        main(*json.load(json_file).values())
