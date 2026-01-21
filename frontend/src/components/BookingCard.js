import { assignProvider, updateStatus } from "../api";
import BookingEvents from "./BookingEvents";
import { useState } from "react";

function BookingCard({ booking, refresh }) {
  const [showEvents, setShowEvents] = useState(false);

  return (
    <div className="card">
      <p><b>ID:</b> {booking.id}</p>
      <p><b>Customer:</b> {booking.customer_name}</p>
      <p><b>Service:</b> {booking.service_type}</p>
      <p><b>Status:</b> {booking.status}</p>

      <button onClick={async () => {
        await assignProvider(booking.id);
        refresh();
      }}>
        Assign Provider
      </button>

      <button onClick={async () => {
        await updateStatus(booking.id, "IN_PROGRESS");
        refresh();
      }}>
        Start
      </button>

      <button onClick={async () => {
        await updateStatus(booking.id, "COMPLETED");
        refresh();
      }}>
        Complete
      </button>

      <button onClick={async () => {
        await updateStatus(booking.id, "CANCELLED");
        refresh();
      }}>
        Cancel
      </button>

      <button onClick={() => setShowEvents(!showEvents)}>
        View Events
      </button>

      {showEvents && <BookingEvents bookingId={booking.id} />}
    </div>
  );
}

export default BookingCard;
