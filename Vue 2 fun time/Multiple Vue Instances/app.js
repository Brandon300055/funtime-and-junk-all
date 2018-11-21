Vue.component('greeting', {
  template: '<p>He i am a {{ name }}. <button v-on:click="changeName">Change Name</button></p>',
  data:function(){
    return {
      name: 'Brandon',
    }
  },
  methods: {
    changeName:function(){
      this.name = 'Stewart';
    }
  }
})

var one = new Vue({
  el:'#app-one',
  data: {
    title: 'Vue App One',
    output: 'Niffty'
  },
  methods:{
    readRefs:function(){
      console.log(this.$refs.input.value);
      this.output = this.$refs.input.value
    }
  },
  computed:{
    greet:function() {
      return "hello from one"
    }
  }
});

var two = new Vue({
  el:'#app-two',
  data: {
    title: 'Vue App Two',
  },
  methods:{
    changeTitle:function() {
      one.title = "Title Changed";
    }

  },
  computed:{
    greet:function() {
      return "hello from two"
    }
  }
});

two.title = "Change override from out side"
