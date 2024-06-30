window.Queue = function Queue({ patients, id }) {
  return (
    <div className={`queue ${id}`}>
      {/* <img className="sprite door--exit" alt="🚪" /> */}
      {patients.map((patient) => {
        return <Patient key={patient.id} {...patient} />;
      })}
      {/* <img className="sprite door--entry" alt="🚪" /> */}
    </div>
  );
};
