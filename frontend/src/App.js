import { useEffect, useState } from "react";
import { getBookings } from "./api";
import CreateBooking from "./components/CreateBooking";
import BookingList from "./components/BookingList";

function App() {
  const [bookings, setBookings] = useState([]);

  const loadBookings = () => {
    getBookings().then(setBookings);
  };

  useEffect(() => {
    loadBookings();
  }, []);

  return (
    <div className="container">
      <h1>Home Services Booking System</h1>
      <CreateBooking refresh={loadBookings} />
      <BookingList bookings={bookings} refresh={loadBookings} />
    </div>
  );
}

export default App;
