window.Patient = function Patient({ id, priority }) {
  return (
    <img
      className="sprite patient"
      id={id}
      alt={priority === "high" ? "🤮" : "🤧"}
    />
  );
};
