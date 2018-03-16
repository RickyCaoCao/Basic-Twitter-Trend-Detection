# Basic Twitter Trend Detection
Uses tweepy and datadog to detect spikes and anomalies from Twitter. Send it to PagerDuty to quickly notify the Social Media Marketing Team.

# setup
Required Libraries: `tweepy` and `datadogpy`

```bash
  pip install -r requirements.txt
```
Then, copy/change `config-sample.py` to `config.py` and enter the necessary credentials.

Finally, install [Pagerduty Integration within Datadog](https://www.pagerduty.com/docs/guides/datadog-integration-guide/) to forward alerts.

# todo
- allow usage of other realtime streaming tools by adding generic Pagerduty API