import BookingCard from "./BookingCard";

function BookingList({ bookings, refresh }) {
  return (
    <div>
      <h2>All Bookings</h2>
      {bookings.map(b => (
        <BookingCard key={b.id} booking={b} refresh={refresh} />
      ))}
    </div>
  );
}

export default BookingList;
