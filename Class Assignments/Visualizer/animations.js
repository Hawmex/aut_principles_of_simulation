// function movePatientOutsideQueue(patientId, queueId) {
//   // select patient
//   // animate patient to last of the queue
//   // change patient opacity to 0 or somehow disappear
// }

// function movePatientInsideQueue(patientId, queueId) {
//   // select patient
//   // patient appears with opacity 0->100
//   // animate patient to before last person in queue
// }

// function movePatientInsideRoom(patientId, roomId) {
//   // select patient
//   // patient appears with opacity 0->100
//   // patient moves to middle block (+1 block)
// }

// function movePatientOutsideRoom(patientId) {
//   // select patient
//   // patient moves to last block (+1 block)
//   // patient appears with opacity 0->100
// }

// function animatePatientIn(patientId, movement) {
//   const patientEl = document.getElementById(patientId);
//   const tl = anime.timeline({
//     targets: patientEl,
//     easing: "linear",
//     // delay: 0,
//   });
//   tl.add({
//     opacity: 1,
//   }).add({
//     translateX: movement * 58,
//   });
// }

// function animatePatientOut(patientId, movement) {
//   const patientEl = document.getElementById(patientId);
//   const tl = anime.timeline({
//     targets: patientEl,
//     easing: "linear",
//     // delay: 0,
//   });
//   tl.add({
//     translateX: movement * 58,
//   }).add({
//     opacity: 0,
//   });
// }
