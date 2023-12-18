<template>
    <div class="container mx-auto mt-12">
    <div v-for="(segment, id) in segments" :key="id"> 
      <div>
    <div class="flex flex-row justify border-b-2 border-gray-200">
      <div class="ml-20 mb-3">
        <audio controls>
          <source src="" type="audio/mpeg" />
          <source src="" type="audio/wav" />
        </audio>
       
      </div>
      <div class="ml-10">
        <div class="mt-4 mb-6">
          <div
            class="w-full max-w-sm overflow-hidden bg-white border rounded-md shadow-md"
          >
            <form  @submit.prevent="updateSegment(segment.id)">
              <div
                class="flex items-center justify-between px-5 py-3 text-gray-700 border-b"
              ></div>

              <div class="px-5 py-6 text-gray-700 bg-gray-200 border-b">
                <label class="text-xs">Transcript text</label>

                <div class="relative mt-2 rounded-md shadow-sm">
                  <span
                    class="absolute inset-y-0 left-0 flex items-center pl-3 text-gray-600"
                  >
                  {{ segment.id }}
                  </span>

                  <input
                    v-model ="segment.transcript"
                    name="transcript"
                    type="text"
                    class="w-full px-12 py-2 border-transparent rounded-md appearance-none focus:border-indigo-600 focus:ring focus:sky-opacity-40 focus:ring-sky-500"
                  />
                </div>
              </div>

              <div class="flex items-center justify-between px-5 py-3">
                <button
                  class="px-3 py-1 text-sm text-gray-700 bg-gray-200 rounded-md hover:bg-gray-300 focus:outline-none"
                >
                  Cancel
                </button>
                <button
                  class="px-3 py-1 text-sm text-white bg-sky-600 rounded-md hover:bg-indigo-500 focus:outline-none"
                >
                  Save
                </button>
              </div>
            </form>
          </div>
        </div>
      </div>
    </div>
  </div>
    </div>
  </div> 
</template>

<script>

import axios from "axios";
export default {
    name: "AudioUpdateView",
    data() {
        return {
            audio: {},
            segments:[],
            currentSegment:{
              id:"",
              transcript:""
            }
        };
    },
    created() {
        console.log("DOM is created");
        this.getAudio();
    },
    mounted() {
        console.log("DOM is mounted");
    },
    methods: {
        getAudio() {
            const id = this.$route.params.id;
            axios
                .get(`/api/audios/${id}/`)
                .then((response) => {
                console.log("data", response.data);
                this.audio = response.data;
                this.segments = response.data.segments;
            })
                .catch((error) => {
                console.log("error", error);
            });
        },

        updateSegment(id){
          this.segments.map((segment) => {
              if(segment.id === id){
                this.currentSegment = {'id':segment.id, 'transcript':segment.transcript}
              }})
          axios.put(`/api/audios/${id}/`, this.currentSegment).then(
          response =>{
            console.log(response.data)
            segments = this.getSegments().segments}).catch(error =>{
    console.log(error)
})


},
    },

};
</script>
