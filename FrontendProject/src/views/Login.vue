<template>
  <div class="max-w-7xl mx-auto grid grid-cols-2 gap-4">
    <div class="main-left">
      <div class="p-12 bg-white border border-gray-200 rounded-lg">
        <h1 class="mb-6 text-xl">Log in</h1>

        <p class="mb-6 text-gray-500">
          Lorem ipsum dolor sit mate. Lorem ipsum dolor sit mate. Lorem ipsum
          dolor sit mate. Lorem ipsum dolor sit mate. Lorem ipsum dolor sit
          mate. Lorem ipsum dolor sit mate.
        </p>

        <p class="font-bold">
          Don't have an account?
          <RouterLink :to="{ name: 'signup' }" class="underline"
            >Click here</RouterLink
          >
          to create one!
        </p>
      </div>
    </div>

    <div class="main-right">
      <div class="p-12 bg-white border border-gray-200 rounded-lg">
        <form class="space-y-6" v-on:submit.prevent="submitForm">
          <div>
            <label>User Name</label><br />
            <input
              type="text"
              v-model="form.email"
              placeholder="Your e-mail address"
              class="w-full mt-2 py-4 px-6 border border-gray-200 rounded-lg"
            />
          </div>

          <div>
            <label>Password</label><br />
            <input
              type="password"
              v-model="form.password"
              placeholder="Your password"
              class="w-full mt-2 py-4 px-6 border border-gray-200 rounded-lg"
            />
          </div>

          <template v-if="errors.length > 0">
            <div class="bg-red-300 text-white rounded-lg p-6">
              <p v-for="error in errors" v-bind:key="error">{{ error }}</p>
            </div>
          </template>

          <div>
            <button class="py-3 px-4 bg-sky-500 text-white rounded-lg">
              Login
            </button>
          </div>
        </form>
      </div>
    </div>
  </div>

  <div class="max-w-7xl mx-auto grid grid-cols-2 gap-4"></div>
</template>

<script>
import axios from "axios";

import { useUserStore } from "@/stores/user";
import { mapActions } from "pinia";
export default {
  name: "LoginView",

  data() {
    return {
      form: {
        email: "",
        password: "",
      },
      errors: [],
    };
  },
  methods: {
    ...mapActions(useUserStore, ["setUserInfo"]),

    async submitForm() {
      await axios
        .get("/api/me/")
        .then((response) => {
          useUserStore.setUserInfo(response.data);
          this.$router.push("/");
        })
        .catch((error) => {
          console.log("error", error);
        });
    },
  },
};
</script>
