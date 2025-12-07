from datetime import datetime, timedelta
from dash_calendar_timeline import DashCalendarTimeline
from dash import Dash, html, callback, Output, Input

now = datetime.now()

# Helper to convert datetime to UNIX timestamp in milliseconds
to_unix_ms = lambda dt: int(dt.timestamp() * 1000)

import random
from datetime import datetime, timedelta

def to_unix_ms(dt):
    """Convert datetime to Unix timestamp in milliseconds."""
    return int(dt.timestamp() * 1000)

# Generate 100 groups
groups = [{"id": i, "title": f"group {i}"} for i in range(1, 101)]

# Current time
now = datetime.now()

items = []
item_id = 1

# Ensure at least one item per group
for group in groups:
    # 1 to 5 random items per group
    num_items = random.randint(1, 5)
    for _ in range(num_items):
        # Random start time offset between -2h and +2h
        start_offset = timedelta(hours=random.uniform(-6, 6))
        duration = timedelta(minutes=random.randint(30, 180))
        start_time = now + start_offset
        end_time = start_time + duration

        items.append({
            "id": item_id,
            "group": group["id"],
            "title": f"item {item_id}",
            "start_time": to_unix_ms(start_time),
            "end_time": to_unix_ms(end_time)
        })
        item_id += 1


app = Dash(
            __name__,
            meta_tags=[{"name": "viewport", "content": "width=device-width, initial-scale=1.0"}]
        )

app.layout = html.Div(
    [
        DashCalendarTimeline(
            id='calendar-timeline',
            groups=groups,
            items=items,
            defaultTimeStart=to_unix_ms(now),
            defaultTimeEnd=to_unix_ms(now + timedelta(hours=5))
        )
    ]
)


if __name__ == '__main__':
    app.run(debug=True)