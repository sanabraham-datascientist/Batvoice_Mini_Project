<template>
  <table class="min-w-full">
    <thead>
      <tr>
        <th
          class="px-6 py-3 text-m font-medium leading-4 tracking-wider text-left text-slate-800 uppercase border-b border-gray-200 bg-gray-50"
        >
          Title
        </th>
        <th
          class="px-6 py-3 text-m font-medium leading-4 tracking-wider text-left text-slate-800 uppercase border-b border-gray-200 bg-gray-50"
        >
          Customer
        </th>
        <th
          class="px-6 py-3 text-m font-medium leading-4 tracking-wider text-left text-slate-800 uppercase border-b border-gray-200 bg-gray-50"
        >
          Status
        </th>
        <th
          class="px-6 py-3 text-m font-medium leading-4 tracking-wider text-left text-slate-800 uppercase border-b border-gray-200 bg-gray-50"
        >
          Anatator
        </th>
        <th
          class="px-6 py-3 text-m font-medium leading-4 tracking-wider text-left text-slate-800 uppercase border-b border-gray-200 bg-gray-50"
        >
          Created
        </th>
        <th class="px-6 py-3 border-b border-gray-200 bg-gray-50" />
        
      </tr>
    </thead>

    <tbody class="bg-white">
      <tr v-for="(audio, index) in audioList" :key="index">
        <td class="px-6 py-4 border-b border-gray-200 whitespace-nowrap">
          <div class="flex items-center">
            <div class="ml-4">
              <div class="text-m font-medium leading-5 text-gray-900">
                {{ audio.title }}
              </div>
              <div class="text-sm leading-5 text-gray-500">
                {{ audio.length }}<span> minutes </span>
              </div>
            </div>
          </div>
        </td>

        <td class="px-6 py-4 border-b border-gray-200 whitespace-nowrap">
          <div class="text-m leading-5 text-gray-900">
            {{ audio.customer }}
          </div>
        </td>

        <td class="px-6 py-4 border-b border-gray-200 whitespace-nowrap">
          <span
            class="inline-flex px-2 text-m font-semibold leading-5 text-green-800 bg-green-100 rounded-full"
          >
            {{ audio.status }}</span
          >
        </td>

        <td
          class="px-6 py-4 text-m leading-5 text-gray-500 border-b border-gray-200 whitespace-nowrap uppercase"
        >
          {{ audio.updated_by.username }}
        </td>

        <td
          class="px-6 py-4 ml-4 text-sm font-medium leading-5 text-center border-b border-gray-200 whitespace-nowrap"
        >
          {{ audio.created_at }}
        </td>
        <template v-if="1 == 1">
          <td
            class="px-6 py-4 ml-4 text-m font-medium leading-5 text-center border-b border-gray-200 whitespace-nowrap"
          >
            <router-link
            :to="{name:'audiodetail',params:{'id':audio.id}}"
              class="text-sky-600 text-lg hover:text-indigo-900 mr-10"
              >Show Details</router-link
            >
            
            <router-link
            :to="{name:'audioupdate',params:{'id':audio.id}}"
              class="text-sky-600 text-lg hover:text-indigo-900 ml-10"
              > Edit</router-link
            > 
          </td>
        </template>
        <template v-if="1 !== 1">
          <td
            class="px-6 py-4 ml-4 text-m font-medium leading-5 text-center border-b border-gray-200 whitespace-nowrap"
          >
            <router-link to="/api/audios/add"
              class="text-sky-600 text-lg hover:text-indigo-900 mr-10"
              >Add </router-link
            >
            <router-link
              v-bind:to="audio.edit_url"
              class="text-sky-600 text-lg hover:text-indigo-900 ml-10"
              >Edit</router-link
            >
            <router-link
              v-bind:to="audio.edit_url"
              class="text-red-600 hover:text-indigo-900 ml-10"
              >Delete</router-link
            >
          </td>
        </template>
      </tr>
    </tbody>
  </table>
</template>
<script>
import Audio from "@/components/Audio.vue";
import axios from "axios";
export default {
  name: "HomeView",
  data() {
    return {
      audioList: [],
    };
  },
  mounted() {
    this.getAudioList();
  },
  methods: {
    getAudioList() {
      axios
        .get("/api/audios/")
        .then((response) => {
          this.audioList = response.data;
        })
        .catch((error) => {
          console.log("error", error);
        });
    },
  },
};
</script>
