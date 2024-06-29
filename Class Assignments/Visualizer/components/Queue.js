window.Queue = function Queue({ patients }) {
  return (
    <div className="queue">
      <img className="sprite door--entry" alt="🚪" />
      {patients.map((patient) => {
        return <Patient key={patient.id} {...patient} />;
      })}
      <img className="sprite door--exit" alt="🚪" />
    </div>
  );
};
