<template>
  <q-page class="flex flex-center q-pa-md q-gutter-sm">
    <q-btn
      size="35px"
      label="歌曲管理"
      to="/songs"
      color="blue"
      icon="note"
    />

    <br/>

    <q-btn
      size="35px"
      label="用户管理"
      to="/users"
      color="blue"
      icon="people"
    />
  </q-page>

</template>

<script setup>
defineOptions({
  name: 'IndexPage'
});
</script>

