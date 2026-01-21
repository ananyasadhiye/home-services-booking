import { useEffect, useState } from "react";
import { getEvents } from "../api";

function BookingEvents({ bookingId }) {
  const [events, setEvents] = useState([]);

  useEffect(() => {
    getEvents(bookingId).then(setEvents);
  }, [bookingId]);

  return (
    <div className="events">
      <h4>Event Log</h4>
      {events.map(e => (
        <div key={e.id}>
          {e.old_status} → {e.new_status} ({e.actor})
        </div>
      ))}
    </div>
  );
}

export default BookingEvents;
