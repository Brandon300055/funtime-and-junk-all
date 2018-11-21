new Vue({
  el:'#app',
  data: {
    calculation: "",

  },
  methods: {
    append:function(num) {
      this.calculation += num;
    },
    clear:function() {
      this.calculation = '';
    },
    eval:function() {
      this.calculation = eval(this.calculation);
    },
    // sin:function(){
    //   this.calculation = math.sin(this.calculation)
    // }
    cos:function(){
      this.calculation = math.cos(this.calculation)
    }
    // tan:function(){
    //   this.calculation = math.tan(this.calculation)
    // }
  },
    //when run caluclations us computed:
    computed: {
    }
});
