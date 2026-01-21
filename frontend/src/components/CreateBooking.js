import { useState } from "react";
import { createBooking } from "../api";

function CreateBooking({ refresh }) {
  const [customer, setCustomer] = useState("");
  const [service, setService] = useState("");

  const submit = async () => {
    await createBooking({
      customer_name: customer,
      service_type: service,
    });
    setCustomer("");
    setService("");
    refresh();
  };

  return (
    <div className="card">
      <h2>Create Booking</h2>
      <input
        placeholder="Customer Name"
        value={customer}
        onChange={e => setCustomer(e.target.value)}
      />
      <input
        placeholder="Service Type"
        value={service}
        onChange={e => setService(e.target.value)}
      />
      <button onClick={submit}>Create</button>
    </div>
  );
}

export default CreateBooking;
