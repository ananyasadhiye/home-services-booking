const BASE_URL = "http://localhost:8000/api";

export const getBookings = () =>
  fetch(`${BASE_URL}/bookings/`).then(res => res.json());

export const createBooking = (data) =>
  fetch(`${BASE_URL}/bookings/create/`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(data),
  });

export const assignProvider = (id) =>
  fetch(`${BASE_URL}/bookings/${id}/assign/`, { method: "POST" });

export const updateStatus = (id, status, actor = "admin") =>
  fetch(`${BASE_URL}/bookings/${id}/status/`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ status, actor }),
  });

export const getEvents = (id) =>
  fetch(`${BASE_URL}/bookings/${id}/events/`).then(res => res.json());
