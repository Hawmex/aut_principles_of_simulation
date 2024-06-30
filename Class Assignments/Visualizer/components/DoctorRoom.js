window.DoctorRoom = function DoctorRoom({ id, status, type, patient, emoji }) {
  return (
    <div
      className={`room room--${type}`}
      id={id}
      title={`${type} ${id}, ${status}`}
    >
      <img className={`sprite doctor doctor--${status}`} alt={emoji} />
      {patient && <Patient {...patient} />}
    </div>
  );
};
