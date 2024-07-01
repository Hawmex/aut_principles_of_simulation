window.DoctorRoom = function DoctorRoom({ id, status, type, patient, emoji }) {
  return (
    <div
      className={`room room--${type}`}
      id={id}
      title={`${type} ${id}, ${status}`}
    >
      <img
        className={`sprite doctor doctor--${patient ? "busy" : "available"}`}
        alt={emoji}
      />
      {patient && <Patient {...patient} key={patient.id} />}
    </div>
  );
};
