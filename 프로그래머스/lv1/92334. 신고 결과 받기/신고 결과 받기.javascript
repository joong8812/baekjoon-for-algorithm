function solution(id_list, report, k) {
  const answer = [];
  const reportDashboard = Array.from(Array(id_list.length), () => new Array());
  const reportedCount = new Array(id_list.length).fill(0);

  for (reportCase of report) {
    const [id, reportedId] = reportCase.split(' ');
    if (id === reportedId) continue;
    if (reportDashboard[id_list.indexOf(id)].includes(reportedId)) continue;
    
    reportDashboard[id_list.indexOf(id)].push(reportedId);
    reportedCount[id_list.indexOf(reportedId)] += 1
  }

  for (reportPerson of reportDashboard) {
    answer.push(reportPerson.filter(person => reportedCount[id_list.indexOf(person)] >= k).length);
  }

  return answer;
}