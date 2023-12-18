<template>
  
    <td class="px-6 py-4 border-b border-gray-200 whitespace-nowrap">
      <div class="flex items-center">
        <div class="flex-shrink-0 w-10 h-10">
          {{ audio.title }}
        </div>

        <div class="ml-4">
          <div class="text-sm font-medium leading-5 text-gray-900">
            {{ audio.length }}
          </div>
          <div class="text-sm leading-5 text-gray-500">
            {{ audio.customer }}
          </div>
        </div>
      </div>
    </td>

    <td class="px-6 py-4 border-b border-gray-200 whitespace-nowrap">
      <div class="text-sm leading-5 text-gray-900">
        {{ audio.customer }}
      </div>
      <div class="text-sm leading-5 text-gray-500">
        {{ audio.customer }}
      </div>
    </td>

    <td class="px-6 py-4 border-b border-gray-200 whitespace-nowrap">
      <span
        class="inline-flex px-2 text-xs font-semibold leading-5 text-green-800 bg-green-100 rounded-full"
      >
        {{ audio.customer }}</span
      >
    </td>

    <td
      class="px-6 py-4 text-sm leading-5 text-gray-500 border-b border-gray-200 whitespace-nowrap"
    >
      {{ audio.customer }}
    </td>

    <td
      class="px-6 py-4 text-sm font-medium leading-5 text-right border-b border-gray-200 whitespace-nowrap"
    >
      <a href="#" class="text-sky-600 hover:text-indigo-900">Show Details</a>
    </td>

    <td
      class="px-6 py-4 text-sm font-medium leading-5 text-right border-b border-gray-200 whitespace-nowrap"
    >
      <a href="#" class="text-sky-600 hover:text-indigo-900">Edit</a>
    </td>
</template>

<script>
export default {
  name: 'Audio',
 
}
</script>
