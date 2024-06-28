window.DoctorRoom = function DoctorRoom({ id, status, type }) {
  return (
    <div
      className={`doctor-room doctor-room--${type}`}
      title={`${type} ${id}, ${status}`}
    >
      <img className="doctor" alt={status === "available" ? "👨🏽‍⚕️" : "💉"} />
    </div>
  );
};
