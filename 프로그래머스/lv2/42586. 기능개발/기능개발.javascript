function solution(progresses, speeds) {
  var answer = [];

  // initialize target job
  let targetJob = 0;

  // while loop
  while (progresses.length > 0) {
    // update each progress per day
    for (let i = 0; i < progresses.length; i++) {
      progresses[i] += speeds[i];
    }
    
    // if target job is 100, count all jobs which are 100 and push into answer array
    if (progresses[targetJob] >= 100) {
      let completedJobs = [];
      let tempProgresses = [...progresses];
      for (let i = 0; i < tempProgresses.length; i++) {
        if (tempProgresses[i] < 100) break;
        completedJobs.push(progresses.shift())
        speeds.shift();   
      }
      answer.push(completedJobs.length);
    }
  }

  return answer;
}