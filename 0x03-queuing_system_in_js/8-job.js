const createPushNotificationsJobs = (jobs, queue) => {
  if (!(jobs instanceof Array)) {
    console.error('Jobs is not an array');
  }

  jobs.forEach((job) => {
    const service = queue.create('push_notification_code_3', job).save((err) => {
      if (!err) {
        console.log(`Notification job created: ${service.id}`);
      }
    });

    service.on('complete', () => {
      console.log(`Notification job ${service.id} completed`);
    });

    service.on('failed', (err) => {
      console.log(`Notification job ${service.id} failed: ${err}`);
    });

    service.on('progress', (progress) => {
      console.log(`Notification job ${service.id} ${progress} completed`);
    });
  });
}

module.exports = createPushNotificationsJobs;
