import os 
import sentry_sdk

def init_sentry():
    sentry_sdk.init(
        dsn=os.getenv("https://c1ff93cca1739fd736f738e1773a8eb0@o4512332898304000.ingest.de.sentry.io/4512336908910672"),
        environment=os.getenv("SENTRY_ENVIRONMENT", "development"),
        traces_sample_rate=1.0,
    )