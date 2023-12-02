import kue from 'kue';

const queue = kue.createQueue();

const job = {
  phoneNumber: '4153518780',
  message: 'This is the code to verify your account',
}

const notify = queue.create('push_notification_code', job).save((err) => {
  if (!err) console.log(`Notification job created: ${notify.id}`);
});

notify.on('complete', () => {
  console.log('Notification job completed');
});

notify.on('failed', (errorMessage) => {
  console.error(`Notification job failed: ${errorMessage}`);
});
