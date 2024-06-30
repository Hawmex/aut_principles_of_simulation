function App() {
  function createDoctorArray(length, keyName) {
    return Array.from({ length: length }, (_, index) => ({
      id: `${keyName}${index + 1}`,
      status: "available",
    }));
  }

  const [patients, setPatients] = React.useState([]);
  // change with empty array
  const [examiners, setExaminers] = React.useState(createDoctorArray(4, "de"));
  const [physicians, setPhysicians] = React.useState(
    createDoctorArray(1, "dp")
  );
  const queues = [
    { id: "qeh" }, //examination_high"
    { id: "qel" }, //examination_low" },
    { id: "qt" }, //"reatment" },
  ];

  // eel.expose(initVisualizer);
  function initVisualizer(examinersCount, physiciansCount, queuesCount) {
    setExaminers(createDoctorArray(examinersCount, "de"));
    setPhysicians(createDoctorArray(physiciansCount, "dp"));
  }

  function createPatient(priority) {
    const newPatients = [
      ...patients,
      {
        id: `p${patients.length + 1}`,
        priority: priority,
        location: priority === "low" ? "qel" : "qeh",
      },
    ];
    setPatients(newPatients);
  }

  function newPatient(priority) {
    ReactDOM.flushSync(() => createPatient(priority));
    animatePatientIn(`p${patients.length + 1}`);
  }

  // function movePatient(patientId, destination) {
  //   const newPatients = patients.map((patient) =>
  //     patient.id === patientId ? { ...patient, location: destination } : patient
  //   );
  //   setPatients(newPatients);
  // }

  function getPatients(location) {
    return patients.filter((p) => p.location === location);
  }

  return (
    <div className="hospital">
      <section className="section">
        <Queue {...queues[0]} patients={getPatients("qeh")} />
        <Queue {...queues[1]} patients={getPatients("qel")} />
      </section>
      <section className="section">
        {examiners.map((examiner) => {
          return (
            <DoctorRoom
              type="examiner"
              {...examiner}
              key={examiner.id}
              patient={getPatients(examiner.id)[0]}
            />
          );
        })}
      </section>
      <section className="section">
        <Queue {...queues[2]} patients={getPatients("qt")} />
      </section>
      <section className="section">
        {physicians.map((physician) => {
          return (
            <DoctorRoom
              type="physician"
              {...physician}
              key={physician.id}
              patient={getPatients(physician.id)[0]}
            />
          );
        })}
      </section>
      <button onClick={() => newPatient("low")}>add low</button>
      <button onClick={() => newPatient("high")}>add high</button>

      {/* <button onClick={() => patientIn("p1", 0, 5)}>animate</button> */}
    </div>
  );
}

const root = ReactDOM.createRoot(document.getElementById("root"));
root.render(<App />);
