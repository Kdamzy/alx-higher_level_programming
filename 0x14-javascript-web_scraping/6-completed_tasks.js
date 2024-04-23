#!/usr/bin/node
// computes the number of tasks completed by user id

const request = require('request');

request.get(process.argv[2], { json: true }, (error, response, body) => {
  if (error) {
    console.log(error);
    return;
  }

  const completestask = {};
  body.forEach((todo) => {
    if (todo.completed) {
      if (!completestask[todo.userId]) {
        completestask[todo.userId] = 1;
      } else {
        completestask[todo.userId] += 1;
      }
    }
  });
  console.log(completestask);
});
