window.Queue = function Queue({ patients, id }) {
  return (
    <div className={`queue ${id}`}>
      {patients.map((patient) => {
        return <Patient key={patient.id} {...patient} />;
      })}
    </div>
  );
};
