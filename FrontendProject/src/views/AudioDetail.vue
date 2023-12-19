<template>
  <div class="max-w-7xl mx-auto grid grid-cols-2 gap-4 mt-20">
    <div class="main-left bg-white rounded-md shadow-md">
      <div class="p-6 ml-15">
        <div class="mb-8">
          <h4 class="px-2 text-xl font-bold text-navy-700 dark:text-white">
            General Information
          </h4>
          <div class="flex flex-col">
            <div class="mb-8 mt-10 w-full">
              <p class="text-sm text-gray-600 ml-4">Description</p>
              <p class="mt-2 ml-2 px-2 text-base text-gray-600 title">
                {{ audio.description }}
              </p>
            </div>
            <div class="grid grid-cols-2 gap-4 px-2 w-full">
              <div
                class="flex flex-col items-start justify-center rounded-2xl bg-white bg-clip-border px-3 py-4 shadow-3xl shadow-shadow-500 dark:!bg-navy-700 dark:shadow-none"
              >
                <p class="text-sm text-gray-600">Customer</p>
                <p
                  class="text-base font-medium text-navy-700 dark:text-white title"
                >
                  {{ audio.customer }}
                </p>
              </div>

              <div
                class="flex flex-col justify-center rounded-2xl bg-white bg-clip-border px-3 py-4 shadow-3xl shadow-shadow-500 dark:!bg-navy-700 dark:shadow-none"
              >
                <p class="text-sm text-gray-600">Title</p>
                <p
                  class="text-base font-medium text-navy-700 dark:text-white title"
                >
                  {{ audio.title }}
                </p>
              </div>
            </div>
            <div class="grid grid-cols-2 gap-4 px-2 w-full">
              <div
                class="flex flex-col items-start justify-center rounded-2xl bg-white bg-clip-border px-3 py-4 shadow-3xl shadow-shadow-500 dark:!bg-navy-700 dark:shadow-none"
              >
                <p class="text-sm text-gray-600">Anatator</p>
                <p
                  class="text-base font-medium text-navy-700 dark:text-white title"
                >
                  {{ audio.anatator }}
                </p>
              </div>

              <div
                class="flex flex-col justify-center rounded-2xl bg-white bg-clip-border px-3 py-4 shadow-3xl shadow-shadow-500 dark:!bg-navy-700 dark:shadow-none"
              >
                <p class="text-sm text-gray-600">Status</p>
                <p
                  class="text-base font-medium text-navy-700 dark:text-white title"
                >
                  {{ audio.status }}
                </p>
              </div>
            </div>

            <div class="grid grid-cols-2 gap-4 px-2 w-full">
              <div
                class="flex flex-col items-start justify-center rounded-2xl bg-white bg-clip-border px-3 py-4 shadow-3xl shadow-shadow-500 dark:!bg-navy-700 dark:shadow-none"
              >
                <p class="text-sm text-gray-600">Created</p>
                <p class="text-base font-medium text-navy-700 dark:text-white">
                  {{ audio.created_at }}
                </p>
              </div>

              <div
                class="flex flex-col justify-center rounded-2xl bg-white bg-clip-border px-3 py-4 shadow-3xl shadow-shadow-500 dark:!bg-navy-700 dark:shadow-none"
              >
                <p class="text-sm text-gray-600">Updated</p>
                <p
                  class="text-base font-medium text-navy-700 dark:text-white"
                ></p>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>

    <div class="main-right">
      <audio controls>
        <source src="" type="" />
        <source src="" type="" />
      </audio>
      <div class="mt-5">
        <router-link
          :to="{ name: 'audioupdate', params: { id: audio.id } }"
          class="text-sky-600 text-m hover:text-indigo-900 ml-4 mt-20 underline underline-offset-1"
          >Go To Transcribe</router-link
        >
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";
export default {
  name: "audiodetail",
  data() {
    return {
      audio: {},
    };
  },
  mounted() {
    this.getAudio();
  },
  methods: {
    async getAudio() {
      const id = this.$route.params.id;
      axios
        .get(`/api/audios/${id}/`)
        .then((response) => {
          this.audio = response.data;
          console.log(this.audio);
        })
        .catch((error) => console.log(error));
    },
  },
};
</script>
