"""Small examples of structured application logs sent to Sentry."""

import os

import sentry_sdk


environment = os.getenv("SENTRY_ENVIRONMENT", "development")
sentry_dsn = os.getenv("SENTRY_DSN", "").strip() or (
    "https://c1ff93cca1739fd736f738e1773a8eb0"
    "@o4512332898304000.ingest.de.sentry.io/4512336908910672"
)

sentry_sdk.init(
    dsn=sentry_dsn,
    environment=environment,
    release=os.getenv("SENTRY_RELEASE"),
    traces_sample_rate=0.1 if environment == "production" else 1.0,
)


def handler(event: dict[str, object]) -> dict[str, str]:
    """Handle a sample event and emit useful, searchable log attributes."""
    name = event.get("name", "work")
    if not isinstance(name, str):
        sentry_sdk.logger.warning(
            "Rejected event with invalid name",
            attributes={"input_type": type(name).__name__},
        )
        return {"message": "invalid event"}

    sentry_sdk.logger.info(
        "Handled event",
        attributes={
            "event_type": "greeting",
            "outcome": "success",
        },
    )
    return {"message": f"hello, {name}!"}


if __name__ == "__main__":
    with sentry_sdk.start_transaction(op="task", name="sample handler"):
        result = handler({"name": "devops"})
        print(result)
