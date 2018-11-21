//object oriented js
//see https://www.youtube.com/watch?v=4l3bTDlT6ZI&list=PL4cUxeGkcC9i5yvDkJgt60vNVWffpblB7&t=0s&index=2

//list array aka json
var names = ["Brandon", "Jason", "Carson"]
//get lenght of list
console.log(names.length)
//sort names apabetecly
console.log(names.sort)


//the windows object

//screen size
console.log(window.innerWidth)

//new String
var names2 = new String('stewart');


//pick up here!!!!
//https://youtu.be/7d9H34ZVRPg?t=5m34s

//class
var userOne = {
  email: 'brandonstewart@gmail.com',
  name: 'brandon',
  login(){ //<-this is a method/function
    console.log(this.name, 'test')
  }
};

console.log(userOne.login);
