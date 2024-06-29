function App() {
  function createDoctorArray(length, keyName) {
    return Array.from({ length: length }, (_, index) => ({
      id: `${keyName}${index + 1}`,
      status: "available",
    }));
  }

  function createQueueArray(length) {
    return Array.from({ length: length }, (_, index) => ({
      id: `q${index + 1}`,
    }));
  }

  // change with empty array
  const [examiners, setExaminers] = React.useState(createDoctorArray(4, "de"));
  const [physicians, setPhysicians] = React.useState(
    createDoctorArray(6, "dp")
  );
  const [queues, setQueues] = React.useState(createQueueArray(3));
  const [patients, setPatients] = React.useState([]);

  // eel.expose(initVisualizer);
  function initVisualizer(examinersCount, physiciansCount, queuesCount) {
    setExaminers(createDoctorArray(examinersCount, "de"));
    setPhysicians(createDoctorArray(physiciansCount, "dp"));
    setQueues(createQueueArray(queuesCount));
  }

  function addPatient(type = "high-priority") {
    const newPatients = [
      ...patients,
      { id: `p${patients.length + 1}`, type: type, location: `q1` },
    ];
    setPatients(newPatients);
  }

  function movePatient(patientId, destination) {
    const newPatients = patients.map((patient) =>
      patient.id === patientId ? { ...patient, location: destination } : patient
    );
    setPatients(newPatients);
  }

  // animations
  function animatePatientQueueOut(patientId, queueId) {
    const patient = document.getElementById(patientId);
    patient.style.background = "yellow";
    patient.style.gridColumn = "-1";
    console.log(patient);
  }

  return (
    <div className="hospital">
      {examiners.map((examiner) => {
        return (
          <DoctorRoom
            type="examiner"
            {...examiner}
            key={examiner.id}
            patient={patients.filter((p) => p.location === examiner.id)[0]}
          />
        );
      })}
      {physicians.map((physician) => {
        return (
          <DoctorRoom
            type="physician"
            {...physician}
            key={physician.id}
            patient={patients.filter((p) => p.location === physician.id)[0]}
          />
        );
      })}
      {queues.map((queue) => {
        return (
          <Queue
            {...queue}
            key={queue.id}
            patients={patients.filter((p) => p.location === queue.id)}
          />
        );
      })}

      <button onClick={() => addPatient("low")}>add patient</button>
      <button onClick={() => animatePatientQueueOut("p2")}>animate</button>
      {/* <button onClick={() => movePatient("p3", "q2")}>p3 to q2</button> */}
      {/* <button onClick={() => movePatient("p2", "de2")}>p2 to doctor2</button> */}
      {/* <p>{JSON.stringify(patients)}</p> */}
    </div>
  );
}

const root = ReactDOM.createRoot(document.getElementById("root"));
root.render(<App />);
