function App() {
  function createDoctorArray(length) {
    return Array.from({ length: length }, (_, index) => ({
      id: index + 1,
      status: "available",
    }));
  }

  // change with empty array
  const [examiners, setExaminers] = React.useState(createDoctorArray(4));
  const [physicians, setPhysicians] = React.useState(createDoctorArray(6));

  // eel.expose(initVisualizer);
  function initVisualizer(examinersCount, physiciansCount) {
    setExaminers(createDoctorArray(examinersCount));
    setPhysicians(createDoctorArray(physiciansCount));
  }

  return (
    <div className="hospital">
      {examiners.map((examiner) => {
        return <DoctorRoom type="examiner" {...examiner} key={examiner.id} />;
      })}
      {physicians.map((physician) => {
        return (
          <DoctorRoom type="physician" {...physician} key={physician.id} />
        );
      })}
      <Queue />
    </div>
  );
}

const root = ReactDOM.createRoot(document.getElementById("root"));
root.render(<App />);
