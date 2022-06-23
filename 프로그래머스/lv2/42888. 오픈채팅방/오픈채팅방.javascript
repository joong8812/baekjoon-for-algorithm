function solution(record) {
  const answer = [];
  const history = [];
  const idBook = {};
  const msgBook = {
    Enter: "님이 들어왔습니다.",
    Leave: "님이 나갔습니다.",
  }

  for (systemMsg of record) {
    const [action, id, name] = systemMsg.split(' ');

    if (action !== 'Change'){
      history.push(`${id}${msgBook[action]}`);
    }
    if (action !== 'Leave') {
      idBook[id] = name;
    }
  }

  for (let line of history) {
    let uid = line.slice(0, line.indexOf('님'));
    answer.push(line.replace(uid, idBook[uid]));
  }

  return answer;
}