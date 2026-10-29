

import sentry_sdk

from sentry_sdk import metrics

sentry_sdk.init(
  dsn="https://c1ff93cca1739fd736f738e1773a8eb0@o4512332898304000.ingest.de.sentry.io/4512336908910672",
)

metrics.count("checkout.failed", 1)
metrics.gauge("queue.depth", 42)
metrics.distribution("cart.amount_usd", 187.5)

sentry_sdk.init(
    dsn="https://c1ff93cca1739fd736f738e1773a8eb0@o4512332898304000.ingest.de.sentry.io/4512336908910672",
    # Tracing is not required for profiling to work
    # but for the best experience we recommend enabling it
    traces_sample_rate=1.0,
    # Set profile_session_sample_rate to 1.0 to profile 100%
    # of profile sessions.
    profile_session_sample_rate=1.0
)

def slow_function():
    import time
    time.sleep(0.1)
    return "done"

def fast_function():
    import time
    time.sleep(0.05)
    return "done"

# Manually call start_profiler and stop_profiler
# to profile the code in between
sentry_sdk.profiler.start_profiler()

for i in range(0, 10):
    slow_function()
    fast_function()

# Calls to stop_profiler are optional - if you don't stop the profiler, it will keep profiling
# your application until the process exits or stop_profiler is called.
sentry_sdk.profiler.stop_profiler()