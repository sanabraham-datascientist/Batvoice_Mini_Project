<template>
  <div class="max-w-7xl mx-auto grid grid-cols-2 gap-4">
    <div class="main-left bg-white rounded-md shadow-md">
      <form @submit.prevent="submitform" class="p-6 ml-15">
        <div class="mb-8">
          <h4 class="px-2 text-xl font-bold text-navy-700 dark:text-white">
            Add Audio
          </h4>
        </div>

        <div class="flex space-x-4">
          <label class="text-m text-gray-600" for="title">Title</label>
          <input
            type=" text "
            id="title"
            name="title"
            v-model="audio.title"
          /><br /><br />
          <label class="text-m text-gray-600" for="customer">Customer</label>
          <input
            type="text"
            id="customer"
            name="customer"
            v-model="audio.customer"
          /><br /><br />
        </div>

        <div
          class="rounded-2xl bg-white bg-clip-border px-3 py-4 shadow-3xl shadow-shadow-500 dark:!bg-navy-700 dark:shadow-none"
        >
          <input
            type="file"
            id="audio"
            name="audio.audio_file"
            @change="getFileInputValue"
          /><br /><br />
        </div>

        <div>
          <div
            class="flex space-between bg-white bg-clip-border px-3 py-4 shadow-3xl shadow-shadow-500 dark:!bg-navy-700 dark:shadow-none"
          >
            <label class="text-m text-gray-600 mr-5">Description</label>

            <textarea
              class="text-base font-medium text-navy-700 dark:text-white w-full"
              name="description"
              v-model="audio.description"
            >
            </textarea>
          </div>
        </div>
        <button
          class="px-5 py-3 text-sm text-white bg-sky-600 rounded-md hover:bg-indigo-500 focus:outline-none" type="submit"
        >
          Save
        </button>
      </form>
    </div>

    <div class="main-right">
      <div class="p-6 ml-15 bg-white rounded-md shadow-md">
        <form @submit.prevent="submitform">
          <div class="mb-8">
            <h4 class="px-2 text-xl font-bold text-navy-700 dark:text-white">
              Add Segment
            </h4>
          </div>
          <div class="grid grid-cols-1 gap-4 px-2 w-full"></div>
          <input type="file" id="audio" name="audio"  /><br /><br />
          <button
            class="px-4 py-3 text-sm text-white bg-sky-600 rounded-md hover:bg-indigo-500 focus:outline-none"
          >
            Add Segment
          </button>
        </form>
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";

export default {
  name: "add-audio",
  data() {
    return {
      audio: {
        title: "",
        customer: "",
        audio_file: "",
        description: "",
      },
    };
  },
  methods: {
    getFileInputValue(event) {
      //get the file input value
      const file = event.target.files;
      //assign it
      audio.value = file[0];
    },

    async submitForm() {
      const audio = {
        tite: this.title,
        customer: this.customer,
        audio_file: this.getFileInputValue(),
        description: this.discription,
      };

      await axios
        .post("/api/audios/admin/add", audio)
        .then((response) => {
          console.log('ttttttttttttt')
          console.log(response);

          this.$router.push("/api/audios");
        })
        .catch((error) => {
          console.log(error);
        });
    },
  },
};
</script>
