import kue from 'kue';

const queue = kue.createQueue();

const blackList = ['4153518780', '4153518781'];
const key = 'push_notification_code_2';

const sendNotification = (phoneNumber, message, job, done) => {
  job.progress(0, 100);
  if (blackList.includes(phoneNumber)) {
    done(`Phone number ${phoneNumber} is blacklisted`);
    return;
  }

  job.progress(50, 100);
  console.log(`Sending notification to ${phoneNumber}, with message: ${message}`);
}

queue.process(key, 2, (job, done) => {
  const { phoneNumber, message } = job.data;
  sendNotification(phoneNumber, message, job, done);
  done();
});
































// const sendNotification = (phoneNumber, message, job, done) => {
//   job.progress(0, 100);
//   if (blackList.includes(phoneNumber)) {
//     done(Error(`Phone number ${phoneNumber} is blacklisted`));
//     return;
//   }

//   job.progress(50, 100);
//   console.log(
//     `Sending notification to ${phoneNumber}, with message: ${message}`
//   );
//   done();
// }

// queue.process(key, 2, (job, done) => {
//   const { phoneNumber, message} = job.data;
//   sendNotification(phoneNumber, message, job, done);
// });
