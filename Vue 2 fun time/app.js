//create new instace of vue
//({pramiters are here})
new Vue({
  //el is a paramiter that controlls your hole front end
  el:'#vue-app',
  //data hold all data
  data: {

    //arrays
    characters: ['brandon', 'kitten', 'people'],

    peoples: [
      {name: 'brandon', age: 21},
      {name: 'kitten', age: .5},
      {name: 'humans', age: 21000},
    ],


    name:'brandon',
    job: 'Back-End Web Applications System Architect',
    //v-bind:href="website" is is how you bind data
    //see https://www.youtube.com/watch?v=xIOwFTCBBDg
    website: 'http://brandonsresume.ml/',
    text: 'text',
    //test binding to the dom via websiteTab an v-html
    websiteTab: '<a href="http://brandonsresume.ml/">Test Link</a>',
    //events
    age:21,
        //note that it all works so far !!!
    x: 0,
    y: 0,
    a: 0,
    b: 0,
    available: false,
    nearby: false,

    error: false,
    success: false,
  },
  methods:{
    addNum(c, d) {
      var a = 2;
      var b = 2;
      return a + b + c + d + this.name;
    },
    ///events
    add:function(num){
      this.age += num;
    },
    remove:function(num){
      this.age -= num;
    },
    updateXYthingy:function(){
      //when calling or doing ana event you can recive it as an event object
      //you can just pass it throght to the function as the paramiter event
      //console.log(event)
      this.x = event.offsetX;
      this.y = event.offsetY;
    },
    click:function(){
      //you can override defualt actions
      alert('You clicked me')
    },
    logName: function(){
      console.log('You entered your name')
    },
    logAge: function(){
      console.log('You entered your age')
    },
  },
    //when run caluclations us computed:
    computed: {
      compClasses: function(){
        return {
          available: this.available,
          nearby: this.nearby,
        }
      },

      addToA: function(){
        //no need to use () parenthises to call computed methods
        console.log('addToA')
        return this.a + this.age;
      },
      addToB: function(){
        console.log('addToB')
        return this.b + this.age;
      },
    }
});
