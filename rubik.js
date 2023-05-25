new Vue({
    el: "#app",
    data: {
      progress: 0,
    },
    methods: {
      solveCube() {
        // Code to solve the cube goes here
      },
    },
    mounted() {
      // Code to scramble the cube goes here
  
      // Simulate solving process with loading bar
      let interval = setInterval(() => {
        if (this.progress < 100) {
          this.progress += 10;
        } else {
          clearInterval(interval);
          this.solveCube();
        }
      }, 1000);
    },
  });
  