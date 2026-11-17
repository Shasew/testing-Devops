import http from 'k6/http';
import { check, sleep } from 'k6';

export const options = {
  stages: [
    { duration: '10s', target: 50 },   
   { duration: '20s', target: 200 },  
    { duration: '20s', target: 500 },  
    { duration: '10s', target: 0 },   
  ],
};
 


export default function () {
    const targeturl = '192.168.115.1:3000/login'; 

    const datalogin = {
        username: 'testuser',
        password: 'testpassword',
    };

    const response = http.post(targeturl, JSON.stringify(datalogin), {
        headers: { 'Content-Type': 'application/json' },
    });

    check(response, {
        'is status 200': (r) => r.status === 200,
    });
    sleep(1);
}