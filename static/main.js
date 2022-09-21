const app = new Vue({
  el: "#app",
  vuetify: new Vuetify(),
  data: {
    task: "new task",
    tasks: [],
  },
  methods: {
    async getTasks() {
      var response = await fetch("http://localhost:8000/tasks", {
        method: "get",
        headers: {
          "X-Requested-With": "XMLHttpRequest",
        },
      });
      this.tasks = await response.json();
    },
  },
  async created() {
    await this.getTasks();
  },
});
