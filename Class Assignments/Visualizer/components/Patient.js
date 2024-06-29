window.Patient = function Patient({ id, priority }) {
  return (
    <div className="patient-box" id={id}>
      <img className="sprite" alt="😷" />
      <span>{id}</span>
    </div>
  );
};
