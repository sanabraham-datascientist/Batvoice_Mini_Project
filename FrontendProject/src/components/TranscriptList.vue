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
            <form  @submit.prevent="updateStudent(currentSegment.id)">
              <div
                class="flex items-center justify-between px-5 py-3 text-gray-700 border-b"
              ></div>

              <div class="px-5 py-6 text-gray-700 bg-gray-200 border-b">
                <label class="text-xs">Transcript text</label>

                <div class="relative mt-2 rounded-md shadow-sm">
                  <span
                    class="absolute inset-y-0 left-0 flex items-center pl-3 text-gray-600"
                  >
                    <svg
                      class="w-6 h-6"
                      fill="none"
                      viewBox="0 0 24 24"
                      stroke="currentColor"
                    >
                      <path
                        stroke-linecap="round"
                        stroke-linejoin="round"
                        stroke-width="2"
                        d="M11 4a2 2 0 114 0v1a1 1 0 001 1h3a1 1 0 011 1v3a1 1 0 01-1 1h-1a2 2 0 100 4h1a1 1 0 011 1v3a1 1 0 01-1 1h-3a1 1 0 01-1-1v-1a2 2 0 10-4 0v1a1 1 0 01-1 1H7a1 1 0 01-1-1v-3a1 1 0 00-1-1H4a2 2 0 110-4h1a1 1 0 001-1V7a1 1 0 011-1h3a1 1 0 001-1V4z"
                      />
                    </svg>
                  </span>

                  <input
                    v-model ="transcript"
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
import Transcript from '@/components/Transcript.vue'
export default {
  name: "TranscriptList",
  components: {
    Transcript,
  },
  props: {
    segments: Array
  }

  
};
</script>
