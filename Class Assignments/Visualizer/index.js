function App() {
  function getRandomExaminer() {
    return ["👨🏻‍⚕️", "👨🏼‍⚕️", "👨🏽‍⚕️", "👨🏾‍⚕️", "👨🏿‍⚕️"][Math.floor(Math.random() * 5)];
  }

  function getRandomPhysician() {
    return ["👩🏿‍⚕️", "👩🏾‍⚕️", "👩🏽‍⚕️", "👩🏼‍⚕️", "👩🏻‍⚕️"][Math.floor(Math.random() * 5)];
  }

  function createDoctorArray(length, type) {
    return Array.from({ length: length }, (_, index) => ({
      id: `${type === "examiner" ? "de" : "dp"}${index + 1}`,
      status: ["available", "busy"][Math.round(Math.random())], // CHANGE
      emoji: type === "examiner" ? getRandomExaminer() : getRandomPhysician(),
    }));
  }

  const [patients, setPatients] = React.useState([]);
  const [examiners, setExaminers] = React.useState([]);
  const [physicians, setPhysicians] = React.useState([]);
  const queues = [
    { id: "qeh" }, //examination_high"
    { id: "qel" }, //examination_low" },
    { id: "qt" }, //"reatment" },
  ];

  eel.expose(initVisualizer);
  function initVisualizer(examinersCount, physiciansCount) {
    setExaminers(createDoctorArray(examinersCount, "examiner"));
    setPhysicians(createDoctorArray(physiciansCount, "physician"));
  }

  function createPatient(priority, id) {
    const newPatients = [
      ...patients,
      {
        id: id,
        priority: priority,
        location: priority === "low" ? "qel" : "qeh",
      },
    ];
    setPatients(newPatients);
  }

  eel.expose(newPatient);
  function newPatient(priority, id) {
    ReactDOM.flushSync(() => createPatient(priority, id));
    animatePatientIn(`p${patients.length + 1}`);
  }

  eel.expose(movePatient);
  function movePatient(patientId, destination) {
    const newPatients = patients.map((patient) =>
      patient.id === patientId ? { ...patient, location: destination } : patient
    );
    setPatients(newPatients);
  }

  function getPatients(location) {
    return patients.filter((p) => p.location === location);
  }

  return (
    <>
      <div className="simulator">
        <div className="hospital">
          <div className="entry" />

          <Queue {...queues[0]} patients={getPatients("qeh")} />
          <Queue {...queues[1]} patients={getPatients("qel")} />

          <section className="doctors">
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

          <Queue {...queues[2]} patients={getPatients("qt")} />

          <section className="doctors">
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
          <div className="exit" />
        </div>
      </div>
    </>
  );
}

const root = ReactDOM.createRoot(document.getElementById("root"));
root.render(<App />);
