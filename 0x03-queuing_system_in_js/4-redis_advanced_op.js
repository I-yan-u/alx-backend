import redis from 'redis';
import { promisify } from 'util';

const client = redis.createClient();
const getAsync = promisify(client.get).bind(client);

client.on('connect', () => {
  console.log('Redis client connected to the server');
});

client.on('error', (err) => {
  console.log(`Redis client not connected to the server: ${err}`);
});

const data = {
  Portland: 50,
  Seattle: 80,
  "New York": 20,
  Bogota: 20,
  Cali: 40,
  Paris: 2, 
}

for (const [key, value] of Object.entries(data)) {
  client.hset('HolbertonSchools', key, value, (_, reply) => redis.print(`Reply: ${reply}`));
}
client.hgetall('HolbertonSchools', (_, reply) => {console.log(reply)});
