<template>
    <audio controls>
      <source :src="src" type="audio/mpeg" />
      <source :src="src" type="audio/wav" />
    </audio>
</template>

<script>
export default {
  name: "AudioPlayer",
  props: {
    src: String,
  },
};
</script>
