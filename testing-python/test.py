import sentry_sdk
from sentry_sdk import metrics

sentry_sdk.init(
  dsn="https://c1ff93cca1739fd736f738e1773a8eb0@o4512332898304000.ingest.de.sentry.io/4512336908910672",
)

metrics.count("checkout.failed", 1)
metrics.gauge("queue.depth", 42)
metrics.distribution("cart.amount_usd", 187.5)