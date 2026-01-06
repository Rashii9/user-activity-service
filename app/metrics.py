from prometheus_client import Counter

REQUEST_COUNT = Counter(
    "app_requests_total",
    "Total number of requests"
)
