"""Small examples of structured application logs sent to Sentry."""

import os

import sentry_sdk


sentry_sdk.init(
    # Set SENTRY_DSN in the environment; never commit a project DSN here.
    dsn=os.getenv("SENTRY_DSN"),
    environment=os.getenv("SENTRY_ENVIRONMENT", "development"),
    # Sentry Logs are opt-in for the Python SDK.
    enable_logs=True,
    # Tune this for production traffic and your Sentry quota.
    traces_sample_rate=0.1,
)


def handler(event: dict[str, object]) -> dict[str, str]:
    """Handle a sample event and emit useful, searchable log attributes."""
    name = event.get("name", "work")
    if not isinstance(name, str):
        # This is a recoverable input issue; log the type, not the raw value.
        sentry_sdk.logger.warning(
            "Rejected event with invalid name",
            attributes={"app.event.name_type": type(name).__name__},
        )
        return {"message": "invalid event"}

    sentry_sdk.logger.info(
        "Handled event",
        attributes={
            "app.event.name": name,
            "app.event.outcome": "success",
        },
    )
    return {"message": f"hello, {name}!"}


if __name__ == "__main__":
    result = handler({"name": "devops"})
    print(result)
