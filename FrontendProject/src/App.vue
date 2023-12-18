<script setup>
// import MessageHeader from "@/components/MessageHeader.vue";
</script>

<template>
  <div class="flex">
    <div
      class= "w-60 flex flex-col h-screen p-3 duration-300 bg-gray-800 shadow   h-screen sticky top-0"
    >
      <div class="space-y-15">
        <div class="flex items-center justify-between">
          <img
            src="https://assets-global.website-files.com/5e942b3d36c30b8400e8c95c/5e99635fd0f2eb60f10a9eba_logo_batvoice_horiz_blue02a9f5_large-p-500.png"
            srcset="
              https://assets-global.website-files.com/5e942b3d36c30b8400e8c95c/5e99635fd0f2eb60f10a9eba_logo_batvoice_horiz_blue02a9f5_large-p-500.png   500w,
              https://assets-global.website-files.com/5e942b3d36c30b8400e8c95c/5e99635fd0f2eb60f10a9eba_logo_batvoice_horiz_blue02a9f5_large-p-800.png   800w,
              https://assets-global.website-files.com/5e942b3d36c30b8400e8c95c/5e99635fd0f2eb60f10a9eba_logo_batvoice_horiz_blue02a9f5_large-p-1080.png 1080w,
              https://assets-global.website-files.com/5e942b3d36c30b8400e8c95c/5e99635fd0f2eb60f10a9eba_logo_batvoice_horiz_blue02a9f5_large-p-1600.png 1600w,
              https://assets-global.website-files.com/5e942b3d36c30b8400e8c95c/5e99635fd0f2eb60f10a9eba_logo_batvoice_horiz_blue02a9f5_large.png        1948w
            "
            alt=""
            sizes="115px"
            class="logo-icon mt-5"
          />
          
        </div>

        <div class="flex-1">
          <ul class="pt-10 pb-10 space-y-1 text-sm">
            <li class="rounded-sm">
              <router-link to="/" class="flex items-center p-2 space-x-3 rounded-md">
                <svg
                  xmlns="http://www.w3.org/2000/svg"
                  fill="none"
                  viewBox="0 0 24 24"
                  stroke-width="1.5"
                  stroke="currentColor"
                  class="w-6 h-6 text-gray-100"
                >
                  <path
                    stroke-linecap="round"
                    stroke-linejoin="round"
                    d="M2.25 12l8.954-8.955c.44-.439 1.152-.439 1.591 0L21.75 12M4.5 9.75v10.125c0 .621.504 1.125 1.125 1.125H9.75v-4.875c0-.621.504-1.125 1.125-1.125h2.25c.621 0 1.125.504 1.125 1.125V21h4.125c.621 0 1.125-.504 1.125-1.125V9.75M8.25 21h8.25"
                  />
                </svg>

                <span class="text-gray-100 text-xl">Home</span>
              </router-link>
            </li>
            <li class="rounded-sm">
              <a href="#" class="flex items-center p-2 space-x-3 rounded-md">
                <svg
                  xmlns="http://www.w3.org/2000/svg"
                  fill="none"
                  viewBox="0 0 24 24"
                  stroke-width="1.5"
                  stroke="currentColor"
                  class="w-6 h-6 text-gray-100"
                >
                  <path
                    stroke-linecap="round"
                    stroke-linejoin="round"
                    d="M2.25 13.5h3.86a2.25 2.25 0 012.012 1.244l.256.512a2.25 2.25 0 002.013 1.244h3.218a2.25 2.25 0 002.013-1.244l.256-.512a2.25 2.25 0 012.013-1.244h3.859m-19.5.338V18a2.25 2.25 0 002.25 2.25h15A2.25 2.25 0 0021.75 18v-4.162c0-.224-.034-.447-.1-.661L19.24 5.338a2.25 2.25 0 00-2.15-1.588H6.911a2.25 2.25 0 00-2.15 1.588L2.35 13.177a2.25 2.25 0 00-.1.661z"
                  />
                </svg>

                <span class="text-gray-100 text-xl">My Work</span>
              </a>
            </li>

            <li class="rounded-sm">
              <a href="#" class="flex items-center p-2 space-x-3 rounded-md">
                <svg
                  xmlns="http://www.w3.org/2000/svg"
                  fill="none"
                  viewBox="0 0 24 24"
                  stroke-width="1.5"
                  stroke="currentColor"
                  class="w-6 h-6 text-gray-100 "
                >
                  <path
                    stroke-linecap="round"
                    stroke-linejoin="round"
                    d="M15.75 9V5.25A2.25 2.25 0 0013.5 3h-6a2.25 2.25 0 00-2.25 2.25v13.5A2.25 2.25 0 007.5 21h6a2.25 2.25 0 002.25-2.25V15M12 9l-3 3m0 0l3 3m-3-3h12.75"
                  />
                </svg>

                <span class="text-gray-100 text-xl"> Logout </span>
              </a>
            </li>
          </ul>
        </div>
      </div>
    </div>
    <div class="container mx-auto mt-12">
      <!-- <div class="grid grid-cols-1 gap-6 mb-6 lg:grid-cols-3">
       <MessageHeader/>
      </div> -->
      <RouterView />
    </div>
  </div>
</template>