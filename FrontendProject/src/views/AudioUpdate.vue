<template>
    <div class="container mx-auto mt-12">
    
    <form  @submit.prevent="updateAudio(segment.id)">
     
    <div v-for="(segment, id) in audio.segments" :key="id"> 
      <div>
    <div class="flex flex-row justify border-b-2 border-gray-200">
      <div class="ml-20 mb-3">
        <audio controls>
          <source src="" type="audio/mpeg" />
          <source src="" type="audio/wav" />
        </audio>
        <template v-if="rules.length > 0">
                        <div  v-for="rule in rules" class="bg-red-300 text-white rounded-lg p-6">
                            <p>{{ rule }}</p>
                        </div>
                    </template>
      </div>
      <div class="ml-10">
        <div class="mt-4 mb-6">
          <div
            class="w-full max-w-sm overflow-hidden bg-white border rounded-md shadow-md"
          >
            
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

             
           
          </div>
        </div>
      </div>
    </div>
  </div>
    </div>
    <div>
     
        <button
          class="px-10 py-3 ml-20 text-sm text-white bg-sky-600 rounded-md hover:bg-indigo-500 focus:outline-none"
        >
          Save All
        </button>
      </div>
   
  </form>
  </div> 
</template>

<script>
  import FormError from 'vue-form-error';
    // Import stylesheet
    import "vue-form-error/dist/FormError.css";
    

import axios from "axios";
export default {
    name: "AudioUpdateView",
    data() {
        return {
            audio: {
      

            },
            formErrors:{},

            segment:{
              id:"",
              transcript:""},  components: {
            FormError
        },

        rules:{}

            
        
        };
    },
    created() {
        console.log("DOM is created");
        this.getAudio()
    },
    mounted() {
        console.log("DOM is mounted");
        this.getAudio()
    },
    methods: {
        getAudio() {
            const id = this.$route.params.id;
            axios
                .get(`/api/audios/${id}/`)
                .then((response) => {
            
                this.audio = response.data;
            })
                .catch((error) => {
                console.log("error", error);
            });
        },

         async updateAudio(){
          const id = this.$route.params.id
        
   await axios.patch(`/api/audios/${id}/update/`, this.audio).then(
          response =>{
            

            this.getAudio()
            
            this.$router.push('/')
           
                    
            }).catch(error =>{
    console.log(error)
            this.rules=[
              {'rule1':'All characters belong to a given character set'},
              {'rule2':'Capital letters are allowed only as a first word letter or if all the letters in the word are upper case'},
              {'rule3':"There can be only zero or one space between two characters"},
              {'rule4':'characters ?.! should be end of text or followed by one space and an uppercase character'},
              {'rule5':'characters ,;: should be end of text of followed by one space"'}]

})


},
    },

};
</script>
