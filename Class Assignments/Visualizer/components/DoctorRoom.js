window.DoctorRoom = function DoctorRoom({ id, status, type, patient }) {
  return (
    <div
      className={`doctor-room doctor-room--${type}`}
      id={id}
      title={`${type} ${id}, ${status}`}
    >
      <img
        className="sprite doctor"
        alt={status === "available" ? "👨🏽‍⚕️" : "💉"}
      />
      {patient && <Patient {...patient} />}
    </div>
  );
};
